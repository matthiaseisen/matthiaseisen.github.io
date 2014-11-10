import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig1 = plt.figure()
ax1 = fig1.add_subplot(
    111,
    frameon=False,
    xlim=[0, 1.1],
    ylim=[0, 1.1],
    xticks=[],
    yticks=[]
)
ax1.add_patch(
    patches.Ellipse(
        (0.5, 0.6),   # (x,y)
        1,            # width
        1,            # height
    )
)
fig1.savefig('ellipse1.png', dpi=90, bbox_inches='tight')

fig2 = plt.figure()
ax2 = fig2.add_subplot(
    111,
    frameon=False,
    xlim=[0, 1.1],
    ylim=[0, 1.1],
    xticks=[],
    yticks=[]
)
ax2.add_patch(
    patches.Ellipse(
        (0, 0.1),
        1,
        1,
        fill=False      # remove background
    )
)
fig2.savefig('ellipse2.png', dpi=90, bbox_inches='tight')

fig3 = plt.figure()
ax3 = fig3.add_subplot(
    111,
    frameon=False,
    xlim=[0, 2.2],
    ylim=[0, 1.1],
    xticks=[],
    yticks=[]
)
for p in [
    patches.Ellipse(
        (0, 0.1), 1, 1,
        hatch='/'
    ),
    patches.Ellipse(
        (1.1, 0.1), 1, 1,
        hatch='\\',
        fill=False
    ),
]:
    ax3.add_patch(p)
fig3.savefig('ellipse3.png', dpi=90, bbox_inches='tight')

patterns = ['-', '+', 'x', 'o', 'O', '.', '*']
fig4 = plt.figure()
ax4 = fig4.add_subplot(
    111,
    frameon=False,
    xlim=[0, 1.1 * len(patterns) + 0.1],
    ylim=[0, 1.1],
    xticks=[],
    yticks=[]
)
for p in [
    patches.Ellipse(
        (0.1 + (i * 1.1), 0.1),
        1,
        1,
        hatch=patterns[i],
        fill=False
    ) for i in range(len(patterns))
]:
    ax4.add_patch(p)
fig4.savefig('ellipse4.png', dpi=90, bbox_inches='tight')

fig5 = plt.figure()
ax5 = fig5.add_subplot(
    111,
    frameon=False,
    xlim=[0, 4.4],
    ylim=[0, 1.1],
    xticks=[],
    yticks=[]
)
for p in [
    patches.Ellipse(
        (0, 0.1), 1, 1,
        alpha=None,
    ),
    patches.Ellipse(
        (1.1, 0.1), 1, 1,
        alpha=1.0
    ),
    patches.Ellipse(
        (2.2, 0.1), 1, 1,
        alpha=0.6
    ),
    patches.Ellipse(
        (3.3, 0.1), 1, 1,
        alpha=0.1
    ),
]:
    ax5.add_patch(p)
fig5.savefig('ellipse5.png', dpi=90, bbox_inches='tight')

fig6 = plt.figure()
ax6 = fig6.add_subplot(
    111,
    frameon=False,
    xlim=[0, 4.4],
    ylim=[0, 1.2],
    xticks=[],
    yticks=[]
)
for p in [
    patches.Ellipse(
        (0, 0.1), 1, 1,
        facecolor=None      # Default
    ),
    patches.Ellipse(
        (1.1, 0.1), 1, 1,
        facecolor="none"     # No background
    ),
    patches.Ellipse(
        (2.2, 0.1), 1, 1,
        facecolor="red"
    ),
    patches.Ellipse(
        (3.3, 0.1), 1, 1,
        facecolor="#00ffff"
    ),
]:
    ax6.add_patch(p)
fig6.savefig('ellipse6.png', dpi=90, bbox_inches='tight')

fig7 = plt.figure()
ax7 = fig7.add_subplot(
    111,
    frameon=False,
    xlim=[0, 4.4],
    ylim=[0, 1.2],
    xticks=[],
    yticks=[]
)
for p in [
    patches.Ellipse(
        (0, 0.1), 1, 1, fill=False,
        edgecolor=None      # Default
    ),
    patches.Ellipse(
        (1.1, 0.1), 1, 1, fill=False,
        edgecolor="none"     # No border
    ),
    patches.Ellipse(
        (2.2, 0.1), 1, 1, fill=False,
        edgecolor="red"
    ),
    patches.Ellipse(
        (3.3, 0.1), 1, 1, fill=False,
        edgecolor="#0000ff"
    ),
]:
    ax7.add_patch(p)
fig7.savefig('ellipse7.png', dpi=90, bbox_inches='tight')

fig8 = plt.figure()
ax8 = fig8.add_subplot(
    111,
    frameon=False,
    xlim=[0, 4.4],
    ylim=[0, 1.2],
    xticks=[],
    yticks=[]
)
for p in [
    patches.Ellipse(
        (0, 0.1), 1, 1, fill=False,
        linewidth=None      # Default
    ),
    patches.Ellipse(
        (1.1, 0.1), 1, 1, fill=False,
        linewidth=0
    ),
    patches.Ellipse(
        (2.2, 0.1), 1, 1, fill=False,
        linewidth=0.5
    ),
    patches.Ellipse(
        (3.3, 0.1), 1, 1, fill=False,
        linewidth=3
    ),
]:
    ax8.add_patch(p)
fig8.savefig('ellipse8.png', dpi=90, bbox_inches='tight')

fig9 = plt.figure()
ax9 = fig9.add_subplot(
    111,
    frameon=False,
    xlim=[0, 4.4],
    ylim=[0, 1.2],
    xticks=[],
    yticks=[]
)
for p in [
    patches.Ellipse(
        (0, 0.1), 1, 1, fill=False,
        linestyle='solid'   # Default
    ),
    patches.Ellipse(
        (1.1, 0.1), 1, 1, fill=False,
        linestyle='dashed'
    ),
    patches.Ellipse(
        (2.2, 0.1), 1, 1, fill=False,
        linestyle='dashdot'
    ),
    patches.Ellipse(
        (3.3, 0.1), 1, 1, fill=False,
        linestyle='dotted'
    ),
]:
    ax9.add_patch(p)
fig9.savefig('ellipse9.png', dpi=90, bbox_inches='tight')

fig10 = plt.figure()
ax10 = fig10.add_subplot(
    111,
    frameon=False,
    xlim=[0, 4.4],
    ylim=[0, 4.4],
    xticks=[],
    yticks=[]
)
for p in [
    patches.Ellipse(
        (0.5, 2), 1, 0.5,
        angle=0.0   # Default
    ),
    patches.Ellipse(
        (1.6, 2), 1, 0.5,
        angle=20.0
    ),
    patches.Ellipse(
        (2.7, 2), 1, 0.5,
        angle=90
    ),
    patches.Ellipse(
        (3.8, 2), 1, 0.5,
        angle=120
    ),
]:
    ax10.add_patch(p)
fig10.savefig('ellipse10.png', dpi=90, bbox_inches='tight')
