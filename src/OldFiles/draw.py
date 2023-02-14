import  tkinter as tk

root = tk.Tk()
root.title("这是Demo")
root.geometry("300x200")
#root---界面（需要放在那个界面），show----输入的字符显示为*，可以设置成show=none
e = tk.Entry(root,show='*')
e.pack()

def insert_point():
    var = e.get()
    t1.insert('insert',var)

def insert_end():
    var = e.get()
    t1.insert('end',var)

#root---界面（需要放在那个界面），text----显示文本
#width----宽度   height----高度  command----命令（执行哪个函数）
b1 = tk.Button(root,text = "insert point",width=15,height=2,command=insert_point)
b1.pack()

b2= tk.Button(root,text = "insert end",width=15,height=2,command=insert_end)
b2.pack()

#root---界面（需要放在那个界面），height ----文本框宽度
t1 = tk.Text(root,height=2)
t1.pack(fill="x")
root.mainloop()