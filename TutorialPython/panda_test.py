def annot_max(x, y, ax=None):
    maxIxVal = np.argmax(y)
    zeroBasedIx = np.argwhere(y.index == maxIxVal).flatten()[0]
    xmax = x[zeroBasedIx]
    ymax = y.max()
    text = "k={:d}, measure={:.3f}".format(xmax, ymax)
    if not ax:
        ax = plt.gca()
    bbox_props = dict(boxstyle="round,pad=0.3", fc="w", ec="k", lw=0.72)
    arrowprops = dict(arrowstyle="-", connectionstyle="arc3,rad=0.1")
    kw = dict(xycoords='data', textcoords="axes fraction",
              arrowprops=arrowprops, bbox=bbox_props, ha="right", va="top")
    ax.annotate(text, xy=(xmax, ymax), xytext=(0.94, 0.90), **kw)


def annot_min(x, y, ax=None):
    minIxVal = np.argmin(y)
    zeroBasedIx = np.argwhere(y.index == minIxVal).flatten()[0]
    xmin = x[zeroBasedIx]
    ymin = y.min()
    text = "k={:d}, measure={:.3f}".format(xmin, ymin)
    if not ax:
        ax = plt.gca()
    bbox_props = dict(boxstyle="round,pad=0.3", fc="w", ec="k", lw=0.72)
    arrowprops = dict(arrowstyle="-", connectionstyle="arc3,rad=0.1")
    kw = dict(xycoords='data', textcoords="axes fraction",
              arrowprops=arrowprops, bbox=bbox_props, ha="right", va="top")
    ax.annotate(text, xy=(xmin, ymin), xytext=(0.94, 0.90), **kw)


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 8, num=301)
y = np.sinc((x - 2.21) * 3)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_ylim(-0.3, 1.5)
annot_max(x, y)


plt.show()
