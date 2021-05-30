import numpy as np

cities = ['Barcelona', 'Berlin', 'Brussels']
dist2barcelona = [0, 1498, 1063, 1455]
dists = np.array(dist2barcelona[:3])
print(dists, '\n')
print(np.abs(dists - dists[:, np.newaxis]))
