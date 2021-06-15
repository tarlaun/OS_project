import tkinter as tk

root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=300, relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='به برنامه پشتیبانی و بازیابی برنامه های اندروید خوش آمدید')
label1.config(font=('B Nazanin', 14))
canvas1.create_window(200, 25, window=label1)

entry1 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)


def backup_process():
    pass


def restore_process():
    pass


button1 = tk.Button(text='پشتیبان گیری', command=backup_process, bg='brown', fg='white',
                    font=('B Nazanin', 9, 'bold'))

button2 = tk.Button(text='بازیابی', command=restore_process, bg='brown', fg='white',
                    font=('B Nazanin', 9, 'bold'))

canvas1.create_window(200, 180, window=button1)
canvas1.create_window(200, 220, window=button2)

root.mainloop()
