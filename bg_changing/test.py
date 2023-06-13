import win32api, win32con, win32gui, random, time

def SetWallPaper(path):
    key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,
                                "Control Panel\\\\Desktop",
                                0,win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, "0")
    win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, path, 1+2)

path = "C://Users/Jason/Documents/Python and stuff/Image.bmp"
SetWallPaper(path)