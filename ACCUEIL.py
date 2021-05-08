
#from PIL import Image, ImageTk

import tkinter as tk
import tkinter.messagebox as mb
import random
import tkinter.ttk

import math
from tkinter.filedialog import askopenfilename

from tkinter import Tk, PhotoImage, Canvas


from tkinter import *
#from map3 import *
from Graphic import *



class Login_Success_Window(tk.Toplevel):

    def __init__(self,master):
        self.window = Tk()
        self.master=master
        self.window.title("Covid-19")
        self.window.geometry("1080x720")
        self.window.minsize(720,480)
       
        self.window.config(background='#B0E0E6')
        # initialization des composants
        self.frame0 = Frame(self.window, bg='#B0E0E6')
        self.frame1 = Frame(self.window, bg='#B0E0E6')
        self.frame11 = Frame(self.frame1, bg='#B0E0E6')
        self.frame12 = Frame(self.frame1, bg='#B0E0E6')
        self.frame2 = Frame(self.window, bg='#B0E0E6')
        # creation des composants
        self.create_widgets()

        # empaquetage
        self.frame0.pack(side=TOP,fill=X)
        self.frame1.pack(pady=150)
        self.frame11.pack()
        self.frame12.pack()
        self.frame2.pack(side=BOTTOM,fill=X)

    def create_widgets(self):
        self.create_title()
        self.create_dAcq_button()
        self.create_dloa_button()
        self.create_dexp_button()
        self.create_EA_button()
        self.help_button()
        self.exit_button()
    def create_title(self):
        label_title = Label(self.frame11, text="BIENVENUE DANS VOTRE NENU PRINCIPAL", font=("Courrier", 20), bg='white',
                            fg='black')
        label_title.pack()
    def create_dAcq_button(self):
        def khadija():
            authentifier()
        dAcq = Button(self.frame12, text="DataAcquisition", font=("Courrier", 14), bg='black', fg='white',command=khadija)
        dAcq.pack(pady=23)
        
    def create_dloa_button(self):
        def Khadija1():
            a=DataLoader(self.window)
            a.mainloop()
        dloa = Button(self.frame12, text="DataLoader", font=("Courrier", 14), bg='black', fg='white',command=Khadija1)
        dloa.pack(pady=20)





    def create_dexp_button(self):

        def Khadija2():
            b=map3(self.window)
            b.mainloop()


        dexp = Button(self.frame12, text="DataExplorer", font=("Courrier", 14), bg='black', fg='white')
        dexp.pack(pady=5)
    
    def create_EA_button(self):
        EA = Button(self.frame12, text="EvolutionAnalyser", font=("Courrier", 14), bg='black', fg='white')
        EA.pack(pady=20)



    
    def exit_button(self):
       

        ex = Button(self.frame2, text="Quitter", font=("Courrier", 14), bg='black', fg='white')

        
        ex.pack(side=RIGHT,padx=5,pady=20)    
        
    def help_button(self):
        h = Button(self.frame2, text="Aide", font=("Courrier", 14), bg='black', fg='white')
        h.pack(side=LEFT,padx=5,pady=5)  
