import streamlit as st
import random

# Список слов для игры
words = ["hangman"]

# Инициализация состояния игры
def initialize():
    if 'word' not in st.session_state:
        st.session_state.word = random.choice(words)  # Случайное слово
        st.session_state.guessed_letters = []          # Угаданные буквы
        st.session_state.remaining_attempts = 6        # Количество попыток

initialize()

# Функция для отображения текущего состояния слова
def display_word():
    displayed_word = ''
    for char in st.session_state.word:
        if char in st.session_state.guessed_letters:
            displayed_word += letter  # Показываем угаданную букву
        else:
            displayed_word += '-'  # Показываем тире для неугаданных букв
    return displayed_word

# Функция для отображения угаданных букв
def display_guessed_letters():
    return ', '.join(st.session_state.guessed_letters)

# Ввод буквы от игрока
if 'input_letter' not in st.session_state:
    st.session_state.input_letter = ''  # Инициализация пустой строки

letter = st.text_input("Введите букву:", value=st.session_state.input_letter, max_chars=1, key="input_letter").lower()

if letter:
    if len(letter) != 1:
        st.warning("Пожалуйста, введите только одну букву!")
    elif letter in st.session_state.guessed_letters:
        st.warning("Вы уже угадали эту букву!")
    elif letter in st.session_state.word:
        st.session_state.guessed_letters.append(letter)
        st.success("Правильно!")
    else:
        st.session_state.guessed_letters.append(letter)
        st.session_state.remaining_attempts -= 1
        st.error("Неправильно!")



# Явно обновляем отображение слова и угаданных букв после ввода
st.write("Слово:", display_word())
st.write(f"Осталось попыток: {st.session_state.remaining_attempts}")
st.write(f"Угаданные буквы: {display_guessed_letters()}")

# Проверка на выигрыш или проигрыш
if set(st.session_state.word).issubset(set(st.session_state.guessed_letters)):
    st.success(f"Поздравляем! Вы угадали слово: {st.session_state.word}")
    if st.button("Играть снова"):
        initialize()

elif st.session_state.remaining_attempts <= 0:
    st.error(f"Вы проиграли! Загаданное слово было: {st.session_state.word}")
    if st.button("Играть снова"):
        initialize()