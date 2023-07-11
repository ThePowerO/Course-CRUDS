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

Style = Style(fenêtre)
Style.theme_use('clam')

frame_logo = Frame(fenêtre, width=850, height=52, background=co6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(fenêtre, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680)

frame_données = Frame(fenêtre, width=850, height=62, background=co1)
frame_données.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(fenêtre, orient=HORIZONTAL).grid(row=3, columnspan=1, ipadx=680)

frame_détails = Frame(fenêtre, width=850, height=200, background=co1)
frame_détails.grid(row=4, column=0, pady=0, padx=0, sticky=NSEW)

frame_table = Frame(fenêtre, width=850, height=200, background=co1)
frame_table.grid(row=5, column=0, pady=0, padx=10, sticky=NSEW)

logo_img = Image.open('logo.png')
logo_img = logo_img.resize((50,50))
logo_img = ImageTk.PhotoImage(logo_img)
frame_logo = Label(frame_logo, image=logo_img, text="Inscription des étudiants", width=850, compound=LEFT, relief=RAISED, anchor=NW, font=("Ivy 15 bold"), bg=co6, fg=co1)
frame_logo.place(x=0, y=0)

def étudiants():
    print("Étudiant")
    
def ajouter():
    print("Cours et Classes")

def sauver():
    print("Sauver")

def contrôle(i):
    if i == 'Inscription':
        for widget in frame_détails.winfo_children():
            widget.destroy()

        for widget in frame_table.winfo_children():
            widget.destroy()

        étudiants()

    if i == 'Ajouter':
        for widget in frame_détails.winfo_children():
            widget.destroy()

        for widget in frame_table.winfo_children():
            widget.destroy()

        ajouter()
        
    if i == 'Sauver':
        for widget in frame_détails.winfo_children():
            widget.destroy()

        for widget in frame_table.winfo_children():
            widget.destroy()

        sauver()

add_img = Image.open('add.png')
add_img = add_img.resize((18,18))
add_img = ImageTk.PhotoImage(add_img)
bouton_register = Button(frame_donnés, command=lambda:contrôle("Inscription"), image=add_img, text="Inscription", width=100, compound=LEFT, overrelief=RIDGE, font=("Ivy 11"), bg=co1, fg=co0)
bouton_register.place(x=10, y=30)

ajouter_img = Image.open('add.png')
ajouter_img = ajouter_img.resize((18,18))


fenêtre.mainloop()
