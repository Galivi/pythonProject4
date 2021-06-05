# import tkinter as tk
#
# root = tk.Tk()
#
# a = tk.Label(text="ID")
# a.pack()
# b = tk.Entry()
# b.pack()
# a = tk.Label(text="password")
# a.pack()
# b = tk.Entry()
# b.pack()
#
# root.mainloop()

#------------------------------------------------------

# import tkinter as tk
#
# root = tk.Tk()
#
# def okClick():
#     name=b.get()
#     print(name)
#     c.config(text=name)
# a= tk.Label(text="채팅창")
# a.pack()
#
# b=tk.Entry()
# b.pack()
#
# c= tk.Label(text="-")
# c.pack()
#
# btn = tk.Button(root, text="입력", command=okClick)
# btn.pack()

#root.mainloop()

#-------------------------------------------------

# import tkinter as tk
# root = tk.Tk()
# def okClick():
#     name=b.get()
#     print(name)
#     c.config(text=name)
#
# a= tk.Label(text="채팅창")
# a.pack()
#
# def ret (event):
#     a.config(text='안녕')
#
# b=tk.Entry()
# b.pack()
#
# c= tk.Label(text="-")
# c.pack()
#
# btn = tk.Button(root, text="입력", command=okClick)
# btn.pack()
#
# a.bind('<Button-1>', ret)
# root.mainloop()

#-----------------------------------------------------------------

import tkinter as tk

def cal1():
    d.config(text=int(a1.get())*int(b1.get()))
def cal2():
    d.config(text=int(a1.get())/int(b1.get()))
def cal3():
    d.config(text=int(a1.get())+int(b1.get()))
def cal4():
    d.config(text=int(a1.get())-int(b1.get()))


root = tk.Tk()
a=tk.Label(root, text='첫번째 수를 입력하세요.')
a.pack()
a1=tk.Entry(root)
a1.pack()
b=tk.Label(root, text='두번째 수를 입력하세요.')
b.pack()
b1=tk.Entry(root)
b1.pack()













