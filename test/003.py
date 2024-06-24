import sys
sys.path.append('..')
from tkwebview2.tkwebview2 import WebView2
import threading
import time
import sys
import random
import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Threading')
from tkinter import Tk, Button
from System import IntPtr, Int32, Func, Type, Environment
from System.Windows.Forms import Control
from System.Threading import Thread,ApartmentState,ThreadStart,SynchronizationContext,SendOrPostCallback

def main():
    def open_devtool():
            frame.core.OpenDevToolsWindow()
    root=Tk()
    root.geometry('600x600+5+5')

    frame=WebView2(root,500,500)
    frame.pack(side='left')
    frame.load_url('https://python.org/')
    Button(root,text='DevTool',command=open_devtool).pack()

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

