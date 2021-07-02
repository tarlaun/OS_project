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
all_the_apps = apps_together.split()  # all the programs to backup


root = tk.Tk()
root.title("برنامه پشتیبانی‌گیری")

WINDOW_WIDTH = 1000
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
entry1 = tk.Entry(root, width=50)
canvas1.create_window(WINDOW_WIDTH / 2 - 210, h0 + (diff * 4), window=entry1)
backup_text_box = tk.Label(root, text='', width=42, height=7, borderwidth=3, relief="sunken")
canvas1.create_window(WINDOW_WIDTH / 2 - 210, WINDOW_HEIGHT * 3 / 5, window=backup_text_box)
entry2 = tk.Entry(root, width=50)
canvas1.create_window(WINDOW_WIDTH / 2 + 250, h0 + (diff * 4), window=entry2)
restore_text_box = tk.Label(root, text='', width=42, height=7, borderwidth=3, relief="sunken")
canvas1.create_window(WINDOW_WIDTH / 2 + 250, WINDOW_HEIGHT * 3 / 5, window=restore_text_box)

programs_to_backup = []
programs_to_restore = []


def backup_process():
    global programs_to_backup
    try:
        print("Backup Process")
        print((programs_to_backup))

        for app in programs_to_backup:
            print(app)
            name = app[8:]
            print(name)
            command = 'adb.exe shell pm path ' + name
            name2 = subprocess.getoutput(command)
            command = 'mkdir "backup/' + name
            subprocess.getoutput(command)
            command = 'mkdir "backup/' + name + '/apk'
            subprocess.getoutput(command)
            print("Number of the paths for this file:" + str(len(name2.split())))
            for path in name2.split():
                # backup the apk file
                path = path[8:]
                savename = path.split('==/')[-1]
                command = 'adb.exe pull /' + path + ' "backup/' + name + '/apk/' + savename
                output = subprocess.getoutput(command)
                print(output)

            # backup the data
            command = 'adb.exe backup -f backup/' + name + '/' + name + '.ab ' + name
            output = subprocess.getoutput(command)
            print(output)

        backup_text_box.config(text="Backup completed!")
        print("Backup completed!")
    except:
        backup_text_box.config(text="Something went wrong")
    finally:
        programs_to_backup = []


def add_one_backup():
    print("Add one")
    new_app = entry1.get()
    entry1.delete(0, "end")
    closest = get_closest(new_app, all_the_apps)
    if closest == "no_match":
        print("no match found")
    else:
        print("matched with " + closest)
        if closest not in programs_to_backup:
            programs_to_backup.append(closest)
        s = "\n".join(programs_to_backup)
        backup_text_box.config(text=s)


def add_all_backup():
    global programs_to_backup
    programs_to_backup = []
    programs_to_backup.extend(all_the_apps)
    s = "\n".join(programs_to_backup)
    backup_text_box.config(text=s)

def backup_listbox_add_button(listbox):
    for i in listbox.curselection():
        name = "package:" + listbox.get(i)
        if name not in programs_to_backup:
            programs_to_backup.append(name)
        s = "\n".join(programs_to_backup)
        backup_text_box.config(text=s)

def show_backup():
    new_canvas = tk.Toplevel(root, width=500, height=500)
    all_app = tk.Listbox(new_canvas, width=70, height=20, selectmode=tk.MULTIPLE)
    btn = tk.Button(new_canvas, text='اضافه کردن', command= lambda: backup_listbox_add_button(all_app))
    btn.pack(side='bottom')
    all_app.pack(side=tk.LEFT, fill=tk.BOTH)
    for a in all_the_apps:
        all_app.insert(tk.END, a[8:])
    w = tk.Scrollbar(new_canvas)
    w.pack(side=tk.RIGHT, fill=tk.BOTH)
    all_app.config(yscrollcommand=w.set)
    w.config(command=all_app.yview)


def restore_process():
    try:
        print("Restore")
        command = 'dir "backup" /b'
        file_names = subprocess.getoutput(command).split()
        file_names = programs_to_restore
        print(programs_to_restore)
        all_data_separate = False
        try:
            file_names.remove("alldata")
            all_data_separate = True
        except:
            print("no all data")

        for app in file_names:
            command = 'dir "backup/' + str(app) + '/apk" /b'
            apk_names = subprocess.getoutput(command).split()
            apk_paths = ' '.join(['backup/' + str(app) + '/apk/' + apkname for apkname in apk_names])
            command1 = 'adb install-multiple ' + apk_paths
            print(subprocess.getoutput(command1))
            if not all_data_separate:
                command2 = 'adb restore backup/' + str(app) + '/' + str(app) + '.ab'
                print(subprocess.getoutput(command2))

        if all_data_separate:
            command3 = 'adb restore -all -nosystem -f backup/alldata/alldata.ab'
            print(subprocess.getoutput(command3))

        restore_text_box.config(text="Restore completed!")
    except:
        restore_text_box.config(text="Something went wrong")

def restore_listbox_add_button(listbox):
    for i in listbox.curselection():
        name = listbox.get(i)
        if name not in programs_to_restore:
            programs_to_restore.append(name)
        s = "\n".join(programs_to_restore)
        restore_text_box.config(text=s)

def show_restore():
    new_canvas = tk.Toplevel(root, width=500, height=500)
    all_app = tk.Listbox(new_canvas, width=70, height=20, selectmode=tk.MULTIPLE)
    btn = tk.Button(new_canvas, text='اضافه کردن', command= lambda: restore_listbox_add_button(all_app))
    btn.pack(side='bottom')
    all_app.pack(side=tk.LEFT, fill=tk.BOTH)
    command = 'dir "backup" /b'
    file_names = subprocess.getoutput(command).split()
    try:
        file_names.remove("alldata")
    except:
        print("no all data")
    for a in file_names:
        all_app.insert(tk.END, a)
    w = tk.Scrollbar(new_canvas)
    w.pack(side=tk.RIGHT, fill=tk.BOTH)
    all_app.config(yscrollcommand=w.set)
    w.config(command=all_app.yview)


def add_one_restore():
    command = 'dir "backup" /b'
    file_names = subprocess.getoutput(command).split()
    try:
        file_names.remove("alldata")
    except:
        print("no all data")

    new_app = entry2.get()
    entry2.delete(0, "end")
    closest = get_closest(new_app, file_names)
    if closest == "no_match":
        print("no match found")
    else:
        print("matched with " + closest)
        if closest not in programs_to_restore:
            programs_to_restore.append(closest)
        s = "\n".join(programs_to_restore)
        restore_text_box.config(text=s)


def add_all_restore():
    global programs_to_restore
    command = 'dir "backup" /b'
    file_names = subprocess.getoutput(command).split()
    try:
        file_names.remove("alldata")
    except:
        print("no all data")
    programs_to_restore = file_names.copy()
    s = "\n".join(programs_to_restore)
    restore_text_box.config(text=s)


commands = dict()
commands['اضافه کردن همه'] = add_all_backup
commands['اضافه کردن'] = add_one_backup
commands['پشتیبان گیری'] = backup_process
commands['نشان‌دادن برنامه‌ها'] = show_backup

cursor = dict()
cursor['اضافه کردن همه'] = "plus"
cursor['اضافه کردن'] = "plus"
cursor['پشتیبان گیری'] = "target"
cursor['نشان‌دادن برنامه‌ها'] = "circle"
button_h_start = 150
i = 0
button_diff = 42.5
button_height = 25
button_width = 100
for text in (
        'پشتیبان گیری', 'اضافه کردن', 'اضافه کردن همه', 'نشان‌دادن برنامه‌ها'):
    button = tk.Button(root, text=text, image=pixel, height=button_height, width=button_width, command=commands[text],
                       compound="c", cursor = cursor[text])

    canvas1.create_window(WINDOW_WIDTH / 2 - 430, button_h_start + (button_diff * i), window=button)
    i += 1



entry1.bind('<Return>', lambda x : add_one_backup())
entry2.bind('<Return>', lambda x: add_one_restore())


commands_r = dict()
commands_r['اضافه کردن همه'] = add_all_restore
commands_r['اضافه کردن'] = add_one_restore
commands_r['بازیابی'] = restore_process
commands_r['نشان‌دادن برنامه‌ها'] = show_restore

cursor_r = dict()
cursor_r['اضافه کردن همه'] = "plus"
cursor_r['اضافه کردن'] = "plus"
cursor_r['بازیابی'] = "target"
cursor_r['نشان‌دادن برنامه‌ها'] = "circle"
button_h_start = 150
i = 0
button_diff = 42.5
button_height = 25
button_width = 100
for text in (
        'بازیابی', 'اضافه کردن', 'اضافه کردن همه', 'نشان‌دادن برنامه‌ها'):
    button = tk.Button(root, text=text, image=pixel, height=button_height, width=button_width, command=commands_r[text],
                       compound="c",cursor=cursor_r[text])

    canvas1.create_window(WINDOW_WIDTH / 2 + 30, button_h_start + (button_diff * i), window=button)
    i += 1

root.iconphoto(False, tk.PhotoImage(file='media/icon.png'))
root.mainloop()
