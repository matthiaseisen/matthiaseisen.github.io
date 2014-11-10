# -(1)
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.add_patch(
    patches.Rectangle(
        (0.1, 0.1),   # (x,y)
        0.5,          # width
        0.5,          # height
    )
)
fig1.savefig('rect1.png', dpi=90, bbox_inches='tight')
# -(/1)

# -(2)
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.add_patch(
    patches.Rectangle(
        (0.1, 0.1),
        0.5,
        0.5,
        fill=False      # remove background
    )
)
fig2.savefig('rect2.png', dpi=90, bbox_inches='tight')
# -(/2)

# -(3)
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig3 = plt.figure()
ax3 = fig3.add_subplot(111)
for p in [
    patches.Rectangle(
        (0.1, 0.1), 0.3, 0.6,
        hatch='/'
    ),
    patches.Rectangle(
        (0.5, 0.1), 0.3, 0.6,
        hatch='\\',
        fill=False
    ),
]:
    ax3.add_patch(p)
fig3.savefig('rect3.png', dpi=90, bbox_inches='tight')
# -(/3)

# -(4)
import matplotlib.pyplot as plt
import matplotlib.patches as patches

patterns = ['-', '+', 'x', 'o', 'O', '.', '*']  # more patterns
fig4 = plt.figure()
ax4 = fig4.add_subplot(111)
for p in [
    patches.Rectangle(
        (0.05 + (i * 0.13), 0.1),
        0.1,
        0.6,
        hatch=patterns[i],
        fill=False
    ) for i in range(len(patterns))
]:
    ax4.add_patch(p)
fig4.savefig('rect4.png', dpi=90, bbox_inches='tight')
# -(/4)

# -(5)
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig5 = plt.figure()
ax5 = fig5.add_subplot(111)
for p in [
    patches.Rectangle(
        (0.03, 0.1), 0.2, 0.6,
        alpha=None,
    ),
    patches.Rectangle(
        (0.26, 0.1), 0.2, 0.6,
        alpha=1.0
    ),
    patches.Rectangle(
        (0.49, 0.1), 0.2, 0.6,
        alpha=0.6
    ),
    patches.Rectangle(
        (0.72, 0.1), 0.2, 0.6,
        alpha=0.1
    ),
]:
    ax5.add_patch(p)
fig5.savefig('rect5.png', dpi=90, bbox_inches='tight')
# -(/5)

# -(6)
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig6 = plt.figure()
ax6 = fig6.add_subplot(111)
for p in [
    patches.Rectangle(
        (0.03, 0.1), 0.2, 0.6,
        facecolor=None      # Default
    ),
    patches.Rectangle(
        (0.26, 0.1), 0.2, 0.6,
        facecolor="none"     # No background
    ),
    patches.Rectangle(
        (0.49, 0.1), 0.2, 0.6,
        facecolor="red"
    ),
    patches.Rectangle(
        (0.72, 0.1), 0.2, 0.6,
        facecolor="#00ffff"
    ),
]:
    ax6.add_patch(p)
fig6.savefig('rect6.png', dpi=90, bbox_inches='tight')
# -(/6)

# -(7)
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig7 = plt.figure()
ax7 = fig7.add_subplot(111)
for p in [
    patches.Rectangle(
        (0.03, 0.1), 0.2, 0.6, fill=False,
        edgecolor=None      # Default
    ),
    patches.Rectangle(
        (0.26, 0.1), 0.2, 0.6, fill=False,
        edgecolor="none"     # No border
    ),
    patches.Rectangle(
        (0.49, 0.1), 0.2, 0.6, fill=False,
        edgecolor="red"
    ),
    patches.Rectangle(
        (0.72, 0.1), 0.2, 0.6, fill=False,
        edgecolor="#0000ff"
    ),
]:
    ax7.add_patch(p)
fig7.savefig('rect7.png', dpi=90, bbox_inches='tight')
# -(/7)

# -(8)
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig8 = plt.figure()
ax8 = fig8.add_subplot(111)
for p in [
    patches.Rectangle(
        (0.03, 0.1), 0.2, 0.6, fill=False,
        linewidth=None      # Default
    ),
    patches.Rectangle(
        (0.26, 0.1), 0.2, 0.6, fill=False,
        linewidth=0
    ),
    patches.Rectangle(
        (0.49, 0.1), 0.2, 0.6, fill=False,
        linewidth=0.5
    ),
    patches.Rectangle(
        (0.72, 0.1), 0.2, 0.6, fill=False,
        linewidth=3
    ),
]:
    ax8.add_patch(p)
fig8.savefig('rect8.png', dpi=90, bbox_inches='tight')
# -(/8)

# -(9)
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig9 = plt.figure()
ax9 = fig9.add_subplot(111)
for p in [
    patches.Rectangle(
        (0.03, 0.1), 0.2, 0.6, fill=False,
        linestyle='solid'   # Default
    ),
    patches.Rectangle(
        (0.26, 0.1), 0.2, 0.6, fill=False,
        linestyle='dashed'
    ),
    patches.Rectangle(
        (0.49, 0.1), 0.2, 0.6, fill=False,
        linestyle='dashdot'
    ),
    patches.Rectangle(
        (0.72, 0.1), 0.2, 0.6, fill=False,
        linestyle='dotted'
    ),
]:
    ax9.add_patch(p)
fig9.savefig('rect9.png', dpi=90, bbox_inches='tight')
# -(/9)
