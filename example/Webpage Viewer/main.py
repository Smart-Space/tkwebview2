#############################################################################
#                                                                           #
#        |     |                 |            o              ,--.           #
#        |___  |__/  . . . ,---. |___  \   /  . ,---. . . .   __/           #
#        |     |  \  | | | |___| |   \  \ /   | |---' | | |  /              #
#        \___| |   \ \_^_/ \___, \___/   V    | \___, \_^_/  |___           #
#                                                                           #
# .  .   .  .  .                          .       .                         #
#  \  \ /  /   |                           \     /o                         #
#   \  \  /.-. |.-. .,-.  .-.  .-.. .-.     \   / .  .-..   .   . .-. .--.  #
#    \/ \/(.-' |   )|   ) ___|(   |(.-'      \ /  | (.-' \ / \ / (.-' |     #
#     ' '  `--''`-' |`-' (___| `-`| `--'      '   |  `--' V   V   `--''     #
#                   |          ._.'                                         #
#                                                                           #
#v2.0.1                      Unicode Text: http://patorjk.com/software/taag/#
#===========================================================================#
#                      2022 By rgzz666 / totowang-hhh                       #
#############################################################################
#The contents of this file are subject to the Mozilla Public Licene         #
#Version 2.0 (the "License"); you may not use this file except in           #
#compliance with the License. You may obtain a copy of the License at       #
#https://www.mozilla.org/MPL/2.0                                            #
#                                                                           #
#Software distributed under the License is distributed on an "AS IS"        #
#basis, WITHOUT WARRANTY OF ANY KIND, either express or implied. See the    #
#License for the specific language governing rights and limitations         #
#under the License.                                                         #
#                                                                           #
#The Initial Developer of the Original Code is rgzz666 (aka. totowang-hhh). #
#                                                                           #
#Portions created by ______________________ are                             #
#Copyright (C) _______________________. All Rights Reserved.                #
#############################################################################

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
import os
import webbrowser
import time
import tttk

win=tk.Tk()
win.title('tkwebview2 Demo Launcher')

#The following code are not really needed, just for checking if tkwebview2 and Edge WebView 2 Runtime are installed
try:
    from tkwebview2.tkwebview2 import have_runtime
    if not have_runtime():
        edge_webview_runtime_not_installed()
except Exception as e:
    err=''
    err+='\n------------------------------------------------------------\n'
    err+=str(e)
    err+='\n------------------------------------------------------------\n'
    if str(e)=="No module named 'tkwebview2'":
        err+='Relax, this is not an error, please install tkwebview2'
    elif str(e)=="name 'edge_webview_runtime_not_installed' is not defined":
        err+='Relax, this is not an error, please install Edge WebView 2 runtime'
    else:
        print(str(e))
        err+='Sorry for wasting your time, but in fact, this is really an error, take a screenshot at this window and send it to tt1224@hotmail.com'
    win.withdraw()
    msgbox.showerror('Error','One or more of the following section(s) is/are not installed: \n- tkwebview2\n- Edge WebView 2 Runtime\n\n\nActually, the program got an error when checking if these things are installed. '+
                     'read the following info to check if this is really an error: '+err)
    exit()
###

#The only useful things for your projects
def view(url):
    if os.path.exists("./browser.py"):
        print('Webpage viewer detected, opening the webpage with it')
        os.popen('python browser.py '+url+' True')
    else:
        print('Webpage viewer not detected, opening the webpage with defult browser')
        webbrowser.open(url)
###

def tttk_demo(): #I just copy and paste everything without translating them...
    twin=tk.Tk()
    def osnk():
        osnk=tttk.Osnk(root=twin,entry=nenter.enter)
    def yzm():
        nenter.btn['text']='已发送'
        nenter.btn['state']='disabled'
        twin.after(3000,lambda:msgbox.showinfo('哈哈','希望您不要惦记着那个验证码:)'))
    toptip=tk.Frame(twin,bg='#FFFFFF') #顶部提示
    tk.Label(toptip,text='这个注册表单包含了tttk的所有控件，\n它们的用法或许也能给您些许提示。',font=('微软雅黑',15),bg='#FFFFFF').pack(padx=15,fill=tk.X)
    tk.Label(toptip,text='本表单旨在展示控件，并不会真正提交',font=('微软雅黑',15,'bold'),bg='#FFFFFF').pack(padx=15,fill=tk.X)
    tk.Label(toptip,text='',bg='#FFFFFF').pack(fill=tk.X) #底部间隔
    toptip.pack(fill=tk.X)
    tk.Label(twin,text='').pack() #空白分隔
    tk.Label(twin,text='请选择您的年龄').pack()
    tk.Label(twin,text='您可以比较两种数字输入框的样式和功能',fg='#A3A3A3').pack() #灰色提示文本
    tttk.NumEnterOld(twin,minnum=0).pack()
    tttk.NumEnter(twin,width=10,minnum=0).pack()
    tk.Label(twin,text='请正确设置最大值、最小值参数，否则以下就是结果',fg='#A3A3A3').pack() #灰色提示文本
    tttk.NumEnterOld(twin,minnum=0,maxnum=0).pack()
    tttk.NumEnter(twin,minnum=0,maxnum=0).pack()
    tk.Label(twin,text='').pack() #空白分隔
    tk.Label(twin,text='请输入您的联系方式').pack()
    tk.Label(twin,text='以下为带按钮的输入框（传入了command参数）及其各种用法',fg='#A3A3A3').pack() #灰色提示文本
    nenter=tttk.TipEnter(twin,text='电话号码 (+86)',command=yzm,btntxt='获取验证码')
    nenter.pack(fill=tk.X,padx=15)
    nenter.set('数字键盘与此输入框绑定')
    menter=tttk.TipEnter(twin,'您的邮箱',btntxt='X 清空')
    menter.command=menter.clear #如果需要清空自己，则需要单独指定（未来计划改进）
    menter.refresh() #如果实例化后再指定command，可能还是不会显示按钮，此时需调用refresh函数
    menter.pack(fill=tk.X,padx=15)
    tttk.TipEnter(twin,text='报告缺失的联系方式',command=lambda:msgbox.showinfo('哈哈','才不会提交呢\n信不信随你')).pack(fill=tk.X,padx=15)
    ttk.Button(twin,text='屏幕数字键盘',command=osnk).pack()
    tk.Label(twin,text='').pack() #空白分隔
    tk.Label(twin,text='以下为不带按钮的输入框（未传入command参数）',fg='#A3A3A3').pack() #灰色提示文本
    tttk.TipEnter(twin,text='您的姓名').pack(fill=tk.X,padx=15)
    tk.Label(twin,text='').pack() #空白分隔
    tk.Label(twin,text='按钮行（BtnRow）控件，您可以查看代码来学习如何指定其内容',fg='#A3A3A3').pack() #灰色提示文本
    tttk.BtnRow(twin,content={'注册':lambda:msgbox.showinfo('哈哈','告诉过你了这是假的！'),'登录':lambda:msgbox.showinfo('哈哈','告诉过你了这是假的！'),'帮助':lambda:msgbox.showinfo('这里没有帮助','你不会看看窗口顶部吗？'),
                             '关于Demo':lambda:msgbox.showinfo('关于','这是tttk的Demo\ntttk和其Demo都是 真_人工智障 的作品')}).pack()
    tk.Label(twin,text='').pack()
    twin.mainloop()

tk.Label(win,text="").pack(padx=15,pady=5,fill=tk.X) #Padding

tk.Label(win,text="Make sure you have installed Python and tkwebview2 first. \n(You've must already installed them if you can see this)").pack(padx=15,pady=5,fill=tk.X)
tk.Label(win,text="You have to add Python to PATH first.").pack(padx=15,pady=5,fill=tk.X)
tk.Label(win,text="Edge WebView 2 Runtime installation checked with\ntkwebview2, it took about "+str(int(time.process_time()))+" secs this time.").pack(padx=15,pady=5,fill=tk.X)
tk.Label(win,text="This file is written in English, bacause I'm lazy...").pack(padx=15,pady=5,fill=tk.X)

tk.Label(win,text="").pack(padx=15,pady=5,fill=tk.X) #Padding

tk.Label(win,text="Demo program by rgzz666(aka. totowang-hhh).").pack(padx=15,pady=5,fill=tk.X)
tttk.BtnRow(win,content={"Author's GitHub":lambda:view("https://github.com/totowang-hhh"),"Author's Site":lambda:view("http://rgzz.likesyou.org"),"Author's Blog":lambda:view("https://www.cnblogs.com/totowang/")},
       seperate=5).pack(padx=15,pady=5)#,fill=tk.X)

tk.Label(win,text="").pack(padx=15,pady=5,fill=tk.X) #Padding

tk.Label(win,text="Based on tkwebview2 by Smart-Space. This is an\nexample program for it.").pack(padx=15,pady=5,fill=tk.X)
tttk.BtnRow(win,content={"GitHub Repo":lambda:view("https://github.com/Smart-Space/tkwebview2"),"Author's Blog":lambda:view("https://blog.csdn.net/tinga_kilin/")},seperate=5).pack(padx=15,pady=5)#,fill=tk.X)

tk.Label(win,text="").pack(padx=15,pady=5,fill=tk.X) #Padding

urlenter=tttk.TipEnter(win,text='Open Custom URL',command=lambda:view(urlenter.get()),btntxt='GO →')
urlenter.pack(padx=15,pady=5,fill=tk.X)

#AD
tk.Label(win,text="").pack(padx=15,pady=5,fill=tk.X) #Padding

tk.Label(win,text="● ADVERTISEMENT ●",fg="#909090").pack(padx=15,pady=5,fill=tk.X)
tk.Label(win,text="The demo launcher uses tttk from the same author.\nIt's similar to tkwebview2 in usage.",fg="#909090").pack(padx=15,pady=5,fill=tk.X)
tk.Label(win,text="Have a try ?",fg="#909090").pack(padx=15,fill=tk.X)
tttk.BtnRow(win,content={"Run a Chinese Demo":tttk_demo,"GitHub Repo":lambda:view("https://github.com/totowang-hhh/tttk"),"PyPI Project Page":lambda:view("https://pypi.org/project/tttk/")},
            seperate=5).pack(padx=15,pady=5)
tk.Label(win,text="↑ HIT ME !                                                  ",fg="#909090").pack(padx=15,fill=tk.X)

tk.Label(win,text="").pack(padx=15,pady=5,fill=tk.X) #Padding

win.resizable(0,0)
win.mainloop()
