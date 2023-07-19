from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

from PIL import ImageTk, Image

from tkcalendar import Calendar, DateEntry
from datetime import date

from view import *

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

    def noveau_étudiants():
        global image, image_string, l_image

        nom = e_nom.get()
        email = e_email.get()
        téléphone = e_téléphone.get()
        genre = c_sexe.get()
        naissance = date_naissance.get()
        cpf = e_cpf.get()
        cours = c_classes.get()
        image = image_string

        liste = [nom, email, téléphone, genre, image, naissance, cpf, cours]
        
        for i in liste:
            if i == "":
                messagebox.showerror("Erreur", "Il faut remplir l'espace")
                return

        créer_étudiants(liste)

        messagebox.showinfo("Succès", "Tu rempli tout avec succès")

        e_nom.delete(0,END)
        e_email.delete(0,END)
        c_sexe.delete(0,END)
        date_naissance.delete(0,END)
        e_cpf.delete(0,END)
        c_classes.delete(0,END)

        montrer_étudiant()
    
    l_nom = Label(frame_détails, text="Nom:", font=("Ivy 10"), anchor=NW,height=1, bg=co1, fg=co4)
    l_nom.place(x=4, y=10)
    e_nom = Entry(frame_détails, width=45, justify='left', relief="solid")
    e_nom.place(x=7, y=40)
    
    l_email = Label(frame_détails, text="Email:", font=("Ivy 10"), anchor=NW,height=1, bg=co1, fg=co4)
    l_email.place(x=4, y=70)
    e_email = Entry(frame_détails, width=45, justify='left', relief="solid")
    e_email.place(x=7, y=100)

    l_téléphone = Label(frame_détails, text="Téléphone:", font=("Ivy 10"), anchor=NW,height=1, bg=co1, fg=co4)
    l_téléphone.place(x=4, y=130)
    c_téléphone = Entry(frame_détails, width=20, justify='left', relief="solid")
    c_téléphone.place(x=7, y=160)

    l_sexe = Label(frame_détails, text="Sexe:", font=("Ivy 10"), anchor=NW,height=1, bg=co1, fg=co4)
    l_sexe.place(x=190, y=130)
    c_sexe = ttk.Combobox(frame_détails, width=12, font=("Ivy 8 bold"))
    c_sexe["values"] = ("Masculin", "Feminine")
    c_sexe.place(x=190, y=160)

    l_date_naissance = Label(frame_détails, text="Date de Naissance:", font=("Ivy 10"), anchor=NW,height=1, bg=co1, fg=co4)
    l_date_naissance.place(x=446, y=10)
    date_naissance = DateEntry(frame_détails, width=18, background="darkblue", foreground='white', borderwidth=2, year=2023)
    date_naissance.place(x=450, y=40)

    l_cpf = Label(frame_détails, text="CPF:", font=("Ivy 10"), anchor=NW,height=1, bg=co1, fg=co4)
    l_cpf.place(x=446, y=70)
    e_cpf = Entry(frame_détails, width=20, justify='left', relief="solid")
    e_cpf.place(x=450, y=100)

    les_classes = ["Classe A Python", "Classe B HTML"]
    classe = []

    for i in les_classes:
        classe.append(i)

    l_classes = Label(frame_détails, text="Classe:", font=("Ivy 10"), anchor=NW,height=1, bg=co1, fg=co4)
    l_classes.place(x=446, y=130)
    c_classes = ttk.Combobox(frame_détails, width=20, font=("Ivy 8 bold"))
    c_classes["values"] = (classe)
    c_classes.place(x=450, y=160)

    global image, image_string, l_image
    
    def choisir_image():
        global image, image_string, l_image
        image = fd.askopenfilename()
        image_string = image

        image = Image.open(image)
        image = image.resize((130,130))
        image = ImageTk.PhotoImage(image)
        l_image = Label(frame_détails, image=image, bg=co1, fg=co4)
        l_image.place(x=300, y=10)

        bouton_charger['text'] = "Chenger Image"

    bouton_charger = Button(frame_détails, command=choisir_image, text="Charger Image".upper(), width=20, compound=CENTER, overrelief=RIDGE, anchor=CENTER, font=("Ivy 7"), bg=co1, fg=co0)
    bouton_charger.place(x=300, y=160)

    l_ligne = Label(frame_détails, text="h", relief=GROOVE, height=100, font=("Ivy 1"), bg=co0, fg=co0, anchor=NW)
    l_ligne.place(x=610, y=10)
    l_ligne = Label(frame_détails, text="h", relief=GROOVE, height=100, font=("Ivy 1"), bg=co1, fg=co0, anchor=NW)
    l_ligne.place(x=608, y=10)

    l_nom1 = Label(frame_détails, text="Rechercer étudient", font=("Ivy 10"), anchor=NW, height=1, bg=co1, fg=co4)
    l_nom1.place(x=627, y=10)
    e_nom_rechercher = Entry(frame_détails, width=17, justify='center', relief="solid", font=("Ivy 10"))
    e_nom_rechercher.place(x=630, y=35)

    bouton_rechercher = Button(frame_détails, anchor=CENTER, text="Rechercher", width=9, overrelief=RIDGE, font=("Ivy 7 bold"), bg=co2, fg=co0)
    bouton_rechercher.place(x=757, y=35)

    bouton_sauver2 = Button(frame_détails, command=noveau_étudiants, anchor=CENTER, text="Sauver".upper(), width=9, overrelief=RIDGE, font=("Ivy 7 bold"), bg=co3, fg=co1)
    bouton_sauver2.place(x=627, y=110) 

    bouton_update2 = Button(frame_détails, anchor=CENTER, text="Update".upper(), width=9, overrelief=RIDGE, font=("Ivy 7 bold"), bg=co6, fg=co1,)
    bouton_update2.place(x=627, y=135)

    bouton_supprimer2 = Button(frame_détails, anchor=CENTER, text="Supprimer".upper(), width=9, overrelief=RIDGE, font=("Ivy 7 bold"), bg=co7, fg=co1,)
    bouton_supprimer2.place(x=627, y=160)

    bouton_voir = Button(frame_détails, anchor=CENTER, text="Voir".upper(), width=9, overrelief=RIDGE, font=("Ivy 7 bold"), bg=co1, fg=co0,)
    bouton_voir.place(x=727, y=160)

    def montrer_étudiant():
        app_nom = Label(frame_table, text="Tableau des estudantes", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        app_nom.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        list_header = ['id', 'Nom', 'email', 'Telefone','sexo', 'imagem', 'Data', 'CPF', 'Curso']

        df_list = voir_étudiants()

        global tree_étudiants

        tree_étudiants = ttk.Treeview(frame_table, selectmode="extended",columns=list_header, show="headings")

        vsb = ttk.Scrollbar(frame_table, orient="vertical", command=tree_étudiants.yview)
        hsb = ttk.Scrollbar(frame_table, orient="horizontal", command=tree_étudiants.xview)

        tree_étudiants.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree_étudiants.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_table.grid_rowconfigure(0, weight=12)

        hd=["nw","nw","nw","center","center","center","center","center","center"]
        h=[40,150,150,70,70,70,80,80,100]
        n=0

        for col in list_header:
            tree_étudiants.heading(col, text=col.title(), anchor=NW)
            tree_étudiants.column(col, width=h[n],anchor=hd[n])

            n+=1

        for item in df_list:
            tree_étudiants.insert('', 'end', values=item)

    montrer_étudiant()

def ajouter():
    # Création des Frames Cours et Tableaus
    frame_tableau_cours = Frame(frame_table, width=300, height=200, bg=co1)
    frame_tableau_cours.grid(row=0, column=0, pady=0, padx=10, sticky=NSEW)

    frame_ligne = Frame(frame_table, width=30, height=200, bg=co1)
    frame_ligne.grid(row=0, column=1, pady=0, padx=10, sticky=NSEW)

    frame_tableau_classes = Frame(frame_table, width=300, height=200, bg=co1)
    frame_tableau_classes.grid(row=0, column=2, pady=0, padx=10, sticky=NSEW)

    #Détails du Cours
    def noveau_cours():
        nom = e_nom_cours.get()
        durée = e_durée.get()
        prix = e_prix.get()
        
        liste = [nom, durée, prix]

        for i in liste:
            if i == "":
                messagebox.showerror("Erreur", "Il faut remplir l'espace")
                return

        créer_course(liste)

        messagebox.showinfo("Succès", "Succès")

        e_nom_cours.delete(0,END)
        e_durée.delete(0,END)
        e_prix.delete(0,END)

        montrer_cours()

    def update_cours():
        try:
            tree_itens = tree_cours.focus()
            tree_dictionnaire = tree_cours.item(tree_itens)
            tree_liste = tree_dictionnaire['values']

            valeur_id = tree_liste[0]

            e_nom_cours.insert(0, tree_liste[1])
            e_durée.insert(0, tree_liste[2])
            e_prix.insert(0, tree_liste[3])

            def update():
                nom = e_nom_cours.get()
                durée = e_durée.get()
                prix = e_prix.get()

                liste = [nom, durée, prix, valeur_id]

                for i in liste:
                    if i == "":
                        messagebox.showerror("Erreur", "Il faut remplir l'espace")
                        return

                update_course(liste)

                messagebox.showinfo("Succès", "Tu rempli tout avec succès")

                e_nom_cours.delete(0,END)
                e_durée.delete(0,END)
                e_prix.delete(0,END)

                montrer_cours()

                bouton_sauver1.destroy()

            bouton_sauver1 = Button(frame_détails, command=update, anchor=CENTER, text="Sauver".upper(), width=10, overrelief=RIDGE, font=("Ivy 7"), bg=co3, fg=co1)
            bouton_sauver1.place(x=227, y=130) 

        except IndexError:
            messagebox.showerror("Erreur", "Sélectionnez l'un des cours du tableau")

    def supprimer_cours():
        try:
            tree_itens = tree_cours.focus()
            tree_dictionnaire = tree_cours.item(tree_itens)
            tree_liste = tree_dictionnaire['values']

            valeur_id = tree_liste[0]

            supprimer_course([valeur_id])

            messagebox.showinfo("Succès", "Les donnés ont été supprimé avec succès")

            montrer_cours()

        except IndexError:
            messagebox.showerror("Erreur", "Sélectionnez l'un des cours du tableau")


    l_nom = Label(frame_détails, text="Nom du Cours:", font=("Ivy 11"), anchor=NW,height=1, bg=co1, fg=co4)
    l_nom.place(x=4, y=10)
    nom_cours = Entry(frame_détails, width=35, justify='left', relief="solid")
    nom_cours.place(x=7, y=40)

    l_durée = Label(frame_détails, text="Durée:", font=("Ivy 11"), anchor=NW,height=1, bg=co1, fg=co4)
    l_durée.place(x=4, y=70)
    durée = Entry(frame_détails, width=19, justify='left', relief="solid")
    durée.place(x=7, y=100)

    l_prix = Label(frame_détails, text="Prix:", font=("Ivy 11"), anchor=NW,height=1, bg=co1, fg=co4)
    l_prix.place(x=4, y=130)
    prix = Entry(frame_détails, width=11, justify='left', relief="solid")
    prix.place(x=7, y=160)

    bouton_sauver1 = Button(frame_détails, command=noveau_cours, anchor=CENTER, text="Sauver".upper(), width=10, overrelief=RIDGE, font=("Ivy 7 bold"), bg=co3, fg=co1)
    bouton_sauver1.place(x=107, y=160)

    bouton_update1 = Button(frame_détails, command=update_cours, anchor=CENTER, text="Update".upper(), width=10, overrelief=RIDGE, font=("Ivy 7 bold"), bg=co6, fg=co1,)
    bouton_update1.place(x=187, y=160)

    bouton_supprimer1 = Button(frame_détails, command=supprimer_cours, anchor=CENTER, text="Supprimer".upper(), width=10, overrelief=RIDGE, font=("Ivy 7 bold"), bg=co7, fg=co1,)
    bouton_supprimer1.place(x=267, y=160)

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

    def noveau_classe():
        nom = e_nom_classe.get()
        cours = c_cours.get()
        date = e_date_initiale.get()

        liste = [nom, cours, date]

        for i in liste:
            if i == "":
                messagebox.showerror("Erreur", "Il faut remplir l'espace")
                return

        crée_class(liste)

        messagebox.showinfo("Succès", "Tu rempli tout avec succès")

        e_nom_classe.delete(0,END)
        c_cours.delete(0,END)
        e_date_initiale.delete(0,END)

        montrer_classes()

    def update_classe():
        try:
            tree_itens = tree_classe.focus()
            tree_dictionnaire = tree_classe.item(tree_itens)
            tree_liste = tree_dictionnaire['values']

            valeur_id = tree_liste[0]

            e_nom_classe.insert(0, tree_liste[1])
            c_cours.insert(0, tree_liste[2])
            e_date_initiale.insert(0, tree_liste[3])

            def update():
                nom = e_nom_classe.get()
                cours = c_cours.get()
                date = e_date_initiale.get()

                liste = [nom, cours, date, valeur_id]

                for i in liste:
                    if i == "":
                        messagebox.showerror("Erreur", "Il faut remplir l'espace")
                        return
                        
                update_classes(liste)

                messagebox.showinfo("Succès", "Tu rempli tout avec succès")

                e_nom_classe.delete(0,END)
                c_cours.delete(0,END)
                e_date_initiale.delete(0,END)

                montrer_classes()

                bouton_sauver1.destroy()

            bouton_sauver1 = Button(frame_détails, command=update, anchor=CENTER, text="Sauver".upper(), width=10, overrelief=RIDGE, font=("Ivy 7"), bg=co3, fg=co1)
            bouton_sauver1.place(x=407, y=130) 

        except IndexError:
            messagebox.showerror("Erreur", "Sélectionnez l'un des classe du tableau")

    def supprimer_classe():
        try:
            tree_itens = tree_classe.focus()
            tree_dictionnaire = tree_classe.item(tree_itens)
            tree_liste = tree_dictionnaire['values']

            valeur_id = tree_liste[0]

            supprimer_classes([valeur_id])

            messagebox.showinfo("Succès", "Les donnés ont été supprimé avec succès")

            montrer_classes()

        except IndexError:
            messagebox.showerror("Erreur", "Sélectionnez l'un des   du tableau")

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

    bouton_sauver2 = Button(frame_détails, command=noveau_classe, anchor=CENTER, text="Sauver".upper(), width=10, overrelief=RIDGE, font=("Ivy 7"), bg=co3, fg=co1)
    bouton_sauver2.place(x=507, y=160) 

    bouton_update2 = Button(frame_détails, command=update_classe, anchor=CENTER, text="Update".upper(), width=10, overrelief=RIDGE, font=("Ivy 7"), bg=co6, fg=co1,)
    bouton_update2.place(x=587, y=160)

    bouton_supprimer2 = Button(frame_détails, command=supprimer_classe, anchor=CENTER, text="Supprimer".upper(), width=10, overrelief=RIDGE, font=("Ivy 7"), bg=co7, fg=co1,)
    bouton_supprimer2.place(x=667, y=160)

    # Tableau du Classes
    def montrer_classes():
        app_nom = Label(frame_tableau_classes, text="Tableau du Cours", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        app_nom.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        # créer une arborescence avec deux barres de défilement
        list_header = ['ID','Nom du Classe','Cours','Date Initiale']

        df_list = []

        global tree_classe

        tree_classe = ttk.Treeview(frame_tableau_classes, selectmode="extended",columns=list_header, show="headings")

        vsb = ttk.Scrollbar(frame_tableau_classes, orient="vertical", command=tree_classe.yview)
        hsb = ttk.Scrollbar(frame_tableau_classes, orient="horizontal", command=tree_classe.xview)

        tree_classe.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree_classe.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_tableau_classes.grid_rowconfigure(0, weight=12)

        hd=["nw","nw","e","e"]
        h=[30,130,150,80]
        n=0

        for col in list_header:
            tree_classe.heading(col, text=col.title(), anchor=NW)
            # ajuster la largeur de la colonne à la chaîne d'en-tête
            tree_classe.column(col, width=h[n], anchor=hd[n],)
            
            n+=1

        for item in df_list:
            tree_classe.insert('', 'end', values=item)

    montrer_classes()


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
