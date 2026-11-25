"""QTAIM molecular-plane picture of the formic acid dimer for the website hero.

Density contours, gradient paths, interatomic-surface traces, bond paths,
nuclei, bond and ring critical points. Transparent background, light palette
for a blue banner.
"""
import sys
import numpy as np
from scipy.optimize import minimize
from scipy.interpolate import RegularGridInterpolator
from pyscf import gto, dft
from pyscf.dft import numint
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = sys.argv[1]

# ---------- geometry (C2h, built from standard parameters) ----------
d2r = np.pi / 180
rCO1, rCO2, rOH, rCH = 1.217, 1.311, 0.995, 1.092
aOCO, aHCO1, aCOH = 126.0, 122.0, 108.5


def monomer(theta):
    C = np.zeros(2)
    u1 = np.array([np.cos(theta), np.sin(theta)])
    O1 = C + rCO1 * u1                                   # carbonyl O
    t2 = theta + aOCO * d2r
    O2 = C + rCO2 * np.array([np.cos(t2), np.sin(t2)])  # hydroxyl O
    tH = theta - aHCO1 * d2r
    H1 = C + rCH * np.array([np.cos(tH), np.sin(tH)])   # formyl H
    v = C - O2
    v /= np.linalg.norm(v)
    cands = []
    for ang in (aCOH * d2r, -aCOH * d2r):                # rotate O2->C by C-O-H
        R = np.array([[np.cos(ang), -np.sin(ang)], [np.sin(ang), np.cos(ang)]])
        cands.append(O2 + rOH * (R @ v))
    H2 = min(cands, key=lambda h: np.linalg.norm(h - O1))  # syn (cis) to C=O
    return dict(C=C, O1=O1, O2=O2, H1=H1, H2=H2)


def build(p):
    theta, tx, ty = p
    m = {k: v + np.array([tx, ty]) for k, v in monomer(theta).items()}
    mB = {k: -v for k, v in m.items()}                   # inversion partner
    return m, mB


def cost(p):
    m, mB = build(p)
    dOO = np.linalg.norm(m["O2"] - mB["O1"])
    a = m["H2"] - m["O2"]
    b = mB["O1"] - m["O2"]
    cosang = a @ b / np.linalg.norm(a) / np.linalg.norm(b)
    return (dOO - 2.70) ** 2 + 0.5 * (1 - cosang) + 0.0 * theta_pen(p)


def theta_pen(p):
    return 0.0


best = min((minimize(cost, [t0, 1.5, 0.5], method="Nelder-Mead",
                     options=dict(xatol=1e-8, fatol=1e-12, maxiter=20000))
            for t0 in np.linspace(0, 2 * np.pi, 13)), key=lambda r: r.fun)
mA, mB = build(best.x)
atoms = []
for m in (mA, mB):
    for k in ("C", "O1", "O2", "H1", "H2"):
        atoms.append((k[0], m[k]))
xy = np.array([a[1] for a in atoms])
# orient the long axis along x
ctr = xy.mean(0)
xy -= ctr
w, V = np.linalg.eigh(xy.T @ xy)
xy = xy @ V[:, ::-1]
sym = [a[0] for a in atoms]
print("O...O:", np.linalg.norm(xy[2] - xy[6]), "fit", best.fun)

mol = gto.M(atom=[(s, (x, y, 0.0)) for s, (x, y) in zip(sym, xy)],
            basis="def2-tzvp", unit="Angstrom", verbose=0)
mf = dft.RKS(mol, xc="b3lyp").run()
dm = mf.make_rdm1()
print("E =", mf.e_tot)


def rho_grad(pts2d):
    pts = np.c_[pts2d, np.zeros(len(pts2d))] / 0.52917721092  # bohr
    ao = numint.eval_ao(mol, pts, deriv=1)
    r = numint.eval_rho(mol, ao, dm, xctype="GGA")
    return r[0], r[1:3].T


# ---------- grid ----------
B2A = 0.52917721092
xmin, xmax, ymin, ymax = -5.6, 5.6, -3.7, 3.7
nx, ny = 700, 470
X = np.linspace(xmin, xmax, nx)
Y = np.linspace(ymin, ymax, ny)
GX, GY = np.meshgrid(X, Y)
P = np.c_[GX.ravel(), GY.ravel()]
rho = np.empty(len(P))
grad = np.empty((len(P), 2))
for i in range(0, len(P), 20000):
    rho[i:i + 20000], grad[i:i + 20000] = rho_grad(P[i:i + 20000])
rho = rho.reshape(ny, nx)
gx = grad[:, 0].reshape(ny, nx)
gy = grad[:, 1].reshape(ny, nx)
Igx = RegularGridInterpolator((Y, X), gx, bounds_error=False, fill_value=0)
Igy = RegularGridInterpolator((Y, X), gy, bounds_error=False, fill_value=0)
Irho = RegularGridInterpolator((Y, X), np.log(rho), bounds_error=False, fill_value=-20)


def g_at(p):
    _, g = rho_grad(p[None, :])
    return g[0]


# ---------- critical points ----------
def hess(p, h=1e-3):
    H = np.zeros((2, 2))
    for k in range(2):
        e = np.zeros(2)
        e[k] = h
        H[:, k] = (g_at(p + e) - g_at(p - e)) / (2 * h)
    return 0.5 * (H + H.T)


def newton(p):
    for _ in range(60):
        g = g_at(p)
        H = hess(p)
        step = np.linalg.solve(H, -g)
        if np.linalg.norm(step) > 0.2:
            step *= 0.2 / np.linalg.norm(step)
        p = p + step
        if np.linalg.norm(step) < 1e-7:
            break
    return p, np.linalg.norm(g_at(p))


cps = []
n = len(xy)
for i in range(n):
    for j in range(i + 1, n):
        d = np.linalg.norm(xy[i] - xy[j])
        if d < 2.2:
            p, gn = newton(0.5 * (xy[i] + xy[j]))
            if gn < 1e-5 and min(np.linalg.norm(p - xy[k]) for k in range(n)) > 0.1:
                cps.append(p)
p, gn = newton(np.zeros(2))
if gn < 1e-5:
    cps.append(p)
uniq = []
for p in cps:
    if all(np.linalg.norm(p - q) > 0.05 for q in uniq):
        uniq.append(p)
bcps, rcps = [], []
for p in uniq:
    ev = np.linalg.eigvalsh(hess(p))
    (bcps if ev[0] < 0 < ev[1] else rcps).append(p)
print(len(bcps), "BCPs,", len(rcps), "RCPs (in-plane)")


# ---------- path integration on interpolated field ----------
def trace(p0, sign, nmax=4000, h=0.01, stop_nuc=True):
    pts = [p0]
    p = p0.copy()
    for _ in range(nmax):
        g = np.array([Igx((p[1], p[0])), Igy((p[1], p[0]))]).ravel()
        ng = np.linalg.norm(g)
        if ng < 1e-9:
            break
        p = p + sign * h * g / ng
        if not (xmin < p[0] < xmax and ymin < p[1] < ymax):
            break
        pts.append(p.copy())
        if stop_nuc and sign > 0 and min(np.linalg.norm(p - q) for q in xy) < 0.03:
            break
        if sign < 0 and Irho((p[1], p[0])) < np.log(2e-4):
            break
        if sign < 0 and len(pts) > 20 and any(np.linalg.norm(p - q) < 0.03 for q in bcps + rcps):
            break
    return np.array(pts)


grad_paths = []
for k, q in enumerate(xy):
    nang = 36 if sym[k] != "H" else 22
    for a in np.linspace(0, 2 * np.pi, nang, endpoint=False):
        grad_paths.append(trace(q + 0.06 * np.array([np.cos(a), np.sin(a)]), -1))

ias, bpaths = [], []
for p in bcps:
    w, V = np.linalg.eigh(hess(p))
    vneg, vpos = V[:, 0], V[:, 1]
    for s in (1, -1):
        ias.append(trace(p + s * 0.01 * vneg, -1))
        bpaths.append(trace(p + s * 0.01 * vpos, +1))

# ---------- draw ----------
fig = plt.figure(figsize=(12, 12 * (ymax - ymin) / (xmax - xmin)), dpi=150)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)
ax.set_aspect("equal")
ax.axis("off")
levels = sorted({s * 10.0 ** e for e in range(-3, 2) for s in (1, 2, 4, 8)})
levels = [l for l in levels if 1e-3 <= l <= 3.0]
ax.contour(GX, GY, rho, levels=levels, colors="white", linewidths=0.7, alpha=0.35)
for gp in grad_paths:
    ax.plot(gp[:, 0], gp[:, 1], color="#bbdefb", lw=0.5, alpha=0.55)
for s in ias:
    ax.plot(s[:, 0], s[:, 1], color="#ffd54f", lw=2.0, alpha=0.95)
for b in bpaths:
    ax.plot(b[:, 0], b[:, 1], color="white", lw=2.4, alpha=0.95)
col = {"C": "#90a4ae", "O": "#ef5350", "H": "#f5f5f5"}
size = {"C": 260, "O": 280, "H": 140}
for s, q in zip(sym, xy):
    ax.scatter(*q, s=size[s], color=col[s], edgecolor="white", linewidth=1.2, zorder=5)
for p in bcps:
    ax.scatter(*p, s=45, color="#ff7043", edgecolor="white", linewidth=0.8, zorder=6)
for p in rcps:
    ax.scatter(*p, s=55, marker="s", color="#ffee58", edgecolor="white", linewidth=0.8, zorder=6)
fig.savefig(OUT, transparent=True)
print("saved", OUT)
