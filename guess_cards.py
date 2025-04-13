import streamlit as st
from PIL import Image
import os

# Сначала вызываем set_page_config - это должна быть первая команда Streamlit
st.set_page_config(layout="wide")

# Добавляем CSS для центрирования и стилизации
st.markdown("""
<style>
    .centered-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin: 0 auto;
    }
    .letter-input {
        text-align: center;
        font-size: 20px !important;
        width: 40px !important;
        padding: 5px !important;
    }
    div[data-testid="column"] {
        padding: 0 5px !important;
    }
    div[data-testid="stVerticalBlock"] {
        gap: 10px !important;
    }
</style>
""", unsafe_allow_html=True)

# Создаем контейнер для центрирования всего содержимого
left, center, right = st.columns([1, 2, 1])

with center:
    # Загрузка изображения
    image_path = 'cards/абрикос.png'
    image = Image.open(image_path)

    # Получаем оригинальные размеры
    width, height = image.size

    # Максимальная высота, которую вы хотите установить
    max_height = 400  # в пикселях

    # Если изображение выше максимальной высоты, изменяем его размер
    if height > max_height:
        # Вычисляем новую ширину, сохраняя соотношение сторон
        new_width = int(width * (max_height / height))
        # Изменяем размер изображения
        image = image.resize((new_width, max_height))

    # Отображаем изображение по центру
    st.image(image, use_container_width=False)

    # Получаем название файла без расширения (это будет слово-ответ)
    image_name = os.path.basename(image_path).split('.')[0]
    word_length = len(image_name)

    # Создаем контейнер для полей ввода
    st.markdown('<div class="centered-container">', unsafe_allow_html=True)
    
    # Создаем колонки для полей ввода букв - по одной колонке на каждую букву
    letter_cols = st.columns(word_length)

    # Создаем поля ввода для каждой буквы
    user_input = []
    for i, col in enumerate(letter_cols):
        with col:
            # Создаем уникальный ключ для каждого поля ввода
            letter = st.text_input(
                "",  # Без метки
                key=f"letter_{i}",
                max_chars=1,  # Ограничиваем ввод одним символом
                placeholder="_",
                label_visibility="collapsed"  # Полностью скрываем метку
            )
            user_input.append(letter)

    st.markdown('</div>', unsafe_allow_html=True)

    # Объединяем введенные буквы в слово
    user_word = ''.join(user_input)

    # Проверяем, правильно ли угадано слово
    if user_word and user_word.lower() == image_name.lower():
        st.success(f"Правильно! Это {image_name}!")
    elif user_word and len(user_word) == word_length:
        st.error("Неправильно. Попробуйте еще раз!")