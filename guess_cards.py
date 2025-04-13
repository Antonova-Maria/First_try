import streamlit as st
from PIL import Image

# Сначала вызываем set_page_config - это должна быть первая команда Streamlit
st.set_page_config(layout="wide")

# Загрузка изображения
image = Image.open('cards/абрикос.png')

# Автоматическое масштабирование по ширине контейнера
st.image(image, use_container_width=True)

# Получаем оригинальные размеры
width, height = image.size
aspect_ratio = width / height

# Слайдер для изменения ширины
image_width = st.slider("Выберите ширину изображения (пиксели)", 
                        min_value=100, 
                        max_value=1000, 
                        value=width if width < 1000 else 1000,
                        step=50)

# Отображение изображения с выбранной шириной
st.image(image, width=image_width)

# Показываем информацию о размерах
st.write(f"Оригинальный размер: {width}x{height} пикселей")
st.write(f"Текущий размер: {image_width}x{int(image_width/aspect_ratio)} пикселей")