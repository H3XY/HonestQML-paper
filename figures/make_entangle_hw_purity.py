"""Figure: 2-qubit purity test on ibm_marrakesh vs FakeMarrakesh (identical circuits), accuracy vs copies.

Reads H3XY/Entangle results/review_purity_hw.json (recalibrated 'after' curves, mean over 30
shot subsamples; 95% bootstrap intervals over the 60 test states). Points are the mean of the two
runs; bars span the lowest lower and highest upper bound of the two runs.
Usage: python figures/make_entangle_hw_purity.py [path/to/review_purity_hw.json]
"""
import json
import os
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "..", "Entangle", "results", "review_purity_hw.json")
d = json.load(open(SRC))
C = np.array(d["copies"])
TEXT, TEXT2, SURFACE, GRID = "#0b0b0b", "#52514e", "#fcfcfb", "#e4e3df"
SERIES = [("QNN 2-copy", "ibm_marrakesh", "QNN two-copy, ibm_marrakesh", "#2a78d6", "-", "o"),
          ("QNN 2-copy", "FakeMarrakesh (identical circuits)", "QNN two-copy, FakeMarrakesh", "#2a78d6", (0, (4, 3)), "o"),
          ("Shadows, global purity (2 params)", "ibm_marrakesh", "Classical shadows, ibm_marrakesh", "#eb6834", "-", "D"),
          ("Shadows, global purity (2 params)", "FakeMarrakesh (identical circuits)", "Classical shadows, FakeMarrakesh", "#eb6834", (0, (4, 3)), "D")]

fig, ax = plt.subplots(figsize=(7, 3.6), dpi=170)
fig.patch.set_facecolor(SURFACE)
ax.set_facecolor(SURFACE)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
for s in ("left", "bottom"):
    ax.spines[s].set_color(GRID)
ax.tick_params(colors=TEXT2, labelsize=8)
ax.grid(color=GRID, linewidth=0.8, zorder=0)
ax.axhline(0.9, color=TEXT2, linewidth=0.8, linestyle=":")
ax.text(13, 0.905, "90%", color=TEXT2, fontsize=7.5, va="bottom")
for method, dev, label, color, ls, marker in SERIES:
    runs = [d["runs"][f"{dev}, run {k}"][method] for k in (1, 2)]
    m = np.array([[np.nan if v is None else v for v in r["after"]] for r in runs], float).mean(axis=0)
    lo = np.min([[np.nan if c is None else c[0] for c in r["after_ci"]] for r in runs], axis=0)
    hi = np.max([[np.nan if c is None else c[1] for c in r["after_ci"]] for r in runs], axis=0)
    ok = ~np.isnan(m)
    ax.errorbar(C[ok], m[ok], yerr=[m[ok] - lo[ok], hi[ok] - m[ok]], fmt="none", ecolor=color, elinewidth=1, capsize=0, zorder=2)
    ax.plot(C[ok], m[ok], color=color, linestyle=ls, linewidth=2, marker=marker, markersize=5,
            markeredgecolor=SURFACE, markeredgewidth=1.2, label=label, zorder=3)
ax.set_xscale("log", base=2)
ax.set_xticks(C)
ax.set_xticklabels([str(c) for c in C])
ax.set_ylim(0.6, 1.02)
ax.set_xlabel("Copies of each test state (state preparations)", color=TEXT2, fontsize=9)
ax.set_ylabel("Test accuracy (recalibrated)", color=TEXT2, fontsize=9)
ax.legend(frameon=False, fontsize=7.5, labelcolor=TEXT, loc="lower right", handlelength=4)
fig.tight_layout()
fig.savefig(os.path.join(HERE, "entangle_hw_purity.png"), facecolor=SURFACE)
print("Wrote figures/entangle_hw_purity.png")
