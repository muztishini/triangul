from scipy.spatial import Delaunay
import numpy as np


def delaunay_triangulation(points):
	triangulation = Delaunay(points)
	return triangulation.simplices


def read_points(file_path):
	with open(file_path, 'r') as file:
		pts = [tuple(map(float, point.split(','))) for line in file for point in line.strip().split(';')]
	return pts


file_path = "ishod/size_2_2.txt"
points = read_points(file_path)
# Создаем набор точек
# points = np.array([[0, 0], [0, 1], [1, 0.5], [1, 1]])

# print(points)


# print(points)
# Вызываем функцию
result = delaunay_triangulation(points)

print(result)
