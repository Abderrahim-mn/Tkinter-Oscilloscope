# -*- coding: utf-8 -*-
import sys
from PIL import Image,ImageGrab
from tkinter import Canvas, colorchooser
from scipy.spatial import KDTree
import webcolors as wc

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

from observer import Observer
from models import Generator


class Screen(Observer):
    def __init__(self, parent, tiles=4, bg="white"):
        super().__init__()
        self.parent = parent
        self.canvas = tk.Canvas(parent, bg=bg)
        self.canvas.bind("<Configure>", self.resize)
        self.width = int(self.canvas.cget("width"))
        self.height = int(self.canvas.cget("height"))
        self.resize = False
        self.tiles = tiles
        self.generators = []
        self.lines = []
        self.spots = {}
        self.curves = 'red'
        self.create_grid()
        #self.save_as_png(self.canvas,"canvas")
        msg = ""
        msgLbl= tk.StringVar()
        label = tk.Label(parent, textvariable=msgLbl)
        msgLbl.set(msg)
        label.pack()
    
    def animate_spot(self, generator_name, samples_per_sec=1, radius=5, i=0):
        generator = None
        for gen in self.generators:
            if gen.get_name() == generator_name:
                generator = gen
                break

        if generator is None:
            self.canvas.delete(f"spot_{generator_name}")
            del self.spots[generator_name]
            return

        if generator_name not in self.spots:
            self.spots[generator_name] = self.canvas.create_oval(
                -radius, -radius, radius, radius,
                fill='yellow', outline='black', tags=f"spot_{generator_name}"
            )

        spot = self.spots[generator_name]
        width, height = self.width, self.height

        signal = generator.get_signal()
        if i >= len(signal):
            i = 0

        x, y = signal[i]
        x *= width
        y = (y + 1) * height / 2
        self.canvas.coords(spot, x - radius, y - radius, x + radius, y + radius)
        return self.parent.after(
            int(1000 / samples_per_sec),
            self.animate_spot, generator_name, samples_per_sec, radius, i + 1
        )

    def __repr__(self):
        return "Screen()"

    def get_canvas(self) :
        return self.canvas

    def get_tiles(self):
        return self.tiles

    def set_tiles(self, tiles):
        self.tiles = tiles

    def plot_signal(self, signal, curves, name="signal"):
        named_color = curves
        if curves != "red":
            named_color = self.convert_rgb_to_names(curves[0])
        self.canvas.delete(name)
        if signal and len(signal) > 1:
            width, height = self.width, self.height
            plot = [(x * width, height / 2 * (y + 1)) for (x, y) in signal]
            line = self.canvas.create_line(plot, fill=named_color, smooth=1, width=3, tags=name)
            self.lines.append(line)
    
    def convert_rgb_to_names(self,rgb_tuple):
    # a dictionary of all the hex and their respective names in css3
        css3_db = wc.CSS3_HEX_TO_NAMES
        names = []
        rgb_values = []
        for color_hex, color_name in css3_db.items():
            names.append(color_name)
            rgb_values.append(wc.hex_to_rgb(color_hex))
        kdt_db = KDTree(rgb_values)
        distance, index = kdt_db.query(rgb_tuple)
        return names[index]

    def create_grid(self):
        white = (255, 255, 255)
        width, height = self.width, self.height
        tiles = self.tiles
        tile_x = width / tiles
        for t in range(1, tiles + 1):          # lignes verticales
            x = t * tile_x
            self.canvas.create_line(x, 0, x, height, tags="grid")
            self.canvas.create_line(x, height / 2 - 5, x, height / 2 + 5, width=4, tags="grid")
        tile_y = height / tiles
        for t in range(1, tiles + 1):           # lignes horizontales
            y = t * tile_y
            self.canvas.create_line(0, y, width, y, tags="grid")
            self.canvas.create_line(width / 2 - 5, y, width / 2 + 5, y, width=4,tags="grid") 
        
    # Save function for the "Save Image" menu button    
    def save_as_png(self,canvas,fileName):
        x = tk.Canvas.winfo_rootx(canvas)
        y = tk.Canvas.winfo_rooty(canvas)
        w = tk.Canvas.winfo_width(canvas) 
        h = tk.Canvas.winfo_height(canvas)
 
        img= ImageGrab.grab((x, y, x+w, y+h)).save(fileName+'.png')

    def color_of_background(self):
        bgcolor = colorchooser.askcolor(title ="Choose a color for your curves")
        self.canvas.config(bg=bgcolor[1])
    
    def color_of_curves(self):
        self.curves = colorchooser.askcolor(title ="Choose a color for your curves")
        for line in self.lines:
            self.canvas.itemconfig(line,fill=self.curves[1])

    def update(self, generator):
        self.plot_signal(generator.get_signal(), self.curves, name = generator.get_name())

    def add_generator(self, generator):
        self.generators.append(generator)
        generator.attach(self)
        self.animate_spot(generator.get_name(), samples_per_sec=70)
        self.update(generator)

    def remove_generator(self, generator):
        generator.detach(self)
        self.canvas.delete(generator.name)
        try:
            self.generators.remove(generator)
        except ValueError:
            pass

    def resize(self, event):
        self.width = event.width
        self.height = event.height
        print("resize : ",self.width,self.height)
        self.canvas.delete("grid")
        self.create_grid()
        for generator in self.generators:
            self.update(generator)


    
if   __name__ == "__main__" :
    root=tk.Tk()
    root.title("Osciloscope")
    view = Screen(root, tiles=10)
    gen  = Generator("TEST")
    view.add_generator(gen)
    gen.generate()
    view.get_canvas().pack()
    
    width = 400
    height = 300
    center = height//2
    white = (255, 255, 255)
    green = (0,128,0)
    cv = tk.Canvas(root, width=width, height=height, bg='white')
    cv.pack()


    root.mainloop()