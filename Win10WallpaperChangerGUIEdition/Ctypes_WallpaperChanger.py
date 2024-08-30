import ctypes
SPIF_SENDCHANGE = 0x2
SPI_SETDESKWALLPAPER = 0x0014
class Wallpaper:
    def ChangeWallpaperW(filename : str):
        User32 = ctypes.WinDLL("User32.dll")
        User32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, filename, SPIF_SENDCHANGE) #Sending Changing Wallpaper in Windows 10 or 11 :D