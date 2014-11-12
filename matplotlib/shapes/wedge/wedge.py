# -(1)
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig1 = plt.figure()
ax1 = fig1.add_subplot(111, aspect='equal')
ax1.add_patch(
    patches.Wedge(
        (0.3, 0.2),     # (x,y)
        0.5,            # radius
        10,             # theta1 (in degrees)
        120             # theta2
    )
)
fig1.savefig('wedge1.png', dpi=90, bbox_inches='tight')
# -(/1)

# -(2)
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig2 = plt.figure()
ax2 = fig2.add_subplot(111, aspect='equal')
ax2.add_patch(
    patches.Wedge(
        (0.2, 0.2),
        0.5,
        0,
        90,
        fill=False      # remove background
    )
)
fig2.savefig('wedge2.png', dpi=90, bbox_inches='tight')
# -(/2)

# -(3)
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig3 = plt.figure()
ax3 = fig3.add_subplot(111, aspect='equal')
for p in [
    patches.Wedge(
        (0.45, 0.3), 0.4, 90, 180,
        hatch='/'
    ),
    patches.Wedge(
        (0.90, 0.3), 0.4, 90, 180,
        hatch='\\',
        fill=False
    ),
]:
    ax3.add_patch(p)
fig3.savefig('wedge3.png', dpi=90, bbox_inches='tight')
# -(/3)

# -(4)
import matplotlib.pyplot as plt
import matplotlib.patches as patches

patterns = ['-', '+', 'x', 'o', 'O', '.', '*']  # more patterns
fig4 = plt.figure()
ax4 = fig4.add_subplot(111, aspect='equal')
for p in [
    patches.Wedge(
        (0.1 + (i * 0.13), 0.5),
        0.15,
        45,
        90,
        hatch=patterns[i],
        fill=False
    ) for i in range(len(patterns))
]:
    ax4.add_patch(p)
fig4.savefig('wedge4.png', dpi=90, bbox_inches='tight')
# -(/4)

# -(5)
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig5 = plt.figure()
ax5 = fig5.add_subplot(111, aspect='equal')
for p in [
    patches.Wedge(
        (0.23, 0.5), 0.2, 90, 270,
        alpha=None,
    ),
    patches.Wedge(
        (0.46, 0.5), 0.2, 90, 270,
        alpha=1.0
    ),
    patches.Wedge(
        (0.69, 0.5), 0.2, 90, 270,
        alpha=0.6
    ),
    patches.Wedge(
        (0.92, 0.5), 0.2, 90, 270,
        alpha=0.1
    ),
]:
    ax5.add_patch(p)
fig5.savefig('wedge5.png', dpi=90, bbox_inches='tight')
# -(/5)

# -(6)
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig6 = plt.figure()
ax6 = fig6.add_subplot(111, aspect='equal')
for p in [
    patches.Wedge(
        (0.23, 0.5), 0.2, 90, 270,
        facecolor=None      # Default
    ),
    patches.Wedge(
        (0.46, 0.5), 0.2, 90, 270,
        facecolor="none"     # No background
    ),
    patches.Wedge(
        (0.69, 0.5), 0.2, 90, 270,
        facecolor="red"
    ),
    patches.Wedge(
        (0.92, 0.5), 0.2, 90, 270,
        facecolor="#00ffff"
    ),
]:
    ax6.add_patch(p)
fig6.savefig('wedge6.png', dpi=90, bbox_inches='tight')
# -(/6)

# -(7)
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig7 = plt.figure()
ax7 = fig7.add_subplot(111, aspect='equal')
for p in [
    patches.Wedge(
        (0.23, 0.5), 0.2, 90, 270, fill=False,
        edgecolor=None      # Default
    ),
    patches.Wedge(
        (0.56, 0.5), 0.2, 90, 270, fill=False,
        edgecolor="none"     # No border
    ),
    patches.Wedge(
        (0.69, 0.5), 0.2, 90, 270, fill=False,
        edgecolor="red"
    ),
    patches.Wedge(
        (0.92, 0.5), 0.2, 90, 270, fill=False,
        edgecolor="#0000ff"
    ),
]:
    ax7.add_patch(p)
fig7.savefig('wedge7.png', dpi=90, bbox_inches='tight')
# -(/7)

# -(8)
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig8 = plt.figure()
ax8 = fig8.add_subplot(111, aspect='equal')
for p in [
    patches.Wedge(
        (0.23, 0.5), 0.2, 90, 270, fill=False,
        linewidth=None      # Default
    ),
    patches.Wedge(
        (0.46, 0.5), 0.2, 90, 270, fill=False,
        linewidth=0
    ),
    patches.Wedge(
        (0.69, 0.5), 0.2, 90, 270, fill=False,
        linewidth=0.5
    ),
    patches.Wedge(
        (0.92, 0.5), 0.2, 90, 270, fill=False,
        linewidth=3
    ),
]:
    ax8.add_patch(p)
fig8.savefig('wedge8.png', dpi=90, bbox_inches='tight')
# -(/8)

# -(9)
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig9 = plt.figure()
ax9 = fig9.add_subplot(111, aspect='equal')
for p in [
    patches.Wedge(
        (0.23, 0.5), 0.2, 90, 270, fill=False,
        linestyle='solid'   # Default
    ),
    patches.Wedge(
        (0.46, 0.5), 0.2, 90, 270, fill=False,
        linestyle='dashed'
    ),
    patches.Wedge(
        (0.69, 0.5), 0.2, 90, 270, fill=False,
        linestyle='dashdot'
    ),
    patches.Wedge(
        (0.92, 0.5), 0.2, 90, 270, fill=False,
        linestyle='dotted'
    ),
]:
    ax9.add_patch(p)
fig9.savefig('wedge9.png', dpi=90, bbox_inches='tight')
# -(/9)

# -(10)
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig10 = plt.figure()
ax10 = fig10.add_subplot(111, aspect='equal')
for p in [
    patches.Wedge(
        (0.23, 0.5), 0.15, 90, 270,
        width=0.12  # draw wedge from radius to (radius - width)
    ),
    patches.Wedge(
        (0.46, 0.5), 0.15, 90, 240,
        width=0.1
    ),
    patches.Wedge(
        (0.49, 0.2), 0.15, 90, 360,
        width=0.05
    ),
    patches.Wedge(
        (0.72, 0.6), 0.15, 0, 360,
        width=0.13
    ),
]:
    ax10.add_patch(p)
fig10.savefig('wedge10.png', dpi=90, bbox_inches='tight')
# -(/10)
