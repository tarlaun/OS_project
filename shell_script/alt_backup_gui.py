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

def change_list(a,b,c):
    final_app = []
    inputstr = str(sv.get())
    # for app in app_list:
    #     lcs = LCSubStr(str(app), str(inputstr))
    #     if lcs > max_len:
    #         max_len = lcs
    #         final_app = [app]
    #     elif lcs == max_len:
    #         final_app.append(app)
    final_app = sorted(app_list,key=lambda x: -LCSubStr(str(x),inputstr))
    curselect = [ls.get(i) for i in ls.curselection()]
    ls.delete(0,ls.size())
    for i in range(len(final_app)):
        app = final_app[i]
        ls.insert(tk.END,app)
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
        txt_box.insert(0, "Search...")
        deftext = True

def backup():
    sel = [ls.get(i) for i in ls.curselection()]
    if len(sel) != 0:
        print(' '.join(sel))
        exit(0)

app_list = [str(x) for x in sys.argv[1:]]
root = tk.Tk()
root.geometry('500x500')
root.title("Backup")

lsfrm = tk.Frame(root)
lsfrm.pack()

ls = tk.Listbox(lsfrm,width = 30,height = 20,selectmode = 'multiple') 
ls.pack(side='left',fill='y')

scroll = tk.Scrollbar(lsfrm,orient='vertical')
scroll.config(command=ls.yview)
scroll.pack(side='right',fill='y')
ls.config(yscrollcommand=scroll.set)
for app in app_list:
    ls.insert(tk.END,app)
sv = tk.StringVar()
sv.trace_add("write",callback=change_list)

deftext = True
txt_box = tk.Entry(root,textvariable=sv)
txt_box.insert(tk.END,'Search...')
txt_box.config(fg='grey')
txt_box.pack()
txt_box.bind("<FocusIn>", handle_focus_in)
txt_box.bind("<FocusOut>", handle_focus_out)
btn = tk.Button(text="Backup",command=backup)
btn.pack()
tk.mainloop()
