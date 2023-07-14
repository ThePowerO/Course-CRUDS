from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

from PIL import ImageTk, Image

#Couleurs
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

#Création des Frames
frame_logo = Frame(fenêtre, width=850, height=52, background=co6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(fenêtre, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680)

frame_données = Frame(fenêtre, width=850, height=65, background=co1)
frame_données.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(fenêtre, orient=HORIZONTAL).grid(row=3, columnspan=1, ipadx=680)

frame_détails = Frame(fenêtre, width=850, height=200, background=co1)
frame_détails.grid(row=4, column=0, pady=0, padx=10, sticky=NSEW)

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
    # Création des Frames Cours et Tableaus
    frame_tableau_cours = Frame(frame_table, width=300, height=200, bg=co1)
    frame_tableau_cours.grid(row=0, column=0, pady=0, padx=10, sticky=NSEW)

    frame_ligne = Frame(frame_table, width=30, height=200, bg=co1)
    frame_ligne.grid(row=0, column=1, pady=0, padx=10, sticky=NSEW)

    frame_tableau_classes = Frame(frame_table, width=300, height=200, bg=co1)
    frame_tableau_classes.grid(row=0, column=2, pady=0, padx=10, sticky=NSEW)

    l_nom = Label(frame_détails, text="Nom du Cours:", font=("Ivy 11"), anchor=NW,height=1, bg=co1, fg=co4)
    l_nom.place(x=14, y=10)
    nom_cours = Entry(frame_détails, width=35, justify='left', relief="solid")
    nom_cours.place(x=14, y=40)

    l_durée = Label(frame_détails, text="Durée:", font=("Ivy 11"), anchor=NW,height=1, bg=co1, fg=co4)
    l_durée.place(x=14, y=70)
    durée = Entry(frame_détails, width=19, justify='left', relief="solid")
    durée.place(x=14, y=100)

    l_prix = Label(frame_détails, text="Prix:", font=("Ivy 11"), anchor=NW,height=1, bg=co1, fg=co4)
    l_prix.place(x=14, y=130)
    prix = Entry(frame_détails, width=11, justify='left', relief="solid")
    prix.place(x=14, y=160)

    bouton_sauver1 = Button(frame_détails, anchor=CENTER, text="Sauver".upper(), width=10, overrelief=RIDGE, font=("Ivy 7 bold"), bg=co3, fg=co1)
    bouton_sauver1.place(x=100, y=160)

    bouton_update1 = Button(frame_détails, anchor=CENTER, text="Update".upper(), width=10, overrelief=RIDGE, font=("Ivy 7 bold"), bg=co6, fg=co1,)
    bouton_update1.place(x=180, y=160)

    bouton_supprimer1 = Button(frame_détails, anchor=CENTER, text="Supprimer".upper(), width=10, overrelief=RIDGE, font=("Ivy 7 bold"), bg=co7, fg=co1,)
    bouton_supprimer1.place(x=260, y=160)

    # Table Cours
    def montrer_cours():
        app_nom = Label(frame_tableau_cours, text="Tableau du Cours", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        app_nom.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        # créer une arborescence avec deux barres de défilement
        list_header = ['ID','Cours','Durée','Prix']

        df_list = []

        global tree_curso

        tree_curso = ttk.Treeview(frame_tableau_cours, selectmode="extended",columns=list_header, show="headings")

        
        vsb = ttk.Scrollbar(frame_tableau_cours, orient="vertical", command=tree_curso.yview)
        
        hsb = ttk.Scrollbar(frame_tableau_cours, orient="horizontal", command=tree_curso.xview)

        tree_curso.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree_curso.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_tableau_cours.grid_rowconfigure(0, weight=12)

        hd=["nw","nw","e","e"]
        h=[30,150,80,60]
        n=0

        for col in list_header:
            tree_curso.heading(col, text=col.title(), anchor=NW)
            # ajuster la largeur de la colonne à la chaîne d'en-tête
            tree_curso.column(col, width=h[n], anchor=hd[n],)

            n+=1

        for item in df_list:
            tree_curso.insert('', 'end', values=item)

    montrer_cours()

    #Séparateur de ligne
    l_ligne = Label(frame_détails, text="h", relief=GROOVE, height=100, font=("Ivy 1"), bg=co0, fg=co0, anchor=NW)
    l_ligne.place(x=374, y=10)
    l_ligne = Label(frame_détails, text="h", relief=GROOVE, height=100, font=("Ivy 1"), bg=co1, fg=co0, anchor=NW)
    l_ligne.place(x=372, y=10)

    l_ligne = Label(frame_tableau_ligne, text="h", relief=GROOVE, height=140, font=("Ivy 1"), bg=co0, fg=co0, anchor=NW)
    l_ligne.place(x=6, y=10)
    l_ligne = Label(frame_tableau_ligne, text="h", relief=GROOVE, height=140, font=("Ivy 1"), bg=co1, fg=co0, anchor=NW)
    l_ligne.place(x=4, y=10)

    #Détails du Classes
    l_nom = Label(frame_détails, text="Nom du Classes:", font=("Ivy 10"), anchor=NW,height=1, bg=co1, fg=co4)
    l_nom.place(x=404, y=10)
    e_nom_classe = Entry(frame_détails, width=35, justify='left', relief="solid")
    e_nom_classe.place(x=407, y=40)

    l_classe = Label(frame_détails, text="Cours", height=1, anchor=NW, font=("Ivy 10"),bg=co1, fg=co4)
    l_classe.place(x=404, y=70)

    les_cours = ["cours 1", "cours 2"]
    cours = []

    for i in les_cours:
        cours.append(i)

    c_cours = ttk.Combobox(frame_détails, width=20, font=("Ivy 8 bold"))
    c_cours["values"] = (cours)
    c_cours.place(x=407, y=100)

    l_date_initiale = Label(frame_détails, text="Date initiale:", font=("Ivy 10"), anchor=NW,height=1, bg=co1, fg=co4)
    l_date_initiale.place(x=406, y=130)
    date_initiale = DateEntry(frame_détails, width=10, background="darkblue", foreground='white', borderwidth=2, year=2023)
    date_initiale.place(x=407, y=160)

    bouton_sauver2 = Button(frame_détails, anchor=CENTER, text="Sauver".upper(), width=10, overrelief=RIDGE, font=("Ivy 7"), bg=co3, fg=co1)
    bouton_sauver2.place(x=507, y=160) 

    bouton_update2 = Button(frame_détails, anchor=CENTER, text="Update".upper(), width=10, overrelief=RIDGE, font=("Ivy 7"), bg=co6, fg=co1,)
    bouton_update2.place(x=587, y=160)

    bouton_supprimer2 = Button(frame_détails, anchor=CENTER, text="Supprimer".upper(), width=10, overrelief=RIDGE, font=("Ivy 7"), bg=co7, fg=co1,)
    bouton_supprimer2.place(x=667, y=160)

    # Tableau du Classes
    def montrer_classes():
        app_nom = Label(frame_tableau_classes, text="Tableau du Cours", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        app_nom.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)


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
ajouter_img = ImageTk.PhotoImage(ajouter_img)
bouton_ajouter = Button(frame_donnés, command=lambda:contrôle("Ajouter"), image=add_img, text="Ajouter", width=100, compound=LEFT, overrelief=RIDGE, font=("Ivy 11"), bg=co1, fg=co0)
bouton_ajouter.place(x=123, y=30)

sauver_img = Image.open('save.png')
sauver_img = sauver_img.resize((18,18))
sauver_img = ImageTk.PhotoImage(sauver_img)
bouton_sauver = Button(frame_donnés, command=lambda:contrôle("Sauver"), image=sauver_img, text="Sauver", width=100, compound=LEFT, overrelief=RIDGE, font=("Ivy 11"), bg=co1, fg=co0)
bouton_sauver.place(x=236, y=30)

fenêtre.mainloop()
