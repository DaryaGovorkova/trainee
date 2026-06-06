import pytest
from tasks.task1 import process_grades

@pytest.fixture
def mixed_records():
    return [
        "Иванов: 85",  # Корректный формат
        "Иванова: 65",  # Корректный формат
        "Петров: 92",  # Корректный формат
        "Сидорова: 59",  # Корректный формат

        "Смирнов: 101",  # БИТАЯ: Оценка вне диапазона (больше 100)
        "Волкова: -10",  # БИТАЯ: Оценка вне диапазона (меньше 0)

        "Кузнецов 88",  # БИТАЯ: Нет двоеточия
        "Попова: ",  # БИТАЯ: Оценка отсутствует (пустая строка)
        ": 65",  # БИТАЯ: Фамилия отсутствует

        "Лебедева: пять",  # БИТАЯ: Оценка не является числом
        "Соловьев: 99.5",  # БИТАЯ: Оценка не целое число

        "   Соколов: 77",  # Корректный, но с лишним пробелом в начале
        "Новикова:100",  # Корректный, но без пробела после двоеточия

        "",  # БИТАЯ: Пустая строка
        "   "  # БИТАЯ: Строка только из пробелов
    ]


@pytest.fixture
def duplicate_records():
    return [
        "Иванов: 70",
        "Петров: 50",
        "Иванов: 80", # Дубликат фамилии
        "Смирнов: 60"
    ]

@pytest.mark.parametrize("records, expected", [
    ([], {"valid_count": 0, "average": 0.0, "passed": [], "skipped": 0}),
    (["Студент: 100"], {"valid_count": 1, "average": 100.0, "passed": ["Студент"], "skipped": 0}),
    (["Студент: 59"], {"valid_count": 1, "average": 59.0, "passed": [], "skipped": 0}),

])
def test_edge_cases(records, expected):
    assert process_grades(records) == expected


def test_with_fixture(mixed_records):
    result = process_grades(mixed_records)
    assert result == {
        "valid_count": 6,
        "average": 79.7,
        "passed": ['Иванов', 'Иванова', 'Новикова', 'Петров', 'Соколов'],
        "skipped": 9
    }

def test_duplicate_names(duplicate_records):
    result = process_grades(duplicate_records)
    assert result["passed"] == ["Иванов", "Смирнов"] # Иванов должен быть один раз
    assert result["valid_count"] == 4
    assert result["average"] == 65.0



