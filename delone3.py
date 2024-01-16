import numpy as np
from scipy.spatial import Delaunay


# Создание набора точек
def read_points(file_path):
	with open(file_path, 'r') as file:
		pts = [tuple(map(float, point.split(','))) for line in file for point in line.strip().split(';')]
	return pts


file_path = "ishod/size_2_2.txt"
points = read_points(file_path)
points = np.array(points)

# Триангуляция Делоне
tri = Delaunay(points)

# Вывод треугольников
for i in range(tri.nsimplex):
	simplex = tri.simplices[i]
	print("Triangle {}: {}".format(i + 1, simplex))
