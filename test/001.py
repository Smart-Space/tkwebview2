'''
tkwebview2 - 001 测试
测试内容：
tkinter输入框在网页控件获取焦点后，无法继续获取焦点使用，
必须通过点击其它窗口或者让本窗口失去焦点后，才能再次使用输入框。
本次测试将测试winform的输入框能够规避这个问题。
实用：否
'''
from tkinter import Frame,Tk,Button,Entry
from tkinter import ttk
import ctypes
import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Threading')
clr.AddReference('System.Drawing')
clr.AddReference('System')
from System.Windows.Forms import Control,TextBox,Keys
from System.Threading import Thread,ApartmentState,ThreadStart
from System.Drawing import Font
from System import String,Single
from tkwebview2.tkwebview2 import WebView2

user32=ctypes.windll.user32

def tofont(name:str,size:int):
    return Font(String(name),Single(size))


#tkinter化winforms的textbox
class tkTextBox(Frame):

    def __init__(self,master,width=400,height=20):
        Frame.__init__(self,master,width=width,height=height)
        font=tofont('微软雅黑',14)
        self.tb=TextBox()
        self.ehwnd=int(str(self.tb.Handle))
        user32.SetParent(self.ehwnd,self.winfo_id())
        user32.MoveWindow(self.ehwnd,0,0,width,height,True)
        self.tb.Font=font
        self.bind('<Configure>',self.__resize)

    def __resize(self,event):
        self.tb.Width=self.winfo_width()
        self.tb.Height=self.winfo_height()

    def get(self):
        return self.tb.Text



def main():
    def frame_new(sender,args):
        deferral = args.GetDeferral()
        args.NewWindow = frame.core
        deferral.Complete()
    def loadurl(s,e):
        if e.KeyCode==Keys.Enter:
            print(Keys.Enter)
            url=entry.get()
            frame.load_url(url)
    root=Tk()
    root.title('tkwebview2 001 test')
    root.geometry('1200x600+5+5')

    frame=WebView2(root,500,500,url='https://www.baidu.com/')
    frame.pack(side='left')
    frame.event_new_window(frame_new)

    noen=ttk.Entry(root,font='微软雅黑 14')
    noen.insert(0,'tkinter输入框')
    noen.place(x=500,y=80,width=600,height=50)
    entry=tkTextBox(noen)
    entry.pack(fill='both',expand=True)
    entry.tb.KeyDown+=loadurl

    root.mainloop()


def go():
    try:
        main()
    except Exception as err:
        print(err)
if __name__ == "__main__":
    t = Thread(ThreadStart(go))
    t.ApartmentState = ApartmentState.STA
    t.Start()
    t.Join()
