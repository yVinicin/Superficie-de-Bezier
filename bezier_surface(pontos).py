import numpy as np
import matplotlib.pyplot as plt

# Função para vetor T(t)
def T(t):
    return np.array([t**3, t**2, t, 1])

# Matriz base de Bézier
matriz_bezier = np.array([
    [-1, 3, -3, 1],
    [3, -6, 3, 0],
    [-3, 3, 0, 0],
    [1, 0, 0, 0]
])

# Pontos de controle (4x4x3)
elementos_geometria = np.array([
    [[0, 1, 10], [2, 0, -8], [4, 0, -1], [6, 2, 0]],
    [[0, 3, -1], [2, 4, 3], [4, 4, 0], [6, 4, 1]],
    [[0, 5, 0], [2, 8, -1], [4, 8, -2], [6, 6, 0]],
    [[0, 7, 10], [2, 12, -6], [4, 12, -3], [8, 8, -2]],
])

# Resolução
step = 0.025
res = int(1 / step)
u = np.linspace(0, 1, res)
v = np.linspace(0, 1, res)

# Lista para armazenar os pontos
pontos_x, pontos_y, pontos_z = [], [], []

for uu in u:
    for vv in v:
        Tu = T(uu)
        Tv = T(vv)
        ponto = np.zeros(3)
        for coord in range(3):
            G_coord = elementos_geometria[:, :, coord]
            ponto[coord] = Tu @ matriz_bezier @ G_coord @ matriz_bezier.T @ Tv.T
        pontos_x.append(ponto[0])
        pontos_y.append(ponto[1])
        pontos_z.append(ponto[2])

# Plot 3D apenas com pontos
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(pontos_x, pontos_y, pontos_z, color='blue', s=5, label='Pontos da superfície')

# Pontos de controle em vermelho
for i in range(4):
    for j in range(4):
        x, y, z = elementos_geometria[i, j]
        ax.scatter(x, y, z, color='red', s=15)

ax.set_title('Superfície de Bézier (pontos)')
ax.legend()
plt.show()
