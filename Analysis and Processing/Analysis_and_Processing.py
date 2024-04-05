import numpy as np
import time

# ���������� �����
points = 1000

# ������� ��� ���������� ���������� ����� ����� ������� � ���������� �����������
def cartesian_distance(point1, point2):
    return np.sqrt(np.sum((np.array(point1) - np.array(point2))**2))

# ������� ��� ���������� ���������� ����� ����� ������� � �������� �����������
def polar_distance(point1, point2):
    return abs(point1[0] - point2[0])

# ������� ��� ���������� ���������� ����� ����� ������� � ����������� �����������
def spherical_distance(point1, point2):
    return np.sqrt(np.sum((np.array(point1) - np.array(point2))**2))



# ������� ��� �������������� ���������� ��������� � ��������
def cartesian_to_polar(point):
    x, y = point
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    return r, theta

# ������� ��� �������������� �������� ��������� � ����������
def polar_to_cartesian(r, theta):
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

# ������� ��� �������������� ���������� ��������� � �����������
def cartesian_to_spherical(point):
    x, y, z = point
    r = np.sqrt(x**2 + y**2 + z**2)
    theta = np.arccos(z / r)
    phi = np.arctan2(y, x)
    return r, theta, phi

# ������� ��� �������������� ����������� ��������� � ����������
def spherical_to_cartesian(r, theta, phi):
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
    return x, y, z

# ������� ��� ��������� ������� ���������� �������������� ��������� � ���������� ����������
def compare_computation_times(points, coordinate_system_function, distance_function):
    start_time = time.time()
    converted_points = [coordinate_system_function(point) for point in points]
    conversion_time = time.time() - start_time

    start_time = time.time()
    distances = [distance_function(point1, point2) for point1 in converted_points for point2 in converted_points]
    distance_calculation_time = time.time() - start_time

    return conversion_time, distance_calculation_time

# ��������� ��������� ����� � 2D ���������� �����������
points_2d = np.random.rand(points, 2) * 10 - 5

# �������������� � �������� ���������� � �������
converted_points_2d = [cartesian_to_polar(point) for point in points_2d]
converted_back_points_2d = [polar_to_cartesian(r, theta) for r, theta in converted_points_2d]

# ������ ���������� � ��������� �������� ���������
cartesian_distances_2d = compare_computation_times(points_2d, lambda x: x, cartesian_distance)
polar_distances_2d = compare_computation_times(points_2d, cartesian_to_polar, polar_distance)

# ����� ����������� ��� 2D ���������
print("2D Cartesian Coordinates:")
print("Original Points:\n", np.round(points_2d))
print("Converted to Polar Coordinates:\n", np.round(converted_points_2d, decimals=2))
print("Converted Back to Cartesian Coordinates:\n", np.round(converted_back_points_2d))
print("Cartesian Distances Time:", cartesian_distances_2d[1])
print("Polar Distances Time:", polar_distances_2d[1])
print("\n")

# ��������� ��������� ����� � 3D ���������� �����������
points_3d = np.random.rand(points, 3) * 10 - 5

# �������������� � ����������� ���������� � �������
converted_points_3d = [cartesian_to_spherical(point) for point in points_3d]
converted_back_points_3d = [spherical_to_cartesian(r, theta, phi) for r, theta, phi in converted_points_3d]

# ������ ���������� � ��������� �������� ���������
cartesian_distances_3d = compare_computation_times(points_3d, lambda x: x, cartesian_distance)
spherical_distances_3d = compare_computation_times(points_3d, cartesian_to_spherical, spherical_distance)

# ����� ����������� ��� 3D ���������
print("3D Cartesian Coordinates:")
print("Original Points:\n", np.round(points_3d))
print("Converted to Spherical Coordinates:\n", np.round(converted_points_3d, decimals=2))
print("Converted Back to Cartesian Coordinates:\n", np.round(converted_back_points_3d))
print("Cartesian Distances Time:", cartesian_distances_3d[1])
print("Spherical Distances Time:", spherical_distances_3d[1])

