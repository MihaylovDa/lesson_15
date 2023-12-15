import tkinter as tk
import logging
import argparse

# Настройка логирования
logging.basicConfig(filename='calc.log', level=logging.INFO)

# Создание окна
root = tk.Tk()
root.title("Калькулятор")

# Создание поля для ввода
input_field = tk.Entry(root, width=30)
input_field.grid(row=0, column=0, columnspan=4)

# Функция для добавления символа в поле ввода
def add_to_input(symbol):
    input_field.insert(tk.END, symbol)

# Функция для удаления символа из поля ввода
def delete_from_input():
    input_field.delete(len(input_field.get())-1, tk.END)

# Функция для вычисления результата и вывода его в поле ввода
def calculate():
    expression = input_field.get()
    try:
        result = eval(expression)
        input_field.delete(0, tk.END)
        input_field.insert(tk.END, str(result))
        logging.info(f"Результат: {expression} = {result}")
    except Exception as e:
        logging.error(f"Ошибка: {str(e)}")

# Создание кнопок
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0
for button in buttons:
    if button == '=':
        tk.Button(root, text=button, width=5, command=calculate).grid(row=row, column=col)
    else:
        tk.Button(root, text=button, width=5, command=lambda symbol=button: add_to_input(symbol)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Запуск приложения
root.mainloop()

# Обработка аргументов из командной строки
parser = argparse.ArgumentParser(description='Калькулятор')
parser.add_argument('expression', nargs='?', help='Выражение для вычисления')

args = parser.parse_args()

if args.expression:
    try:
        result = eval(args.expression)
        print(f"Результат: {args.expression} = {result}")
        logging.info(f"Результат: {args.expression} = {result}")
    except Exception as e:
        print(f"Ошибка: {str(e)}")
        logging.error(f"Ошибка: {str(e)}")