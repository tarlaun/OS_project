import tkinter as tk

root = tk.Tk()
root.title("برنامه پشتیبانی‌گیری")

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400
canvas1 = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='به برنامه پشتیبانی برنامه های اندروید خوش آمدید')
label1.config(font=('B Nazanin', 17))
canvas1.create_window(WINDOW_WIDTH/2, 25, window=label1)
label2 = tk.Label(root, text='برای انتخاب کردن برنامه های خاص نام هر کدام را وارد کرده و دکمه اضافه کردن را فشار دهید')
label2.config(font=('B Nazanin', 14))
canvas1.create_window(WINDOW_WIDTH/2, 70, window=label2)
label3 = tk.Label(root, text=' برای انتخاب کردن همه برنامه ها دکمه همه را فشار دهید')
label3.config(font=('B Nazanin', 14))
canvas1.create_window(WINDOW_WIDTH/2, 100, window=label3)
entry1 = tk.Entry(root)
canvas1.create_window(WINDOW_WIDTH/2, 140, window=entry1)


def backup_process():
    pass



button1 = tk.Button(text='پشتیبان گیری', command=backup_process, bg='brown', fg='white',
                    font=('B Nazanin', 9, 'bold'))
button2 = tk.Button(text='اضافه کردن', command=backup_process, bg='green', fg='white',
                    font=('B Nazanin', 9, 'bold'))
canvas1.create_window(WINDOW_WIDTH/2 - 100, 140, window=button2)
canvas1.create_window(WINDOW_WIDTH/2, 180, window=button1)


root.mainloop()
