import numpy as np
import matplotlib.pyplot as plt



X = np.linspace(-2 * np.pi, 4 * np.pi, 200, endpoint=True)
#F1 = np.sin(X ** 3 / 2)
F2 = np.sin(X**3)

fig, ax = plt.subplots()

ax.xaxis.set_major_locator(plt.MultipleLocator(np.pi / 2))
ax.set_xticklabels([r'$-2\pi$', r'$-\frac{3\pi}{2}$', r'$-\pi$',
                    r'$-\frac{\pi}{2}$', 0, r'$\frac{\pi}{2}$',
                    r'$+\pi$', r'$\frac{3\pi}{2}$', r'$+2\pi$'])

for xtick in ax.get_xticklabels():
    xtick.set_fontsize(18)
    xtick.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.7))

for ytick in ax.get_yticklabels():
    ytick.set_fontsize(14)
    ytick.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.7))

#ax.plot(X, F1, label="$sin(x)$")
ax.plot(X, F2, label="$sin(x)$")
ax.legend(loc='lower left')


#-------------------------------
print(ax.get_xticklabels())

for xtick in ax.get_xticklabels():
    print(xtick)

labels = [xtick.get_text() for xtick in ax.get_xticklabels()]
print(labels)
#--------------------------------
plt.show()