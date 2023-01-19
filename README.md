# tkwebview2

tkinter浏览器-网页组件，tkwebview2登场！！！

基于pythonnet-webview绑定和WebView2.Core，将受到微软WebView2的持续改进支持，外观和效能相比`tkinterie`得到大幅度改进。

## 依赖

以下是`tkwebview2`的依赖库：

- pythonnet(clr)
- pywebview(webview)

---

## 使用方法

```python
WebView2(master,width:int,height:int,url:str='',**kw)
'''
master::父组件
width::初始宽度
height::初始高度
url::网址或html文件，可以为空
**kw::其它Frame参数
'''
```

例子：

```python
from tkinter import Tk
from tkwebview2.tkwebview2 import WebView2, have_runtime, install_runtime
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Threading')
from System.Windows.Forms import Control
from System.Threading import Thread,ApartmentState,ThreadStart    

#范例
def main():
    if not have_runtime():#没有webview2 runtime
        install_runtime()
    root=Tk()
    root.title('pywebview for tkinter test')
    root.geometry('1200x600+5+5')

    frame=WebView2(root,500,500)
    frame.pack(side='left')
    frame.load_html('<h1>hi hi</h1>')

    frame2=WebView2(root,500,500)
    frame2.pack(side='left',padx=20,fill='both',expand=True)
    frame2.load_url('https://smart-space.com.cn/')

    root.mainloop()

if __name__ == "__main__":
    t = Thread(ThreadStart(main))
    t.ApartmentState = ApartmentState.STA
    t.Start()
    t.Join()
```

> 必须在STA线程模式创建窗口

---

## 方法

### get_url()

返回当前url。

### evaluate_js(self,script,callback=None)

执行JavaScript代码，并返回最终结果。

callback绑定一个函数，回调js执行返回内容。

### load_css(self,css)

加载CSS样式。

### load_html(self,content,base_uri=None)

加载HTML代码，`base_uri`为基本URL，默认为本程序启动目录。

### load_url(self,url)

加载全新url。

### reload(self)

重新加载页面。

### event_new_window(self,command=None)

绑定新窗口事件

### event_core_completed(self,command)

响应core核心初始化事件。可获取`self.core`。

> 更多方法请使用底层类：
> 
> self.web::WebView2 Class
> 
> self.core::CoreWebView2 Class（需要页面加载完成后可用，或绑定加载完成事件）

---

## 判断WebView2 runtime是否存在并处理

tkwebview2提供了两个函数：`have_runtime`, `install_runtime`。

### have_runtime()

判断运行环境是否存在，存在返回True，不存在返回False。

```python
from tkwebview2.tkwebview2 import have_runtime

print(have_runtime())
```

### install_runtime()

下载并安装运行环境。

```python
from tkwebview2.tkwebview2 import have_runtime, install_runtime

if not have_runtime():
    install_runtime()
```

> 注意：该函数会暂停程序运行，直到安装界面被用户手动关闭。期间，会下载安装程序到当前工作目录，安装完成后会自动删除。

---

## What's new

-3.5.0-

fix **initialization** bug caused by pywebview new version.

-3.4.0-

text_select, menu, devtools  are enabled.

-3.3.3-

add new demo contributed by [tt68686](https://blog.csdn.net/tt68686), `002.py` Licene: MPL v2.0.

-3.3.2-

fix the js function.

-3.3.1-

fix an `import` bug.

-3.3.0-

Delete the NewWindowRequest event.

-3.2.0-

Add some functions. Add some event callback methods. Download setup.exe in working path.

-3.0.0-

Using EdgeChrome in pywebview as widget instead of pywebview's window. More powerful.

-2.0.1-[fix]

Add `try ... except ...` to avoid error when importing as a test or a package.

-2.0.0-

You can use function `have_runtime` and `install_runtime` to check or download WebView2 Runtime in your application conveniently.

-1.2.0-

You can use it when you add a WebView in your window separately. However, you should destroy it when you want to close a window or a widget.

-1.1.0-

Upload to PYPI.