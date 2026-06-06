import bisect
from statistics import mean


def process_grades(records: list[str]) -> dict:

    valid_count = 0     # количество успешно распарсенных записей
    grades = []         # список оценок
    passed = []         # фамилии тех, у кого оценка >= 60 (по алфавиту)
    skipped = 0         # количество строк, которые не удалось обработать

    for record in records:
        try:
            # Разделение строки на фамилию и оценку
            last_name, grade_str = record.split(":", 1)
            last_name_clean = last_name.strip()
            grade = int(grade_str.strip())

            if not last_name_clean:
                raise ValueError("Фамилия отсутствует")

            # Проверка диапазона оценки
            if not (0 <= grade <= 100):
                raise ValueError("Оценка вне диапазона")

            if grade >= 60:
                insert_pos = bisect.bisect_left(passed, last_name_clean)
                # Проверка на повтор фамилии в списке
                if not (insert_pos < len(passed) and passed[insert_pos] == last_name_clean):
                    passed.insert(insert_pos, last_name_clean)

            valid_count += 1
            grades.append(grade)

        except (ValueError, IndexError):
            skipped += 1


    average = round(float(mean(grades)), 1) if grades else 0.0
    return {
        "valid_count": valid_count,
        "average": average,
        "passed": passed,
        "skipped": skipped
    }


students_grades = [
    "Иванов: 85",        # Корректный формат
    "Иванова: 65",       # Корректный формат
    "Петров: 92",        # Корректный формат
    "Сидорова: 59",      # Корректный формат
    "Петров: 62",        # Корректный формат

    "Смирнов: 101",      # ОШИБКА: Оценка вне диапазона (больше 100)
    "Волкова: -10",      # ОШИБКА: Оценка вне диапазона (меньше 0)

    "Кузнецов 88",       # ОШИБКА: Нет двоеточия
    "Попова: ",          # ОШИБКА: Оценка отсутствует (пустая строка)
    ": 65",              # ОШИБКА: Фамилия отсутствует

    "Лебедева: пять",    # ОШИБКА: Оценка не является числом
    "Соловьев: 99.5",    # ОШИБКА: Оценка не целое число (если по ТЗ нужны только int)

    "   Соколов: 77",    # Корректный, но с лишним пробелом в начале
    "Новикова:100",      # Корректный, но без пробела после двоеточия

    "",                  # ОШИБКА: Пустая строка
    "   "                # ОШИБКА: Строка только из пробелов
]

print(process_grades(students_grades))



data = [

"Иванов: 78",

"Петров: 79",

"Сидоров: abc", # битая

"Козлов: 90",

": 55", # битая

"Иванов: 100" # повтор (считаем как отдельную запись)

]

print(process_grades(data))

# В данном примере ошибка значения "average": 61.8, должно быть равным 71.8