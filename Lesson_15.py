import tkinter as tk
import logging
import argparse

# ��������� �����������
logging.basicConfig(filename='calc.log', level=logging.INFO)

# �������� ����
root = tk.Tk()
root.title("�����������")

# �������� ���� ��� �����
input_field = tk.Entry(root, width=30)
input_field.grid(row=0, column=0, columnspan=4)

# ������� ��� ���������� ������� � ���� �����
def add_to_input(symbol):
    input_field.insert(tk.END, symbol)

# ������� ��� �������� ������� �� ���� �����
def delete_from_input():
    input_field.delete(len(input_field.get())-1, tk.END)

# ������� ��� ���������� ���������� � ������ ��� � ���� �����
def calculate():
    expression = input_field.get()
    try:
        result = eval(expression)
        input_field.delete(0, tk.END)
        input_field.insert(tk.END, str(result))
        logging.info(f"���������: {expression} = {result}")
    except Exception as e:
        logging.error(f"������: {str(e)}")

# �������� ������
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

# ������ ����������
root.mainloop()

# ��������� ���������� �� ��������� ������
parser = argparse.ArgumentParser(description='�����������')
parser.add_argument('expression', nargs='?', help='��������� ��� ����������')

args = parser.parse_args()

if args.expression:
    try:
        result = eval(args.expression)
        print(f"���������: {args.expression} = {result}")
        logging.info(f"���������: {args.expression} = {result}")
    except Exception as e:
        print(f"������: {str(e)}")
        logging.error(f"������: {str(e)}")