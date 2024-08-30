import os
import GUI
import atexit
import tkinter.messagebox as m

@atexit.register
def ExitCode():
    if m.askyesno(title="PyWin10WallpaperChanger", message="Do you want to Exit?!") == m.YES:
        exit(4003)
    else:
        print("OKAY!!!")
def Main():
    GUI.Main()

if __name__ == "__main__":
    Main()