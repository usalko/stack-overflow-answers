# https://stackoverflow.com/questions/68428544/representation-of-a-triangulation-by-different-data-structures
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay

points = np.array([[0.2, 0], [0.1, 1.1], [0.6, 0.1], [1, 0.5], [0.6,0.9], [0.4,0.4]])
tri = Delaunay(points)

#plot
plt.triplot(points[:,0], points[:,1], tri.simplices)
plt.plot(points[:,0], points[:,1], 'o')
plt.show()

print(tri.points)
"""
[[0.2 0. ]
[0.  1.1]
[0.6 0. ]
[1.  1. ]
[0.2 0.8]
[0.4 0.4]]
"""
print(tri.simplices)
"""
[[0 5 1]
[5 4 1]
[4 5 3]
[5 2 3]
[2 5 0]]
"""

# Response:
# Sorry for my five cents, but if you think about memory optimization. Perhaps this library https://github.com/nschloe/meshio brings more ideas.
