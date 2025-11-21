import sys

def main():
    if len(sys.argv) < 2:
        print("Укажите имя файла в аргументе командной строки")
        return

    filename = sys.argv[1]
    
    try:
        with open(filename, 'r') as f:
            data = f.read().split()
        
        if not data:
            print("Файл пуст")
            return
            
        nums = [int(x) for x in data]
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
        return
    except ValueError:
        print("Ошибка: в файле должны быть только целые числа")
        return

    # Сортируем массив
    nums.sort()
    n = len(nums)
    
    # Находим медиану
    if n % 2 == 1:
        median = nums[n//2]
    else:
        median = nums[n//2 - 1]  # Можно выбрать любое из двух средних
    
    # Считаем необходимое количество ходов
    moves = sum(abs(x - median) for x in nums)
    
    if moves <= 20:
        print(moves)
    else:
        print("20 ходов недостаточно для приведения всех элементов массива к одному числу")

if __name__ == "__main__":
    main()