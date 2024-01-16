import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt


# Создание списка точек
def read_points(file_path):
	with open(file_path, 'r') as file:
		pts = [tuple(map(float, point.split(','))) for line in file for point in line.strip().split(';')]
	return pts


file_path = "ishod/size_2_2.txt"
points = read_points(file_path)
points = np.array(points)

# Создание объекта класса Delaunay
tri = Delaunay(points)

# Получение треугольников
triangles = points[tri.simplices]

# Вывод результатов
print(tri.simplices)
print(triangles)

# Визуализация результата
plt.triplot(points[:, 0], points[:, 1], tri.simplices)
plt.plot(points[:, 0], points[:, 1], 'o')
plt.show()
