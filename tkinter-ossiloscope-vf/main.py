# -*- coding: utf-8 -*-
import sys
major=sys.version_info.major
minor=sys.version_info.minor
if major==2 and minor==7 :
    import Tkinter as tk
    import tkFileDialog as filedialog
elif major==3 :
    import tkinter as tk
    from tkinter import filedialog
else :
    if __name__ == "__main__" :
        print("Your python version is : ",major,minor)
        print("... I guess it will work !")
    import tkinter as tk
    from tkinter import filedialog 

from math import pi,sin
from utils import radians
from models import Generator
from controllers import Controller,SignalControls
from views import Screen

if   __name__ == "__main__" :
    root = tk.Tk()
    root.title("Osciloscope")
    root.option_readfile("config.opt")
    model_X = Generator("X")
    model_Y = Generator("Y")
    view = Screen(root, tiles=10)
    ctrl = Controller(root, view, [model_X, model_Y])
    model_X.generate()
    model_Y.generate()

    root.mainloop()

