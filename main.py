import streamlit as st
import pandas as pd

def calculate_statistics(data, statistic_choice):
    """Вычисление статистики по стоимости билетов"""
    if statistic_choice == "Средняя стоимость":
        return data.groupby('Embarked')['Fare'].mean().round(2)
    elif statistic_choice == "Минимальная стоимость":
        return data.groupby('Embarked')['Fare'].min().round(2)
    else:  # Максимальная стоимость
        return data.groupby('Embarked')['Fare'].max().round(2)


def create_result_table(result):
    """Создание итоговой таблицы с форматированием"""
    embark_mapping = {
        'C': 'Шербур (C)',
        'Q': 'Квинстаун (Q)',
        'S': 'Саутгемптон (S)'
    }

    return pd.DataFrame({
        'Пункт посадки': [embark_mapping.get(emb, emb) for emb in result.index],
        'Стоимость билета ($)': result.values
    })


def main():
    st.set_page_config(page_title="Данные пассажиров Титаника", layout="centered")

    # 1) Картинка Титаника
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/RMS_Titanic_3.jpg/800px-RMS_Titanic_3.jpg",
             caption="RMS Титаник",
             use_column_width=True)

    # 2) Хидер "Данные пассажиров Титаника"
    st.title("Данные пассажиров Титаника")

    # 3) Описание выбора
    st.markdown("""
    **Вычислить среднюю, минимальную или максимальную стоимость билета 
    у пассажиров по каждому пункту посадки.**
    """)

    # Загрузка данных
    data = pd.read_csv('titanic_train.csv')

    if data is None:
        st.error("Не удалось загрузить данные")
        return

    # 4) Выбор значения поля (мин/средн/макс)
    statistic_choice = st.selectbox(
        "Выберите тип стоимости билета:",
        ["Средняя стоимость", "Минимальная стоимость", "Максимальная стоимость"]
    )

    # Расчет выбранной статистики
    result = calculate_statistics(data, statistic_choice)

    # Создание таблицы с результатами
    result_table = create_result_table(result)

    # Отображение таблицы
    st.markdown(f"**{statistic_choice} по пунктам посадки:**")
    st.dataframe(result_table, width=600)

if __name__ == "__main__":
    main()