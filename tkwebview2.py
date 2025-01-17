from tkinter import Frame,Tk,Button
from tkinter import filedialog
import ctypes
import os
from threading import Event, Semaphore, Thread
from uuid import uuid4
import clr
import webview
from webview.window import Window
from webview.platforms.edgechromium import EdgeChrome
from webview.guilib import initialize
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Threading')
from System import IntPtr, Int32, Func, Type, Environment
from System.Windows.Forms import Control
from System.Threading import Thread,ApartmentState,ThreadStart,SynchronizationContext,SendOrPostCallback

user32=ctypes.windll.user32
guilib=initialize('edgechromium')

class WebView2(Frame):
    '''tkinter的WebView2绑定，基于pywebview & pythonnet'''

    def __init__(self,parent,width:int,height:int,url:str='',js_api=None,**kw):
        Frame.__init__(self,parent,width=width,height=height,**kw)
        control=Control()
        uid = 'master' if len(windows) == 0 else 'child_' + uuid4().hex[:8]
        window=Window(uid,str(id(self)), url=None, html=None, js_api=js_api, width=width, height=height, x=None, y=None,
                      resizable=True, fullscreen=False, min_size=(200, 100), hidden=False,
                      frameless=False, easy_drag=True,
                      minimized=False, on_top=False, confirm_close=False, background_color='#FFFFFF',
                      transparent=False, text_select=True, localization=None,
                      zoomable=True, draggable=True, vibrancy=False, focus=False)
        self.window=window
        self.web_view=EdgeChrome(control,window,None)
        self.control=control
        if hasattr(self.web_view,'webview'):
            self.web=self.web_view.webview
        else:
            self.web=self.web_view.web_view
        windows.append(window)
        self.width=width
        self.height=height
        self.parent=parent
        self.chwnd=int(str(self.control.Handle))
        user32.SetParent(self.chwnd,self.winfo_id())
        user32.MoveWindow(self.chwnd,0,0,width,height,True)
        self.loaded=window.events.loaded
        self.__go_bind()
        if url!='':
            self.load_url(url)
        self.core=None
        self.window._initialize(guilib)
        self.web.CoreWebView2InitializationCompleted+=self.__load_core#获取底层WebView2

    def __go_bind(self):
        self.bind('<Destroy>',lambda event:self.web.Dispose())
        self.bind('<Configure>',self.__resize_webview)
        self.newwindow=None
    def __resize_webview(self,event):
        user32.MoveWindow(self.chwnd,0,0,self.winfo_width(),self.winfo_height(),True)
    def __load_core(self,sender,_):
        self.core=sender.CoreWebView2
        self.core.NewWindowRequested-=self.web_view.on_new_window_request
        if self.newwindow!=None:
            self.core.NewWindowRequested+=self.newwindow
        settings = sender.CoreWebView2.Settings#设置
        settings.AreDefaultContextMenusEnabled=True#菜单
        settings.AreDevToolsEnabled=True#开发者工具
        #self.core.DownloadStarting+=self.__download_file

    def __download_file(self,sender,args):
        pass

    def get_url(self):
        #返回当前url，若果没有则为空
        return self.web_view.get_current_url()

    def evaluate_js(self,script,callback=None):
        #执行javascript代码，并返回最终结果
        js_r=[]
        semaphore=Semaphore(1)
        if callback!=None:
            return self.web_view.evaluate_js(script,semaphore,js_r,callback)
        else:
            return self.web_view.evaluate_js(script,semaphore,js_r)

    def load_css(self,css):
        #加载css
        self.web_view.load_css(css)

    def load_html(self,content,base_uri=None):
        #加载HTML代码
        #content=HTML内容
        #base_uri=基本URL，默认为启动程序的目录
        self.web_view.load_html(content,base_uri)

    def load_url(self,url):
        #加载全新的URL
        self.web_view.load_url(url)

    def reload(self):
        #重新加载页面
        self.core.Reload()

    def open_devtools(self):
        #打开开发者界面
        self.core.OpenDevToolsWindow()

    def event_core_completed(self,command):
        #当core核心被初始化后响应事件
        self.web.CoreWebView2InitializationCompleted+=command

    def event_new_window(self,command=None):
        #新窗口响应事件
        self.newwindow=command

    def none(self):
        pass


windows=[]


def have_runtime():#检测是否含有webview2 runtime
    from webview.platforms.winforms import _is_chromium
    return _is_chromium()

def install_runtime(ssl:bool=True):#安装webview2 runtime
    #https://go.microsoft.com/fwlink/p/?LinkId=2124703
    from urllib import request
    import subprocess
    import os
    import ssl
    # 创建一个SSL上下文对象
    context = ssl.create_default_context()
    # SSL证书验证
    context.check_hostname = ssl
    context.verify_mode = ssl.CERT_NONE
    url=r'https://go.microsoft.com/fwlink/p/?LinkId=2124703'
    path=os.getcwd()+'\\webview2runtimesetup.exe'
    unit=request.urlopen(url,context=context).read()
    with open(path,mode='wb') as uf:
        uf.write(unit)
    cmd=path
    p=subprocess.Popen(cmd,shell=True)
    return_code=p.wait()#等待子进程结束
    os.remove(path)
    return return_code

#print(install_runtime())
#范例
def main():
    def open_devtool():
        frame2.open_devtools()
    def frame_new(sender,args):
        deferral = args.GetDeferral()
        args.Handled = True
        args.NewWindow = frame.core
        deferral.Complete()
    if not have_runtime():#没有webview2 runtime
        install_runtime()
    root=Tk()
    root.title('pywebview for tkinter test')
    root.geometry('1200x600+5+5')

    frame=WebView2(root,500,500,url='https://www.baidu.com/')
    frame.pack(side='left')
    frame.event_new_window(frame_new)
    #frame.load_html('<h1>hi hi</h1>')

    frame2=WebView2(root,500,500)
    frame2.pack(side='left',padx=20,fill='both',expand=True)
    frame2.load_url('https://smart-space.com.cn/project/TinUI/index.html')
    Button(root,text='重载[左]',command=frame.reload).pack()
    Button(root,text='开发者视图[右]',command=open_devtool).pack()
    root.after(5000,lambda : frame2.evaluate_js('document.title',print))

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
