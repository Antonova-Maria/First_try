import streamlit as st
import random
import uuid

# Список слов для игры
words = ["hangman"]

# Инициализация состояния игры
def initialize():
    if 'word' not in st.session_state:
        st.session_state.word = random.choice(words)  # Случайное слово
        st.session_state.guessed_letters = []          # Угаданные буквы
        st.session_state.remaining_attempts = 6        # Количество попыток
    
    if 'input_text_key' not in st.session_state:
        st.session_state.input_text_key = str(uuid.uuid4())

# Функция для начала новой игры
def play_again():
    st.session_state.word = random.choice(words)
    st.session_state.guessed_letters = []
    st.session_state.remaining_attempts = 6
    st.session_state.input_text_key = str(uuid.uuid4())  # Обновляем ключ поля ввода

# Функция для очистки поля ввода
def clear_field():
    st.session_state.input_text_key = str(uuid.uuid4())

# Функция для отображения текущего состояния слова
def display_word():
    displayed_word = ''
    for char in st.session_state.word:
        if char in st.session_state.guessed_letters:
            displayed_word += char  # Показываем угаданную букву
        else:
            displayed_word += '-'  # Показываем тире для неугаданных букв
    return displayed_word

# Функция для отображения угаданных букв
def display_guessed_letters():
    return ', '.join(st.session_state.guessed_letters) if st.session_state.guessed_letters else "Нет"

# Инициализация игры
initialize()

# Заголовок игры
st.title("Игра Виселица")
st.write("Угадайте загаданное слово, вводя по одной букве.")

# Отображение текущего состояния игры
st.write("Слово:", display_word())
st.write(f"Осталось попыток: {st.session_state.remaining_attempts}")
st.write(f"Угаданные буквы: {display_guessed_letters()}")

# Проверка на выигрыш или проигрыш
game_over = False

if set(st.session_state.word).issubset(set(st.session_state.guessed_letters)):
    st.success(f"Поздравляем! Вы угадали слово: {st.session_state.word}")
    game_over = True
    st.button("Играть снова", on_click=play_again)

elif st.session_state.remaining_attempts <= 0:
    st.error(f"Вы проиграли! Загаданное слово было: {st.session_state.word}")
    game_over = True
    st.button("Играть снова", on_click=play_again)

# Ввод буквы от игрока (только если игра не окончена)
if not game_over:
    letter = st.text_input("Введите букву:", value='', max_chars=1, key=st.session_state.input_text_key).lower()

    if letter:
        if len(letter) != 1:
            st.warning("Пожалуйста, введите только одну букву!")
            clear_field()
            
        elif not letter.isalpha():
            st.warning("Пожалуйста, введите букву!")
            clear_field()
            
        elif letter in st.session_state.guessed_letters:
            st.warning("Вы уже угадали эту букву!")
            clear_field()
            
        elif letter in st.session_state.word:
            st.session_state.guessed_letters.append(letter)
            st.success("Правильно!")
            clear_field()
            
        else:
            st.session_state.guessed_letters.append(letter)
            st.session_state.remaining_attempts -= 1
            st.error("Неправильно!")
            clear_field()
            
