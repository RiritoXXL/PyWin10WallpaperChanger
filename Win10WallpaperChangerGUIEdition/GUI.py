import Ctypes_WallpaperChanger as wallp
import dearpygui.dearpygui as dpg

def GetValue():
    return dpg.get_value("wallpaper_filename")

def ChangeWallpaper():
    return wallp.Wallpaper.ChangeWallpaperW(str(GetValue()))
def Main():
    dpg.create_context()
    with dpg.window(label="Windows10WallpaperChanger by RiritoXXL", tag="windowmain", width=555, height=555):
        dpg.add_text("This Is My First Program to Changing Wallpaper in Windows 10 or 11...")
        dpg.add_input_text(label="Wallpaper Filename", tag="wallpaper_filename")
        dpg.add_button(label="Change Wallpaper!", callback=ChangeWallpaper)
    dpg.create_viewport(title='PyWin10WallpaperChanger by RiritoXXL', width=555, height=555)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("windowmain", True)
    dpg.start_dearpygui()
    dpg.destroy_context()