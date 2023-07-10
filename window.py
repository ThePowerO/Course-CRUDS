from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

from PIL import ImageTk, Image

co0 = "#2e2d2b"  # Noir
co1 = "#feffff"  # Blanc 
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Vert
co4 = "#403d3d"   # lettre
co6 = "#003452"   # Blue
co7 = "#ef5350"   # Rouge

co6 = "#038cfc"   # Blue
co8 = "#263238"   # + vert
co9 = "#e9edf5"   # + vert

fenêtre = Tk()
fenêtre.title("")
fenêtre.geometry("850x620")
fenêtre.configure(background=co1)
fenêtre.resizable(width=FALSE, height=FALSE)

frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)


Style = Style(fenêtre)
Style.theme_use('clam')

frame_logo = Frame(fenêtre, width=850, height=52, background=co6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(fenêtre, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680)

frame_données = Frame(fenêtre, width=850, height=62, background=co1)
