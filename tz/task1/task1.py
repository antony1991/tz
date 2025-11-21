def calculate_detailed_path(n, m):
    path = []
    intervals = []
    current = 1
    step = 1
    
    print(f"\n--- Обработка массива n={n}, m={m} ---")
    print(f"Круговой массив: {''.join(str(i) for i in range(1, n+1))}")
    print(f"Длина массива: {n}")
    print(f"Длина интервала: {m}")
    print("\nФормируемые интервалы:")
    
    while True:
        # Формируем текущий интервал
        interval = []
        temp = current
        for i in range(m):
            interval.append(str(temp))
            temp = temp % n + 1  # Переход к следующему элементу с учетом круговости
        
        interval_str = ''.join(interval)
        intervals.append(interval_str)
        path.append(str(current))
        
        print(f"  Шаг {step}: интервал {interval_str}, начальный элемент: {current}")
        
        # Вычисляем следующий начальный элемент
        next_start = (current + m - 1) % n
        if next_start == 0:
            next_start = n
        
        current = next_start
        step += 1
        
        # Условие завершения - вернулись к первому элементу
        if current == 1:
            break
    
    path_str = ''.join(path)
    print(f"Полученный путь: {path_str}")
    print(f"Длина пути: {len(path_str)}")
    
    return path_str

def main():
    print("=" * 50)
    print("ПРОГРАММА ДЛЯ РАБОТЫ С КРУГОВЫМИ МАССИВАМИ")
    print("=" * 50)
    
    # Ввод параметров для первого массива
    print("\n--- Параметры первого массива ---")
    n1 = int(input("Введите n для первого массива: "))
    m1 = int(input("Введите m для первого массива: "))
    
    # Ввод параметров для второго массива
    print("\n--- Параметры второго массива ---")
    n2 = int(input("Введите n для второго массива: "))
    m2 = int(input("Введите m для второго массива: "))
    
    # Обработка первого массива
    path1 = calculate_detailed_path(n1, m1)
    
    # Обработка второго массива
    path2 = calculate_detailed_path(n2, m2)
    
    # Объединение результатов
    final_result = path1 + path2
    
    print("\n" + "=" * 50)
    print("ИТОГОВЫЙ РЕЗУЛЬТАТ")
    print("=" * 50)
    print(f"Путь из первого массива: {path1}")
    print(f"Путь из второго массива: {path2}")
    print(f"Объединенный путь: {final_result}")
    print(f"Общая длина финального пути: {len(final_result)}")

if __name__ == "__main__":
    main()