import tkinter as tk
import sys
import os


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


def change_list(a, b, c):
    search_order = []
    if not deftext:
        inputstr = str(sv.get())
    else:
        inputstr = ""
    search_order = sorted(app_list, key=lambda x: -LCSubStr(str(x), inputstr))
    curselect = [ls.get(i) for i in ls.curselection()]
    ls.delete(0, tk.END)
    for i in range(len(search_order)):
        app = search_order[i]
        ls.insert(tk.END, app)
        if app in curselect:
            ls.select_set(i)


def handle_focus_in(a):
    global deftext
    if deftext:
        deftext = False
        txt_box.delete(0, tk.END)
        txt_box.config(fg='black')


def handle_focus_out(a):
    global deftext
    if len(sv.get()) == 0:
        txt_box.delete(0, tk.END)
        txt_box.config(fg='grey')
        txt_box.insert(0, search_text)
        deftext = True


def backup():
    sel = [ls.get(i) for i in ls.curselection()]
    if len(sel) == len(app_list):
        print('ALL')
        exit(0)
    elif len(sel) != 0:
        print(' '.join(sel))
        exit(0)


app_list = [str(x) for x in sys.argv[1:]]
app_list = list(set(app_list))
root = tk.Tk()
root.geometry('500x500')
root.title("پشتیبان‌گیر آندروید")
label = tk.Label(text="سلام. لطفا برنامه‌های مورد نظر خود را انخاب کنید")
label.pack()
lsfrm = tk.Frame(root)
lsfrm.pack()
ls = tk.Listbox(lsfrm, width=30, height=20,
                selectmode='multiple', exportselection=False)
ls.pack(side='left', fill='y')
scroll = tk.Scrollbar(lsfrm, orient='vertical')
scroll.config(command=ls.yview)
scroll.pack(side='right', fill='y')
ls.config(yscrollcommand=scroll.set)
for app in app_list:
    ls.insert(tk.END, app)
sv = tk.StringVar()
sv.trace_add("write", callback=change_list)
deftext = True
search_text = "Search..."
txt_box = tk.Entry(root, textvariable=sv)
txt_box.insert(tk.END, search_text)
txt_box.config(fg='grey')
txt_box.pack()
txt_box.bind("<FocusIn>", handle_focus_in)
txt_box.bind("<FocusOut>", handle_focus_out)
selb = tk.Button(text="انتخاب همه", command=lambda: ls.selection_set(0, tk.END)
                 )
selb.pack()
deselb = tk.Button(text="پاک کردن انتخاب‌ها",
                   command=lambda: ls.selection_clear(0, tk.END))
deselb.pack()
btn = tk.Button(text="پشتیبان‌گیری", command=backup)
btn.pack()
tk.mainloop()
