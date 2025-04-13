import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

# Загрузка изображения
image = Image.open('cards/абрикос.png')

# Создание колонок для центрирования изображения
col1, col2, col3 = st.columns([1, 2, 1])  # Соотношение ширины колонок

# Отображение изображения в средней колонке
with col2:
    st.image(image, use_container_width=True)