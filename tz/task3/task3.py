import json
import sys

def fill_values(tests_structure, values_dict):
    """
    Рекурсивно заполняет поля 'value' в структуре tests на основе values_dict
    """
    if isinstance(tests_structure, dict):
        # Если у текущего объекта есть id, ищем для него значение в values_dict
        if 'id' in tests_structure:
            test_id = tests_structure['id']
            if test_id in values_dict:
                tests_structure['value'] = values_dict[test_id]
        
        # Рекурсивно обрабатываем вложенные структуры
        for key, value in tests_structure.items():
            if isinstance(value, (dict, list)):
                fill_values(value, values_dict)
    
    elif isinstance(tests_structure, list):
        # Обрабатываем каждый элемент списка
        for item in tests_structure:
            fill_values(item, values_dict)

def main():
    if len(sys.argv) != 4:
        print("Использование: python program.py <values.json> <tests.json> <report.json>")
        sys.exit(1)
    
    values_file, tests_file, report_file = sys.argv[1], sys.argv[2], sys.argv[3]
    
    try:
        # Чтение values.json
        with open(values_file, 'r', encoding='utf-8') as f:
            values_data = json.load(f)
        
        # Преобразование values в словарь для быстрого поиска по id
        values_dict = {}
        for item in values_data:
            if 'id' in item and 'value' in item:
                values_dict[item['id']] = item['value']
        
        # Чтение tests.json
        with open(tests_file, 'r', encoding='utf-8') as f:
            tests_data = json.load(f)
        
        # Создаем копию структуры tests для заполнения
        report_data = json.loads(json.dumps(tests_data))  # Глубокая копия
        
        # Заполняем значения в структуре отчета
        fill_values(report_data, values_dict)
        
        # Запись результата в report.json
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, ensure_ascii=False, indent=2)
        
        print(f"Отчет успешно создан: {report_file}")
        
    except FileNotFoundError as e:
        print(f"Ошибка: Файл не найден - {e.filename}")
    except json.JSONDecodeError as e:
        print(f"Ошибка: Неверный формат JSON - {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()