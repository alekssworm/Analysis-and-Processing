import numpy as np
import time

# Количество точек
points = 1000

# Функция для вычисления расстояния между двумя точками в декартовых координатах
def cartesian_distance(point1, point2):
    return np.sqrt(np.sum((np.array(point1) - np.array(point2))**2))

# Функция для вычисления расстояния между двумя точками в полярных координатах
def polar_distance(point1, point2):
    return abs(point1[0] - point2[0])

# Функция для вычисления расстояния между двумя точками в сферических координатах
def spherical_distance(point1, point2):
    return np.sqrt(np.sum((np.array(point1) - np.array(point2))**2))



# Функция для преобразования декартовых координат в полярные
def cartesian_to_polar(point):
    x, y = point
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    return r, theta

# Функция для преобразования полярных координат в декартовые
def polar_to_cartesian(r, theta):
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

# Функция для преобразования декартовых координат в сферические
def cartesian_to_spherical(point):
    x, y, z = point
    r = np.sqrt(x**2 + y**2 + z**2)
    theta = np.arccos(z / r)
    phi = np.arctan2(y, x)
    return r, theta, phi

# Функция для преобразования сферических координат в декартовые
def spherical_to_cartesian(r, theta, phi):
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
    return x, y, z

# Функция для сравнения времени выполнения преобразования координат и вычисления расстояний
def compare_computation_times(points, coordinate_system_function, distance_function):
    start_time = time.time()
    converted_points = [coordinate_system_function(point) for point in points]
    conversion_time = time.time() - start_time

    start_time = time.time()
    distances = [distance_function(point1, point2) for point1 in converted_points for point2 in converted_points]
    distance_calculation_time = time.time() - start_time

    return conversion_time, distance_calculation_time

# Генерация случайных точек в 2D декартовых координатах
points_2d = np.random.rand(points, 2) * 10 - 5

# Преобразование в полярные координаты и обратно
converted_points_2d = [cartesian_to_polar(point) for point in points_2d]
converted_back_points_2d = [polar_to_cartesian(r, theta) for r, theta in converted_points_2d]

# Расчет расстояний в различных системах координат
cartesian_distances_2d = compare_computation_times(points_2d, lambda x: x, cartesian_distance)
polar_distances_2d = compare_computation_times(points_2d, cartesian_to_polar, polar_distance)

# Вывод результатов для 2D координат
print("2D Cartesian Coordinates:")
print("Original Points:\n", np.round(points_2d))
print("Converted to Polar Coordinates:\n", np.round(converted_points_2d, decimals=2))
print("Converted Back to Cartesian Coordinates:\n", np.round(converted_back_points_2d))
print("Cartesian Distances Time:", cartesian_distances_2d[1])
print("Polar Distances Time:", polar_distances_2d[1])
print("\n")

# Генерация случайных точек в 3D декартовых координатах
points_3d = np.random.rand(points, 3) * 10 - 5

# Преобразование в сферические координаты и обратно
converted_points_3d = [cartesian_to_spherical(point) for point in points_3d]
converted_back_points_3d = [spherical_to_cartesian(r, theta, phi) for r, theta, phi in converted_points_3d]

# Расчет расстояний в различных системах координат
cartesian_distances_3d = compare_computation_times(points_3d, lambda x: x, cartesian_distance)
spherical_distances_3d = compare_computation_times(points_3d, cartesian_to_spherical, spherical_distance)

# Вывод результатов для 3D координат
print("3D Cartesian Coordinates:")
print("Original Points:\n", np.round(points_3d))
print("Converted to Spherical Coordinates:\n", np.round(converted_points_3d, decimals=2))
print("Converted Back to Cartesian Coordinates:\n", np.round(converted_back_points_3d))
print("Cartesian Distances Time:", cartesian_distances_3d[1])
print("Spherical Distances Time:", spherical_distances_3d[1])

