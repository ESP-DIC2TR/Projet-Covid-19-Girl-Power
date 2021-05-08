from tkinter import*
#nous permet de parcourir les fichiers dont on a besoin pour mettre au niveau de l'interface graphique 
from tkinter.filedialog import askopenfilename
#pour gerer les librairies ou fenetres d'erreurs et afficher les messages d'information
from tkinter.messagebox import showerror, showinfo
from tkinter import Tk, BooleanVar, Label, Checkbutton
from tkinter import Tk, StringVar, Label, Checkbutton
from functools import partial
import pandas as panda
import PIL
import pytesseract
from pdf2image import*
from pprint import pprint
import json

from pdf2image import convert_from_path,convert_from_bytes
from pdf2image.exceptions import (
PDFInfoNotInstalledError,
PDFPageCountError,
PDFSyntaxError
)
import os
#os.listdir("C:\\Users\\hp\\Desktop\\DIC 2_TR\\SGBD\\Python\\Telechargementpy")
folder_path = "C:\\Users\\hp\\Desktop\\DIC 2_TR\\SGBD\\Python\\Telechargementpy"

for path, dirs, files in os.walk(folder_path):
    for filename in files:
        print(filename)

#dataframe=panda.read_json("C:\\Users\\hp\\Desktop\\DIC 2_TR\\SGBD\\Python\\JSON", orient='columns')
#pages = pdf2image.convert_from_path("C:\\Users\\hp\\Desktop\\DIC 2_TR\\SGBD\\Python\\Telechargementpy", 500)

  

#data=panda.read_pdf('communiquen0.pdf')

#data.head(20)
#creons une premiere fenetre


#fen.geometry("300*320+300+150")
#fen.title("Interface")

#l=Label(fen, text="L'ensemble de nos communiqués sont repartis comme suit:")
#l.pack()
#affichage
#fen.mainloop()
#parcourir=Button(cntenu, text="Pr",command=parcourir)


   


#def update_label(label, var):
    
    #Met à jour le texte d'un label en utilisant un BooleanVar.
    
 #   text = var.get()
  #  label.config(text=str(text))

#root = Tk()
#is_checked = BooleanVar(root, '1')
#label = Label(root, text=str(is_checked.get()))
#checkbox = Checkbutton(root, variable=is_checked, 
                    #   command=partial(update_label, label,
                     #                  is_checked))

#label.grid(row=0, column=0)
#checkbox.grid(row=1, column=0)
#root.mainloop()



def update_label(label, var):
    """
    Met à jour le texte d'un label en utilisant un BooleanVar.
    """
    text = var.get()
    label.config(text=text)


root = Tk()
is_red = StringVar(root, 'red')
label = Label(root, text=is_red.get())
checkbox = Checkbutton(root, variable=is_red, onvalue='red', offvalue='white', command=partial(update_label, label, is_red))

label.grid(row=0, column=0)
checkbox.grid(row=1, column=0)
root.mainloop()