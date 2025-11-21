import sys

def read_ellipse_params(file_path):
    """Читает параметры эллипса из файла"""
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Читаем координаты центра (первая строка)
    center_line = lines[0].strip().split()
    h = float(center_line[0])
    k = float(center_line[1])
    
    # Читаем радиусы (вторая строка)
    radius_line = lines[1].strip().split()
    a = float(radius_line[0])  # радиус по оси X
    b = float(radius_line[1])  # радиус по оси Y
    
    return h, k, a, b

def read_points(file_path):
    """Читает координаты точек из файла"""
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    points = []
    for line in lines:
        coords = line.strip().split()
        if len(coords) >= 2:
            x = float(coords[0])
            y = float(coords[1])
            points.append((x, y))
    
    return points

def check_point_position(x, y, h, k, a, b):
    """
    Определяет положение точки относительно эллипса
    Возвращает:
      0 - точка на эллипсе
      1 - точка внутри эллипса
      2 - точка снаружи эллипса
    """
    # Уравнение эллипса: ((x-h)/a)^2 + ((y-k)/b)^2 = 1
    value = ((x - h) / a) ** 2 + ((y - k) / b) ** 2
    
    # Определяем положение точки с учетом погрешности вычислений
    epsilon = 1e-10  # малая величина для учета погрешности вычислений
    
    if abs(value - 1.0) < epsilon:
        return 0  # на эллипсе
    elif value < 1.0:
        return 1  # внутри
    else:
        return 2  # снаружи

def main():
    if len(sys.argv) != 3:
        print("Использование: python program.py <файл_эллипса> <файл_точек>")
        sys.exit(1)
    
    ellipse_file = sys.argv[1]
    points_file = sys.argv[2]
    
    try:
        # Читаем параметры эллипса
        h, k, a, b = read_ellipse_params(ellipse_file)
        
        # Читаем точки
        points = read_points(points_file)
        
        print(f"Параметры эллипса:")
        print(f"  Центр: ({h}, {k})")
        print(f"  Радиусы: a={a}, b={b}")
        print(f"Количество точек для проверки: {len(points)}")
        print("\nРезультаты:")
        
        # Проверяем положение каждой точки
        for i, (x, y) in enumerate(points, 1):
            position = check_point_position(x, y, h, k, a, b)
            print(f"Точка {i} ({x}, {y}): {position}")
            
    except FileNotFoundError as e:
        print(f"Ошибка: Файл не найден - {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"Ошибка: Неверный формат данных в файле - {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()