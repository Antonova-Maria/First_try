import streamlit as st
from PIL import Image
image = Image.open('cards/абрикос.png') 
st.image(image)