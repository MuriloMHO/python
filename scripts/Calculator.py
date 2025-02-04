from tkinter import *


field_text = ''

def add_to_field(sth):
    global field_text
    field_text = field_text+str(sth)
    field.delete('1.0', 'end')
    field.insert('1.0', field_text)

def calculate():
    global field_text
    result = str(eval(field_text))
    field.delete('1.0', 'end')
    field.insert('1.0', result)

def clear():
    global field_text
    field_text = ''
    field.delete('1.0', 'end')

root = Tk()
root.geometry('300x300')
field = Text(root, height=2, width=21, font=('Times New Roman', 20))
field.grid(row=1, column=1, columnspan=4)

btn_1 = Button(root, text='1', command=lambda: add_to_field(1), width=5, font=('Times New Roman', 14))
btn_1.grid(row=4, column=1)

btn_2 = Button(root, text='2', command=lambda: add_to_field(2), width=5, font=('Times New Roman', 14))
btn_2.grid(row=4, column=2)

btn_3 = Button(root, text='3', command=lambda: add_to_field(3), width=5, font=('Times New Roman', 14))
btn_3.grid(row=4, column=3)

btn_4 = Button(root, text='4', command=lambda: add_to_field(4), width=5, font=('Times New Roman', 14))
btn_4.grid(row=3, column=1)

btn_5 = Button(root, text='5', command=lambda: add_to_field(5), width=5, font=('Times New Roman', 14))
btn_5.grid(row=3, column=2)

btn_6 = Button(root, text='6', command=lambda: add_to_field(6), width=5, font=('Times New Roman', 14))
btn_6.grid(row=3, column=3)

btn_7 = Button(root, text='7', command=lambda: add_to_field(7), width=5, font=('Times New Roman', 14))
btn_7.grid(row=2, column=1)

btn_8 = Button(root, text='8', command=lambda: add_to_field(8), width=5, font=('Times New Roman', 14))
btn_8.grid(row=2, column=2)

btn_9 = Button(root, text='9', command=lambda: add_to_field(9), width=5, font=('Times New Roman', 14))
btn_9.grid(row=2, column=3)

btn_0 = Button(root, text='0', command=lambda: add_to_field(0), width=5, font=('Times New Roman', 14))
btn_0.grid(row=5, column=1)

btn_divide = Button(root, text='/', command=lambda: add_to_field('/'), width=5, font=('Times New Roman', 14))
btn_divide.grid(row=2, column=4)

btn_multply = Button(root, text='*', command=lambda: add_to_field('*'), width=5, font=('Times New Roman', 14))
btn_multply.grid(row=3, column=4)

btn_add = Button(root, text='+', command=lambda: add_to_field('+'), width=5, font=('Times New Roman', 14))
btn_add.grid(row=4, column=4)

btn_minus = Button(root, text='-', command=lambda: add_to_field('-'), width=5, font=('Times New Roman', 14))
btn_minus.grid(row=5, column=4)

btn_dot = Button(root, text='.', command=lambda: add_to_field('.'), width=5, font=('Times New Roman', 14))
btn_dot.grid(row=5, column=2)

btn_bracket_open = Button(root, text='(', command=lambda: add_to_field('('), width=5, font=('Times New Roman', 14))
btn_bracket_open.grid(row=6, column=1)

btn_bracket_close = Button(root, text=')', command=lambda: add_to_field(')'), width=5, font=('Times New Roman', 14))
btn_bracket_close.grid(row=6, column=2)

btn_clear = Button(root, text='Clear', command=lambda: clear(), width=5, font=('Times New Roman', 14))
btn_clear.grid(row=5, column=3)

btn_equal = Button(root, text='=', command=lambda: calculate(), width=13, font=('Times New Roman', 14))
btn_equal.grid(row=6, column=3, columnspan=2)

root.mainloop
