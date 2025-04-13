import streamlit as st
from PIL import Image
import os

# Сначала вызываем set_page_config - это должна быть первая команда Streamlit
st.set_page_config(layout="wide")

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

# Отображаем изображение
st.image(image, use_container_width=False)

# Получаем название файла без расширения (это будет слово-ответ)
image_name = os.path.basename(image_path).split('.')[0]
word_length = len(image_name)

# Отображение изображения по ширине контейнера
#st.image(image, use_container_width=True)

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
            placeholder="_"
        )
        user_input.append(letter)

# Объединяем введенные буквы в слово
user_word = ''.join(user_input)

# Проверяем, правильно ли угадано слово
if user_word and user_word.lower() == image_name.lower():
    st.success(f"Правильно! Это {image_name}!")
elif user_word and len(user_word) == word_length:
    st.error("Неправильно. Попробуйте еще раз!")