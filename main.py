

import tkinter as tk
from turtle import color
# 建立視窗Create a window
window_0 = tk.Tk()
# 設定視窗大小
window_0.geometry('400x600')
#設定視窗可調整
window_0.resizable(False,False)

# 設定視窗標題
window_0.title('數字計算視窗編寫')

# Label

label_0=tk.Label(window_0,text=0,font=('新細明體',20),fg='red',width=100,height=3)
label_0.pack()

button_1=tk.Button(text='1',width=5,height=3)
button_1.pack()

# 設定視窗迴圈
window_0.mainloop()