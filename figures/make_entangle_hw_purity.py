"""Figure: 2-qubit purity test on ibm_marrakesh vs FakeMarrakesh, accuracy vs copies.

Numbers from H3XY/Entangle results/review_hardware.md (stage 7; mean +- std over 2 runs,
subsampled from device counts, recalibrated on 20 labelled device states).
Usage: python figures/make_entangle_hw_purity.py  -> figures/entangle_hw_purity.png
"""
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

COPIES = [16, 32, 64, 128, 256, 512, 1024]
DATA = {  # (label, color, linestyle, means, stds); None = not measured
    "QNN two-copy, ibm_marrakesh": ("#2a78d6", "-", [0.773, 0.856, 0.929, 0.976, 0.999, 1.000, 1.000],
                                    [0.026, 0.012, 0.005, 0.002, 0.000, 0.000, 0.000]),
    "QNN two-copy, FakeMarrakesh": ("#2a78d6", (0, (4, 3)), [0.838, 0.908, 0.965, 0.992, 1.000, 1.000, 1.000],
                                    [0.002, 0.009, 0.011, 0.001, 0.000, 0.000, 0.000]),
    "Classical shadows, ibm_marrakesh": ("#eb6834", "-", [None, 0.653, 0.790, 0.907, 0.963, 0.986, 1.000],
                                         [None, 0.008, 0.018, 0.012, 0.001, 0.005, 0.000]),
    "Classical shadows, FakeMarrakesh": ("#eb6834", (0, (4, 3)), [None, 0.671, 0.813, 0.910, 0.964, 0.987, 1.000],
                                         [None, 0.020, 0.019, 0.011, 0.010, 0.011, 0.000]),
}
TEXT, TEXT2, SURFACE, GRID = "#0b0b0b", "#52514e", "#fcfcfb", "#e4e3df"

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
for label, (color, ls, m, sd) in DATA.items():
    xs = [c for c, v in zip(COPIES, m) if v is not None]
    ys = [v for v in m if v is not None]
    es = [e for e in sd if e is not None]
    marker = "o" if label.startswith("QNN") else "D"
    ax.errorbar(xs, ys, yerr=es, fmt="none", ecolor=color, elinewidth=1, capsize=0, zorder=2)
    ax.plot(xs, ys, color=color, linestyle=ls, linewidth=2, marker=marker, markersize=5,
            markeredgecolor=SURFACE, markeredgewidth=1.2, label=label, zorder=3)
ax.set_xscale("log", base=2)
ax.set_xticks(COPIES)
ax.set_xticklabels([str(c) for c in COPIES])
ax.set_ylim(0.6, 1.02)
ax.set_xlabel("Copies of each test state", color=TEXT2, fontsize=9)
ax.set_ylabel("Test accuracy (recalibrated)", color=TEXT2, fontsize=9)
ax.legend(frameon=False, fontsize=7.5, labelcolor=TEXT, loc="lower right", handlelength=4)
fig.tight_layout()
fig.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)), "entangle_hw_purity.png"), facecolor=SURFACE)
print("Wrote figures/entangle_hw_purity.png")
