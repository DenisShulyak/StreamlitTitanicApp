import pandas as pd
import pytest
from main import calculate_statistics, create_result_table

# Тестовые данные
def create_test_data():
    return pd.DataFrame({
        'Embarked': ['C', 'Q', 'S', 'C', 'S'],
        'Fare': [100.0, 50.0, 75.0, 150.0, 25.0]
    })

# Тест 1: Проверка расчета средней стоимости
def test_calculate_mean():
    """Тест расчета средней стоимости билетов"""
    test_data = create_test_data()

    result = calculate_statistics(test_data, "Средняя стоимость")

    # Проверяем, что результат - это pandas Series
    assert isinstance(result, pd.Series)

    # Проверяем правильность расчетов
    assert result['C'] == 125.0  # (100 + 150) / 2
    assert result['Q'] == 50.0  # 50 / 1
    assert result['S'] == 50.0  # (75 + 25) / 2


# Тест 2: Проверка создания таблицы с результатами
def test_create_result_table():
    """Тест создания итоговой таблицы"""
    test_data = create_test_data()
    result = calculate_statistics(test_data, "Средняя стоимость")

    table = create_result_table(result)

    # Проверяем структуру таблицы
    assert isinstance(table, pd.DataFrame)
    assert list(table.columns) == ['Пункт посадки', 'Стоимость билета ($)']
    assert len(table) == 3  # Три пункта посадки

    # Проверяем, что названия пунктов правильно преобразованы
    embark_points = table['Пункт посадки'].tolist()
    assert 'Шербур (C)' in embark_points
    assert 'Квинстаун (Q)' in embark_points
    assert 'Саутгемптон (S)' in embark_points


# Тест 3: Проверка всех типов статистик
def test_all_statistic_types():
    """Тест всех трех типов статистик"""
    test_data = create_test_data()

    # Тестируем минимальную стоимость
    min_result = calculate_statistics(test_data, "Минимальная стоимость")
    assert min_result['C'] == 100.0
    assert min_result['Q'] == 50.0
    assert min_result['S'] == 25.0

    # Тестируем максимальную стоимость
    max_result = calculate_statistics(test_data, "Максимальная стоимость")
    assert max_result['C'] == 150.0
    assert max_result['Q'] == 50.0
    assert max_result['S'] == 75.0

    # Тестируем среднюю стоимость
    mean_result = calculate_statistics(test_data, "Средняя стоимость")
    assert mean_result['C'] == 125.0
    assert mean_result['Q'] == 50.0
    assert mean_result['S'] == 50.0