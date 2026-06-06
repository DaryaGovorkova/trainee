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