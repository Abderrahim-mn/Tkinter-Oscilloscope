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
from observer import *

class Generator(Subject) :
    def __init__(self,name="X",mag=0.5,freq=2.0,phase=0.0,harmonics=1):
        Subject.__init__(self)
        self.name=name
        self.mag,self.freq,self.phase,self.harmonics=mag,freq,phase,harmonics
        self.signal1=[]
        self.signal = []
        self.harmo_odd_even=1
        self.samples=100
        self.generate()

    def __repr__(self):
        return "<Screen(mag:{}, freq:{}, phase:{}, harmonics :{})>".format(self.mag,self.freq,self.phase,self.harmonics)
    def get_signal(self):
        return self.signal
    def get_signal1(self):
        return self.signal1
    def get_canvas(self) :
        return self.canvas
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name=name
    def get_magnitude(self):
        return self.mag
    def set_magnitude(self,mag):
        self.mag=mag
    def get_frequency(self):
        return self.freq
    def set_frequency(self,freq):
        self.freq=freq
    def get_phase(self):
        return self.phase
    def set_phase(self,phase):
        self.phase=phase
    def get_harmonics(self) :
        return self.harmonics    
    def set_harmonics(self,harmonics=1) :
        self.harmonics=harmonics
    def get_samples(self):
        return self.samples
    def set_samples(self,samples):
        self.samples=samples

    def vibration(self,t):
        a,f,p,harmonics=self.mag,self.freq,self.phase,self.harmonics
        p_to_r=radians(p)
        sum=a*sin(2*pi*f*t)-p_to_r
        for h in range(2,harmonics+1) :
            if  self.harmo_odd_even==1  :
                sum=sum+(a*1.0/h)*sin(2*pi*(f*h)*t-p_to_r)
            elif  self.harmo_odd_even==2 and h%2==1 :
                sum=sum+(a*1.0/h)*sin(2*pi*(f*h)*t-p_to_r)
        return sum
    
    def generate(self,period=2):
        del self.signal[0:]
        del self.signal1[0:]
        echantillons=range(int(self.samples)+1)
        echantillons1=range(int(self.samples)+1)
        Tech=period/self.samples
        for t in echantillons :
            self.signal.append([t*Tech,self.vibration(t*Tech)])
        for t1 in echantillons1 :
            self.signal1.append([t1*Tech,self.vibration(t1*Tech)])
        self.notify()
        return self.signal

if   __name__ == "__main__" :
    root=tk.Tk()
    root.title("Osciloscope")
    simulator=Generator()
    signal = simulator.generate()
    print(signal)

