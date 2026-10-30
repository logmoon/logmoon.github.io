"""Build the MARL cover figure: waiting time on the real district, from the
page's own benchmark table (mean over 3 seeds, medium demand, normal scenario).
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BG = "#191919"
TEXT = "#D4DDD8"
GREY = "#7a7f7c"
BROWN = "#9a8b7d"
ACCENT = "#d67933"

bars = [
    ("Max-Pressure", 8.9, GREY),
    ("One LLM call", 16.4, BROWN),
    ("LLM team", 8.7, ACCENT),
]

fig, ax = plt.subplots(figsize=(9, 5.4), dpi=100)
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)

xs = range(len(bars))
vals = [b[1] for b in bars]
ax.bar(xs, vals, width=0.55, color=[b[2] for b in bars], zorder=3)

for x, (label, v, _) in zip(xs, bars):
    ax.text(x, v + 0.45, f"{v:.1f}", ha="center", va="bottom",
            color=TEXT, fontsize=30, fontweight="bold", zorder=4)

ax.set_xticks(list(xs))
ax.set_xticklabels([b[0] for b in bars], color=TEXT, fontsize=19)
ax.set_ylim(0, 20)
ax.set_yticks([])
for side in ("top", "right", "left"):
    ax.spines[side].set_visible(False)
ax.spines["bottom"].set_color("#3a3a3a")
ax.tick_params(axis="x", length=0, pad=8)
ax.grid(axis="y", color="#2a2a2a", linewidth=1, zorder=0)

ax.text(0.005, 1.0, "Waiting time, seconds  ·  real district, normal demand",
        transform=ax.transAxes, color=GREY, fontsize=16, va="bottom")

fig.tight_layout()
fig.savefig("cover.png", facecolor=BG)
print("saved cover.png")
