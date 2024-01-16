from scipy.spatial import Delaunay
import matplotlib.pyplot as plt
import numpy as np


# Создание набора точек
def read_points(file_path):
	with open(file_path, 'r') as file:
		pts = [tuple(map(float, point.split(','))) for line in file for point in line.strip().split(';')]
	return pts


file_path = "ishod/size_2_2.txt"
points = read_points(file_path)
points = np.array(points)

# Выполнение триангуляции Делоне
tri = Delaunay(points)

# Построение графика триангуляции
plt.triplot(points[:, 0], points[:, 1], tri.simplices)
plt.plot(points[:, 0], points[:, 1], 'o')
plt.show()
