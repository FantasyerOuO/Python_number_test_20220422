

from ctypes.wintypes import RGB
import tkinter as tk
from turtle import color

from pyparsing import col
# 建立視窗Create a window
window_0 = tk.Tk()
# 設定視窗大小
window_0.geometry('450x600')
#設定視窗可調整
window_0.resizable(False,False)

# 設定視窗標題
window_0.title('數字計算視窗編寫')

# Label

label_0=tk.Label(window_0,text=0,font=('新細明體',20,'bold'),fg='red',height=4)
button_1=tk.Button(text='1',width=10,height=4,font=('新細明體',15))
button_2=tk.Button(text='2',width=10,height=4,font=(15))
button_3=tk.Button(text='3',width=10,height=4,font=(15))
button_4=tk.Button(text='4',width=10,height=4,font=(15))
button_5=tk.Button(text='5',width=10,height=4,font=(15))
button_6=tk.Button(text='6',width=10,height=4,font=(15))
button_7=tk.Button(text='7',width=10,height=4,font=(15))
button_8=tk.Button(text='8',width=10,height=4,font=(15))
button_9=tk.Button(text='9',width=10,height=4,font=(15))
button_0=tk.Button(text='0',width=10,height=4,font=(15))
button_e=tk.Button(text='=',width=10,height=4,bg='cyan',font=(15))# =
button_a=tk.Button(text='+',width=10,height=4,font=(15))# +
button_r=tk.Button(text='-',width=10,height=4,font=(15))# -
button_t=tk.Button(text='x',width=10,height=4,font=(15))# *
button_d=tk.Button(text='/',width=10,height=4,font=(15))# /
button_c=tk.Button(text='C',width=10,height=4,font=(15))# c


label_0.grid(row=0, column=3,padx=5,pady=10)
button_1.grid(row=3,column=0,padx=5,pady=10)
button_2.grid(row=3,column=1,padx=5,pady=10)
button_3.grid(row=3,column=2,padx=5,pady=10)
button_4.grid(row=2,column=0,padx=5,pady=10)
button_5.grid(row=2,column=1,padx=5,pady=10)
button_6.grid(row=2,column=2,padx=5,pady=10)
button_7.grid(row=1,column=0,padx=5,pady=10)
button_8.grid(row=1,column=1,padx=5,pady=10)
button_9.grid(row=1,column=2,padx=5,pady=10)
button_0.grid(row=4,column=1,padx=5,pady=10)
button_c.grid(row=4,column=0,padx=5,pady=10)
button_e.grid(row=4,column=2,padx=5,pady=10)
button_a.grid(row=1,column=3,padx=5,pady=10)
button_r.grid(row=2,column=3,padx=5,pady=10)
button_t.grid(row=3,column=3,padx=5,pady=10)
button_d.grid(row=4,column=3,padx=5,pady=10)



# 設定視窗迴圈
window_0.mainloop()