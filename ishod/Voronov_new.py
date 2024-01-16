import numpy as np

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else -1

def in_circle(a, b, c, d):
    ax, ay = a
    bx, by = b
    cx, cy = c
    dx, dy = d

    matrix = [
        [ax - dx, ay - dy, (ax - dx)**2 + (ay - dy)**2],
        [bx - dx, by - dy, (bx - dx)**2 + (by - dy)**2],
        [cx - dx, cy - dy, (cx - dx)**2 + (cy - dy)**2]
    ]

    det = (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -
        matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
        matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )

    return det < 0

def delaunay_triangulation(points):
    n = len(points)
    if n < 3:
        raise ValueError("Необходимо минимум 3 точки для триангуляции.")
        
    super_triangle = [(sum(p[0] for p in points) / n, sum(p[1] for p in points) / n + 10 * max(p[1] for p in points))]
    super_triangle.extend(points)
    triangles = [tuple(i for i, _ in enumerate(super_triangle))]
    
    for i, point in enumerate(points):
        edges = []
        for triangle in triangles:
            a, b, c = triangle[:3] 
            if orientation(points[a], points[b], point) != -1 and \
               orientation(points[b], points[c], point) != -1 and \
               orientation(points[c], points[a], point) != -1:
                edges.extend([(a, b), (b, c), (c, a)])
                triangles.remove(triangle)
        for edge in edges:
            if edges.count(edge) == 1:
                triangles.append((edge[0], edge[1], i))
                
    triangles = [triangle for triangle in triangles if not any(vertex in triangle for vertex in super_triangle[0])]
    
    return triangles

def point(points, triangles):
    for i, point in enumerate(points):
        print(f"Point {i+1}: {point}")
        # print(triangles)

def read_points(file_path):
    with open(file_path, 'r') as file:
        points = [tuple(map(float, point.split(','))) for line in file for point in line.strip().split(';')]
    return points

if __name__ == "__main__":
    file_path = "/home/kroshakov/Python/triangul/ishod/size_2_2.txt"
    points = read_points(file_path)

    points = [list(p) for p in points]

    triangles = delaunay_triangulation(points)
    point(points, triangles)
