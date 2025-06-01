import matplotlib.pyplot as plt
import numpy as np

# Координати квадрату ABCD
A = np.array([0, 0, 0])
B = np.array([4, 0, 0])
C = np.array([4, 4, 0])
D = np.array([0, 4, 0])

# Точка K — не в площині квадрата (вгору по z)
K = np.array([2, 4, 3])

# Середина DK
M = (D + K) / 2

# Точка N на BC (для прикладу — посередині)
N = np.array([4, 2, 0])

# Побудова
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Квадрат ABCD
square_points = np.array([A, B, C, D, A])
ax.plot(square_points[:,0], square_points[:,1], square_points[:,2], 'k-', label='Квадрат ABCD')

# Трикутник DKC
triangle_points = np.array([D, K, C, D])
ax.plot(triangle_points[:,0], triangle_points[:,1], triangle_points[:,2], 'g-', label='Трикутник DKC')

# Відрізки DK і MN
ax.plot([D[0], K[0]], [D[1], K[1]], [D[2], K[2]], 'g--', label='DK')
ax.plot([M[0], N[0]], [M[1], N[1]], [M[2], N[2]], 'r-', linewidth=2, label='MN')

# Позначення точок
points = {'A': A, 'B': B, 'C': C, 'D': D, 'K': K, 'M': M, 'N': N}
for name, coord in points.items():
    ax.text(coord[0], coord[1], coord[2]+0.2, name, fontsize=12)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Просторова модель: квадрат ABCD і трикутник DKC')
ax.legend()
plt.tight_layout()
plt.show()