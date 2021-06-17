import tkinter as tk
import subprocess

def LCSubStr(s, t):
    # Create DP table
    n = len(s)
    m = len(t)
    dp = [[0 for i in range(m + 1)] for j in range(2)]
    res = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (s[i - 1] == t[j - 1]):
                dp[i % 2][j] = dp[(i - 1) % 2][j - 1] + 1
                if (dp[i % 2][j] > res):
                    res = dp[i % 2][j]
            else:
                dp[i % 2][j] = 0
    return res


def get_closest(inputstr, app_list):
    final_app = ""
    max_len = 0
    for app in app_list:
        lcs = LCSubStr(str(app), str(inputstr))
        if lcs > max_len:
            max_len = lcs
            final_app = str(app)

    if max_len < int(len(inputstr) * 3 / 4):
        return "no_match"
    else:
        return final_app


command = "adb shell pm list packages -3"
apps_together = subprocess.getoutput(command)
all_the_apps = apps_together.split()  # all the programs

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

programs_to_backup = []

def backup_process():
    print("Backup Process")
    print((programs_to_backup))
    
    for app in programs_to_backup:
        print(app)
        name = app[8:]
        print(name)
        command = 'adb.exe shell pm path ' + name
        name2 = subprocess.getoutput(command)[8:]
        command = 'mkdir "backup/' + name + '" -p'
        subprocess.getoutput(command)
    
    print("Backup completed!")


def add_one():
    print("Add one")
    new_app = entry1.get()
    entry1.delete(0, "end")
    closest = get_closest(new_app, all_the_apps)
    if closest == "no_match":
        print("no match found")
    else:
        print("matched with " + closest)
        programs_to_backup.append(closest)


def add_all():
    programs_to_backup = []
    programs_to_backup.extend(all_the_apps)
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
