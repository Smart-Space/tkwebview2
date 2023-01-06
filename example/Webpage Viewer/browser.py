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
#The Original Code is from Easy PyPI (aka. EZPIP / PIPUI),                  #
#but now this program is indipendent from Easy PyPI.                        #
#                                                                           #
#The Initial Developer of the Original Code is rgzz666 (aka. totowang-hhh). #
#                                                                           #
#Portions created by ______________________ are                             #
#Copyright (C) _______________________. All Rights Reserved.                #
#############################################################################
#Params Intro. (sys.argv)                                                   #
#===========================================================================#
#No.    |Name (Meaning) |Optional   |Defult |Type   |Additional Info.       #
#-------+---------------+-----------+-------+-------+-----------------------#
#0      |Work Path      |True       |N/A    |str    |CAN NOT MODIFY         #
#1      |Initial URL    |False      |N/A    |str    |                       #
#2      |Use English    |True       |False  |bool   |                       #
#===========================================================================#
#Will open http://rgzz.likesyou.org/home/zero_start/ if no params are given #
#############################################################################
#This program is based on tkwebview2 by |smart-space|, and Edge WebView 2.  #
#It doesn't requires Microsoft Edge so users can remove it from their PCs.  #
#############################################################################

import tkinter as tk
import tkinter.ttk as ttk
import webbrowser
import sys
from tkwebview2.tkwebview2 import WebView2, have_runtime, install_runtime
import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Threading')
from System.Windows.Forms import Control
from System.Threading import Thread,ApartmentState,ThreadStart

def main(url,eng=False):
    webwin=tk.Tk()
    if eng:
        webwin.title('Webpage Viewer')
    else:
        webwin.title('网页查看器')
    frame=WebView2(webwin,860,480)
    frame.load_url(url)
    frame.pack(fill=tk.BOTH,expand=True)
    if eng:
        ttk.Button(webwin,text='Open in Defult Browser',command=lambda:webbrowser.open(frame.get_url())).pack(fill=tk.X,side=tk.BOTTOM)
    else:
        ttk.Button(webwin,text='在默认浏览器内打开',command=lambda:webbrowser.open(frame.get_url())).pack(fill=tk.X,side=tk.BOTTOM)
    webwin.update()
    webwin.minsize(webwin.winfo_width(),webwin.winfo_height())
    webwin.geometry('1080x680')
    webwin.mainloop()

if __name__ == "__main__":
    if len(sys.argv)<2:
        url="http://rgzz.likesyou.org/home/zero_start/"
        useeng=False
    else:
        if len(sys.argv)>2:
            useeng=bool(sys.argv[2])
        else:
            useeng=False
        url=sys.argv[1]
    t = Thread(ThreadStart(lambda:main(url,useeng)))
    t.ApartmentState = ApartmentState.STA
    t.Start()
    t.Join()
