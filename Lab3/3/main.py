import wx
from Window import Window

if __name__ == "__main__":

    app = wx.App()
    wnd = Window(None, "Поиск строк")
    app.MainLoop()