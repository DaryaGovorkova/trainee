import pytest
from tasks.task2 import longest_increasing_streak

@pytest.fixture
def mixed_data():
    return [10, 5, 1, 2, 3, 8, 6, 7]


@pytest.mark.parametrize(
    "input_list, expected_output",
    [
        # Тест на пустой список
        ([], {'length': 0, 'streak': []}),
        # Тест на один элемент
        ([42], {'length': 0, 'streak': []}),
        # Тест на одинаковые элементы
        ([5, 5, 5, 5], {'length': 0, 'streak': []}),
        # Тест на убывающую последовательность
        ([9, 8, 7, 6, 5], {'length': 0, 'streak': []}),
        # Тест на строго возрастающую последовательность
        ([1, 2, 3, 4, 5], {'length': 5, 'streak': [1, 2, 3, 4, 5]}),
        # Тест со смешанными данными (одна длинная последовательность)
        ([10, 1, 2, 3, 8, 6, 7], {'length': 4, 'streak': [1, 2, 3, 8]}),
        # Тест с несколькими равными по длине последовательностями
        ([1, 2, 3, 2, 7, 4, 5, 6, 3], {'length': 3, 'streak': [1, 2, 3]}), # Проверяет, что берется первая
    ]
)
def test_various_scenarios(input_list, expected_output):
    """
    Параметризованный тест проверяет функцию с различными наборами данных для покрытия основных логических веток.
    """

    result = longest_increasing_streak(input_list)
    assert result == expected_output


def test_with_fixture(mixed_data):

    result = longest_increasing_streak(mixed_data)
    assert result == {'length': 4, 'streak': [1, 2, 3, 8]}


