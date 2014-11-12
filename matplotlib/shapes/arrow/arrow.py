# -(1)
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig1 = plt.figure()
ax1 = fig1.add_subplot(111, aspect='equal')
ax1.add_patch(
    patches.Arrow(
        0.3,            # x
        0.2,            # y
        0.5,            # dx
        0.5,            # dy
        width=0.2       # optional - defaults to 1.0
    )
)
fig1.savefig('arrow1.png', dpi=90, bbox_inches='tight')
# -(/1)

# -(2)
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig2 = plt.figure()
ax2 = fig2.add_subplot(111, aspect='equal')
ax2.add_patch(
    patches.Arrow(
        0.6,
        0.8,
        0,
        -0.6,
        width=0.4,
        fill=False      # remove background
    )
)
fig2.savefig('arrow2.png', dpi=90, bbox_inches='tight')
# -(/2)

# -(3)
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig3 = plt.figure()
ax3 = fig3.add_subplot(111, aspect='equal')
for p in [
    patches.Arrow(
        0.3, 0.2, 0, 0.5, width=0.5,
        hatch='/'
    ),
    patches.Arrow(
        0.7, 0.2, 0, 0.5, width=0.5,
        hatch='\\',
        fill=False
    ),
]:
    ax3.add_patch(p)
fig3.savefig('arrow3.png', dpi=90, bbox_inches='tight')
# -(/3)

# -(4)
import matplotlib.pyplot as plt
import matplotlib.patches as patches

patterns = ['-', '+', 'x', 'o', 'O', '.', '*']  # more patterns
fig4 = plt.figure()
ax4 = fig4.add_subplot(111, aspect='equal')
for p in [
    patches.Arrow(
        0.1 + (i * 0.13),
        0.8,
        0,
        -0.6,
        width=0.2,
        hatch=patterns[i],
        fill=False
    ) for i in range(len(patterns))
]:
    ax4.add_patch(p)
fig4.savefig('arrow4.png', dpi=90, bbox_inches='tight')
# -(/4)

# -(5)
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig5 = plt.figure()
ax5 = fig5.add_subplot(111, aspect='equal')
for p in [
    patches.Arrow(
        0.04, 0.2, 0.3, 0.6, width=0.4,
        alpha=None,
    ),
    patches.Arrow(
        0.24, 0.2, 0.3, 0.6, width=0.4,
        alpha=1.0
    ),
    patches.Arrow(
        0.44, 0.2, 0.3, 0.6, width=0.4,
        alpha=0.6
    ),
    patches.Arrow(
        0.64, 0.2, 0.3, 0.6, width=0.4,
        alpha=0.1
    ),
]:
    ax5.add_patch(p)
fig5.savefig('arrow5.png', dpi=90, bbox_inches='tight')
# -(/5)

# -(6)
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig6 = plt.figure()
ax6 = fig6.add_subplot(111, aspect='equal')
for p in [
    patches.Arrow(
        0.04, 0.2, 0.3, 0.6, width=0.4,
        facecolor=None      # Default
    ),
    patches.Arrow(
        0.24, 0.2, 0.3, 0.6, width=0.4,
        facecolor="none"     # No background
    ),
    patches.Arrow(
        0.44, 0.2, 0.3, 0.6, width=0.4,
        facecolor="red"
    ),
    patches.Arrow(
        0.64, 0.2, 0.3, 0.6, width=0.4,
        facecolor="#00ffff"
    ),
]:
    ax6.add_patch(p)
fig6.savefig('arrow6.png', dpi=90, bbox_inches='tight')
# -(/6)

# -(7)
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig7 = plt.figure()
ax7 = fig7.add_subplot(111, aspect='equal')
for p in [
    patches.Arrow(
        0.04, 0.2, 0.3, 0.6, width=0.4, fill=False,
        edgecolor=None      # Default
    ),
    patches.Arrow(
        0.24, 0.2, 0.3, 0.6, width=0.4, fill=False,
        edgecolor="none"     # No border
    ),
    patches.Arrow(
        0.44, 0.2, 0.3, 0.6, width=0.4, fill=False,
        edgecolor="red"
    ),
    patches.Arrow(
        0.64, 0.2, 0.3, 0.6, width=0.4, fill=False,
        edgecolor="#0000ff"
    ),
]:
    ax7.add_patch(p)
fig7.savefig('arrow7.png', dpi=90, bbox_inches='tight')
# -(/7)

# -(8)
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig8 = plt.figure()
ax8 = fig8.add_subplot(111, aspect='equal')
for p in [
    patches.Arrow(
        0.04, 0.2, 0.3, 0.6, width=0.4, fill=False,
        linewidth=None      # Default
    ),
    patches.Arrow(
        0.24, 0.2, 0.3, 0.6, width=0.4, fill=False,
        linewidth=0
    ),
    patches.Arrow(
        0.44, 0.2, 0.3, 0.6, width=0.4, fill=False,
        linewidth=0.5
    ),
    patches.Arrow(
        0.64, 0.2, 0.3, 0.6, width=0.4, fill=False,
        linewidth=3
    ),
]:
    ax8.add_patch(p)
fig8.savefig('arrow8.png', dpi=90, bbox_inches='tight')
# -(/8)

# -(9)
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig9 = plt.figure()
ax9 = fig9.add_subplot(111, aspect='equal')
for p in [
    patches.Arrow(
        0.04, 0.2, 0.3, 0.6, width=0.4, fill=False,
        linestyle='solid'   # Default
    ),
    patches.Arrow(
        0.24, 0.2, 0.3, 0.6, width=0.4, fill=False,
        linestyle='dashed'
    ),
    patches.Arrow(
        0.44, 0.2, 0.3, 0.6, width=0.4, fill=False,
        linestyle='dashdot'
    ),
    patches.Arrow(
        0.64, 0.2, 0.3, 0.6, width=0.4, fill=False,
        linestyle='dotted'
    ),
]:
    ax9.add_patch(p)
fig9.savefig('arrow9.png', dpi=90, bbox_inches='tight')
# -(/9)

# -(10)
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig10 = plt.figure()
ax10 = fig10.add_subplot(111, aspect='equal')
for p in [
    patches.FancyArrow(
        0.04, 0.2, 0.3, 0.6,
        width=0.001,        # Default
        head_width=0.05,    # Default: 3 * width
        head_length=0.06    # Default: 1.5 * head_width
    ),
    patches.FancyArrow(
        0.24, 0.2, 0.3, 0.6, width=0.01,
        head_width=0.01,
    ),
    patches.FancyArrow(
        0.44, 0.2, 0.3, 0.6, width=0.02,
        head_width=0.02,
        head_length=0.1
    ),
    patches.FancyArrow(
        0.64, 0.2, 0.3, 0.6, width=0.01,
        head_width=0.08,
        head_length=0.04,
        length_includes_head=True   # Default: False
    ),
]:
    ax10.add_patch(p)
fig10.savefig('arrow10.png', dpi=90, bbox_inches='tight')
# -(/10)

# -(11)
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig11 = plt.figure()
ax11 = fig11.add_subplot(111, aspect='equal')
for p in [
    patches.FancyArrowPatch(
        (0.04, 0.2),
        (0.14, 0.8),
        arrowstyle='simple',    # Default
        mutation_scale=20
    ),
    patches.FancyArrowPatch(
        (0.24, 0.2),
        (0.34, 0.8),
        arrowstyle='->',
        mutation_scale=30
    ),
    patches.FancyArrowPatch(
        (0.44, 0.2),
        (0.54, 0.8),
        arrowstyle='wedge',
        mutation_scale=30
    ),
    patches.FancyArrowPatch(
        (0.64, 0.2),
        (0.74, 0.8),
        arrowstyle='fancy',
        mutation_scale=30
    ),
]:
    ax11.add_patch(p)
fig11.savefig('arrow11.png', dpi=90, bbox_inches='tight')
# -(/11)

# -(12)
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig12 = plt.figure()
ax12 = fig12.add_subplot(111, aspect='equal')

# More styles:
styles = ['<-', '<->', '-', '-|>', '<|-', '<|-|>', '-[', ']-', ']-[', '|-|']

for p in [
    patches.FancyArrowPatch(
        (0.02 + i * 0.1, 0.2),
        (0.02 + i * 0.1, 0.8),
        arrowstyle=styles[i],
        mutation_scale=20
    ) for i in range(len(styles))
]:
    ax12.add_patch(p)
fig12.savefig('arrow12.png', dpi=90, bbox_inches='tight')
# -(/12)

# -(13)
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig13 = plt.figure()
ax13 = fig13.add_subplot(111, aspect='equal')
for p in [
    patches.FancyArrowPatch(
        (0.04, 0.2),
        (0.24, 0.8),
        connectionstyle='arc3',    # Default
        mutation_scale=20
    ),
    patches.FancyArrowPatch(
        (0.34, 0.2),
        (0.34, 0.8),
        connectionstyle='arc3, rad=0.7',
        mutation_scale=20
    ),
    patches.FancyArrowPatch(
        (0.74, 0.2),
        (0.94, 0.8),
        connectionstyle='arc3, rad=-0.5',
        mutation_scale=20
    ),
]:
    ax13.add_patch(p)
fig13.savefig('arrow13.png', dpi=90, bbox_inches='tight')
# -(/13)
