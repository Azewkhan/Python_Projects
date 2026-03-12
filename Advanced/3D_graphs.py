import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(12,10))  # optional, makes figure bigger

# ---------------- 3D line + scatter ----------------
ax = fig.add_subplot(221, projection='3d')

# 3D line
z = np.linspace(0, 15, 1000)
x = np.sin(z)
y = np.cos(z)
ax.plot3D(x, y, z, 'grey')

# 3D scatter
z_points = 15 * np.random.random(100)
x_points = np.sin(z_points) + 0.1 * np.random.randn(100)
y_points = np.cos(z_points) + 0.1 * np.random.randn(100)
ax.scatter3D(x_points, y_points, z_points, c=z_points, cmap='Greens')
ax.set_title('Line + Scatter')

# ---------------- 3D Contour ----------------
def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

ax = fig.add_subplot(222, projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Contour')

# ---------------- Wireframe ----------------
ax = fig.add_subplot(223, projection='3d')
ax.plot_wireframe(X, Y, Z, color='black')
ax.set_title('Wireframe')

# ---------------- Surface ----------------
ax = fig.add_subplot(224, projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
ax.set_title('Surface')

plt.tight_layout()  # optional: avoids overlap
plt.show()          # one final show