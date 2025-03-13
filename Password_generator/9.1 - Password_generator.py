import string
from random import randint, choice
from tkinter import *

def generate_password():
    password_min = 8
    password_max = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits 

    password = "".join(choice(all_chars)for x in range(randint(password_min, password_max)))
    password_entry.delete(0, END) # Supprime le contenu du champ de saisie
    password_entry.insert(0, password) # Insertion du mot de passe dans le champ de saisie
        

# Créer une fenêtre
window = Tk()
window.title("Générateur de mot de passe")
window.geometry("720x480")
window.iconbitmap("L.ico")
window.config(bg="grey")

# Créer une frame principale
frame = Frame(window, 
              bg="grey")


# Création d'une image
# Canva : zone dans laquelle on va dessiner une image
width = 500
height = 600
image = PhotoImage(file="mdp.png").zoom(35).subsample(32)
# canvas : # Espace pour dessiner des éléments graphiques
canvas = Canvas(frame,
                width=width,
                height=height,
                bg="grey",
                bd=0,
                highlightthickness=0
                ) 
canvas.create_image(width/2,
                    height/2,
                    image=image
                    )
canvas.grid(row=0, column=0, sticky=W)

# Créer une sous boite
right_frame = Frame(frame, bg="grey")

# Création d'un titre
label_title = Label(right_frame, 
                    text="Mot de passe",
                    font=("Helvetica", 20),
                    bg="grey",
                    fg="white")
#label_title.grid(row=0, 
#                column=2, 
#                sticky=W)
label_title.pack() 

# Création d'un champ de saisie (entrée/input)
password_entry = Entry(right_frame,
                       font=("Helvetica", 20),
                        bg="grey",
                        )
password_entry.pack()

# Création d'un bouton
generate_button = Button(right_frame,
       font=("Helvetica", 20),
       text="Générer",
       bg="grey",
       fg="white",
       command=generate_password
       )
generate_button.pack()

# Place la sous-boite à droite de la frame principale
right_frame.grid(row=0, column=1, sticky=W)
# Afficher la frame
frame.pack(expand=YES)

# Création d'un menu
menu_bar = Menu(window)
#Création d'un premier menu
file_menu = Menu(menu_bar, tearoff=0)#Pour ne pas avoir de tiret
file_menu.add_command(label="Nouveau", command=generate_password)
file_menu.add_command(label="Quitter", command=window.quit) # Ferme la fenêtre
menu_bar.add_cascade(label="Cliquez-ici", menu=file_menu)

#Configurer la fenêtre pour ajouter le menu
window.config(menu=menu_bar)

#Affichage de la fenêtre
window.mainloop()

