import tkinter as tk

root = tk.Tk()
root.title("برنامه پشتیبانی‌گیری")

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400
canvas1 = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, relief='raised')
canvas1.pack()
h0 = 25
diff = 30
label1 = tk.Label(root, text='به برنامه پشتیبانی برنامه های اندروید خوش آمدید')
label1.config(font=('B Nazanin', 17))
canvas1.create_window(WINDOW_WIDTH / 2, h0, window=label1)
label2 = tk.Label(root, text='برای انتخاب کردن برنامه های خاص نام هر کدام را وارد کرده و دکمه اضافه کردن را فشار دهید')
label2.config(font=('B Nazanin', 14))
canvas1.create_window(WINDOW_WIDTH / 2, h0+diff, window=label2)
label3 = tk.Label(root, text=' برای انتخاب کردن همه برنامه ها دکمه همه را فشار دهید')
label3.config(font=('B Nazanin', 14))
canvas1.create_window(WINDOW_WIDTH / 2, h0+(diff*2), window=label3)
label4 = tk.Label(root, text=' در صورتی که قبلاً پشتیبان گیری کرده اید برای رفتن به صفحه بازیابی، دکمه بازیابی را فشار دهید.')
label4.config(font=('B Nazanin', 14))
canvas1.create_window(WINDOW_WIDTH / 2, h0+(diff*3), window=label4)
entry1 = tk.Entry(root)
canvas1.create_window(WINDOW_WIDTH / 2, h0+(diff*4), window=entry1)


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

button1 = tk.Button(text='پشتیبان گیری', command=backup_process, bg='brown', fg='white',
                    font=('B Nazanin', 9, 'bold'))
button2 = tk.Button(text='اضافه کردن', command=add_one, bg='green', fg='white',
                    font=('B Nazanin', 9, 'bold'))
button3 = tk.Button(text='همه', command=add_all, bg='green', fg='white',
                    font=('B Nazanin', 9, 'bold'))
button4 = tk.Button(text='بازیابی', command=restore, bg='blue', fg='white',
                    font=('B Nazanin', 9, 'bold'))
canvas1.create_window(WINDOW_WIDTH / 2 - 200, 220, window=button1)
canvas1.create_window(WINDOW_WIDTH / 2 - 200, 140, window=button2)
canvas1.create_window(WINDOW_WIDTH / 2 - 200, 180, window=button3)
canvas1.create_window(WINDOW_WIDTH / 2 - 200, 260, window=button4)

root.mainloop()
