#!/usr/bin/env python
# coding: utf-8

# # Interfaces graphiques avec Tkinter

# ## Initialisation

# Tkinter est un module que l'on peut importer dans Python.

# In[1]:


import tkinter as tk


# Pour démarrer, il faut commencer par créer une fenêtre pour notre application.

# In[8]:


# Création de la fenêtre de l'application
root = tk.Tk()
# Définir un titre pour la fenêtre
root.title("Mon Application")
# Définir la taille de la fenêtre 
root.geometry("400x400") # mettre les pixels suivant ce pattern 0pixels x 0pixels
# Définir le style de la fenêtre
root.configure(bg="black") # bg = background

# Définir une taille minimale
root.minsize(200, 200)
# Définir une taille maximale
root.maxsize(600, 600)

# Pour afficher la fenêtre à l'utilisateur
root.mainloop()


# ## Les Widgets

# Il existe différents widgets qui permettent de remplir la fenêtre de l'application.

# ### Frame

# Une frame est un espace que l'on définit dans la fenêtre de notre application.
# La taille de la frame va dépendre des autres widgets qu'elle contient.
# 
# Définir plusieurs frames permet de segmenter le contenu de la fenêtre principale pour séparer les différents contenus.

# In[10]:


root = tk.Tk()
root.title("Mon Application")
root.geometry("400x400")
root.configure(bg="black")

# Création d'une frame qui contiendra les titres
frame_titre = tk.Frame(root, bg="red") # root est la fenêtre à laquelle la frame est rattachée

# Permet de l'insérer dans la fenêtre
frame_titre.pack()

root.mainloop()


# ### Label

# Permet d'afficher du texte.

# In[18]:


root = tk.Tk()
root.title("Mon Application")
root.geometry("400x400")
root.configure(bg="black")

frame_titre = tk.Frame(root, bg="red")
frame_titre.pack()

# On définit le texte que l'on veut afficher dans notre frame
titre = tk.Label(frame_titre, text='Je suis le titre', font=("Helvetica", 20), bg='orange', fg='white')
# text = le texte à afficher, font = définir une police particulière et sa taille, 
# bg = couleur de l'arrière plan, et fg = couleur du texte

# Il faut également lui dire de l'afficher dans la frame
titre.pack(pady=10, padx=10) 
# pady et padx sont des marges en pixels sur les axes y et x, 
# c'est-à-dire en vertical et en horizontal respectivement.
# Ces marges nous permettront de voir la couleur de la frame qui comprend notre texte.

root.mainloop()


# ### Button

# Tkinter permet la création de boutons qui permettent des interactions avec l'utilisateur.
# Il est possible d'appeler une fonction en cliquant sur le bouton.

# In[31]:


import random as rand

# Fonction utilisée sur le bouton que l'on va créé
# La fonction change le texte affiché dans le Label titre.
# La fonction prend un chiffre aléatoire entre 1 et 6 et écrit le résultat à la place 
# du titre de notre application.
def roll():
    x = rand.randint(1, 6)
    titre.configure(text=x)  


# In[32]:


root = tk.Tk()
root.title("Mon Application")
root.geometry("800x400")
root.configure(bg="black")

frame_titre = tk.Frame(root, bg="red")
frame_titre.pack()

#Nouvelle fenêtre qui contiendra les boutons
frame_bouton = tk.Frame(root, bg="black")
frame_bouton.pack()

titre = tk.Label(frame_titre, text='Cliquez sur le bouton pour lancer le dé.', font=("Helvetica", 20), bg='orange', fg='white')
titre.pack(pady=10, padx=10) 

# Création du bouton
bouton = tk.Button(frame_bouton, text='Lancer le dé', height=5, width=20, bd=0)
# height = permet de définir la hauteur du bouton, width = définir la largeur, 
# bd = pour lui dire que l'on veut un bouton sans bordure,
# command = permet de lui indiquer une fonction a exécuter lorsque l'utilisateur clique sur le bouton

# Il est possible de modifier les propriétés d'un bouton pour lui ajouter une commande
bouton.configure(command=roll) # la fonction appelée ne prend pas d'arguments donc pas de ()

# Afficher le bouton dans la frame
bouton.pack()

root.mainloop()


# ### Entry

# Une Entry correspond à un champ de saisie qui permet à l'utilisateur de spécifier une variable qui sera utilisée dans notre application après.

# In[42]:


def roll_x():
    # on défini la borne supérieure pour le lancer aléatoire
    # on lui indique que la borne supérieure correspond à la valeur saisie par l'utilisateur
    x = rand.randint(1, int(saisi.get()))
    titre.configure(text=x)  

root = tk.Tk()
root.title("Mon Application")
root.geometry("800x400")
root.configure(bg="black")

frame_titre = tk.Frame(root, bg="red")
frame_titre.pack()

frame_bouton = tk.Frame(root, bg="black")
frame_bouton.pack()

titre = tk.Label(frame_titre, text='Cliquez sur le bouton pour lancer le dé.', font=("Helvetica", 20), bg='orange', fg='white')
titre.pack(pady=10, padx=10) 

bouton = tk.Button(frame_bouton, text='Lancer le dé', height=5, width=20, bd=0)
bouton.configure(command=roll_x)
bouton.pack()

# On créé une entry pour que l'utilisateur ait un choix de nombre maximum pour le dé
saisi = tk.Entry(frame_bouton, width=10, justify="center", font=("Helvetica", 10), bg="white", fg="black")
# justify = permet de définir comment le texte est justifié, soit "center", "left", "right"
# par défaut le texte est justifié à gauche

# Afficher l'entry dans la fenêtre
saisi.pack()

root.mainloop()


# ## Les méthodes d'affichage

# ### Pack

# `pack` permet d'ajouter le widget directement dans une fenêtre à l'endroit où il y a de la place.  
# Il existe plusieurs paramètres permettant de configurer le `pack`.

# ```python
# .pack(expand="YES") # permet de prendre la largeur entière de la frame dans laquelle le widget se situe
# .pack(fill="x") # permet de faire un expand mais uniquement en x
# .pack(fill="y") # permet de faire un expand mais uniquement en y
# 
# .pack(pady=10) # permet de définir une marge externe à l'objet horizontale
# .pack(padx=10) # permet de définir une marge externe à l'objet verticale
# 
# .pack(ipady=10) # permet de définir une marge interne à l'objet horizontale
# .pack(ipadx=10) # permet de définir une marge interne à l'objet verticale
# 
# .pack(side="top") # permet de définir la position d'affichage (left, right, top, bottom)
# ```

# ### Grid

# `grid` permet de faire la même chose que `pack` mais cette fois en suivant une logique de quadrillage.
# Il faudra donc indiquer sur quelle ligne et sur quelle colonne afficher le widget.

# ```python
# .grid(row=0, column=0) # la première ligne est 0, de même pour la première colonne
# 
# .grid(padx=10, pady=10) # même chose que pour pack
# .grid(ipadx=10, ipady=10) # même chose que pour pack
# 
# .grid(sticky="n") # permet d'afficher en fonction d'une orientation ("n", "s", "w", "e", "ne", "se", "nw", "sw")
# 
# .grid(columnspan=5) # permet de définir sur combien de colonnes s'étend le widget, par défaut columnspan=1
# .grid(rowspan=5) # permet de définir sur combien de lignes s'étend le widget, par défaut rowspan=1
# ```
