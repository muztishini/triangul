import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt


# Создание набора точек
def read_points(file_path):
	with open(file_path, 'r') as file:
		pts = [tuple(map(float, point.split(','))) for line in file for point in line.strip().split(';')]
	return pts


file_path = "ishod/size_2_2.txt"
points = read_points(file_path)
points = np.array(points)

# Выполнение построения диаграммы Вороного
vor = Voronoi(points)

# Построение диаграммы Вороного
fig = voronoi_plot_2d(vor)

# Отображение графика
plt.show()
