import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("برنامه پشتیبانی‌گیری")

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400
canvas1 = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, relief='raised')
canvas1.pack()
pixel = tk.PhotoImage(width=1, height=1)
h0 = 25
diff = 30
label1 = tk.Label(root, text='به برنامه پشتیبانی برنامه های اندروید خوش آمدید')
label1.config(font=('B Nazanin', 17))
canvas1.create_window(WINDOW_WIDTH / 2, h0, window=label1)
label2 = tk.Label(root, text='برای انتخاب کردن برنامه های خاص نام هر کدام را وارد کرده و دکمه اضافه کردن را فشار دهید')
label2.config(font=('B Nazanin', 14))
canvas1.create_window(WINDOW_WIDTH / 2, h0 + diff, window=label2)
label3 = tk.Label(root, text=' برای انتخاب کردن همه برنامه ها دکمه همه را فشار دهید')
label3.config(font=('B Nazanin', 14))
canvas1.create_window(WINDOW_WIDTH / 2, h0 + (diff * 2), window=label3)
label4 = tk.Label(root,
                  text=' در صورتی که قبلاً پشتیبان گیری کرده اید برای رفتن به صفحه بازیابی، دکمه بازیابی را فشار دهید')
label4.config(font=('B Nazanin', 14))
canvas1.create_window(WINDOW_WIDTH / 2, h0 + (diff * 3), window=label4)
entry1 = tk.Entry(root)
canvas1.create_window(WINDOW_WIDTH / 2, h0 + (diff * 4), window=entry1)


def backup_process():
    print("Backup Process")
    pass


def add_one():
    print("Add one")
    pass


def add_all():
    print("Add all")
    pass


def restore():
    print("Restore")
    pass


commands = dict()
commands['همه'] = add_all
commands['اضافه کردن'] = add_one
commands['بازیابی'] = restore
commands['پشتیبان گیری'] = backup_process

button_h_start = 150
i = 0
button_diff = 35
button_height = 25
button_width = 100
for text in (
        'بازیابی', 'پشتیبان گیری', 'همه', 'اضافه کردن'):
    button = tk.Button(root, text=text, image=pixel, height=button_height, width=button_width, command=commands[text],
                       compound="c")

    canvas1.create_window(WINDOW_WIDTH / 2 - 200, button_h_start + (button_diff * i), window=button)
    i += 1

root.mainloop()
