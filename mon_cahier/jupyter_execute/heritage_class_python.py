#!/usr/bin/env python
# coding: utf-8

# # Héritage
# 
# Sources :
# https://www.programiz.com/python-programming/inheritance
# 
# 
# L'héritage permet de définir une classe qui va reprendre toutes les fonctionnalités d'une classe parente et nous permettre d'en ajouter davantage.
# 
# La classe parente (ou base / super-classe) n’est pas modifiée par le processus de création de la classe enfant (ou dérivée).
# 
# Les classes parentes ne sont pas instanciables.
# 
# 
# 

# In[15]:


class Animal():
    
    def __init__(self):
        pass

    def dire_nom(self):
        print(f"Je m’appelle {self.name}.")

    def crier(self, x):
        print(x*3)


# On crée une classe fille à la classe Animal :

# In[22]:


class Chien(Animal):
    
    def __init__(self, name):
        self.name = name
    
    def abboyer(self):
        super().crier("Woof ! ")

chien = Chien("Rex")

chien.dire_nom()
chien.abboyer()


# Dans cet exemple on veut créer une classe chien, mais il est pertinent de créer une super-classe animal.
# 
# De cette façon, on peut profiter des fonctionnalités de la classe animal dans diverses classes dérivées qui correspondront à d'autres espèces ayant en plus leurs propres fonctionnalités.

# `    def cri(self):
#         super().cri("Woof! ")
# `
# 
# Ici, super() est une référence implicite à la classe mère. À ce titre, cela vous dispense d'utiliser le self lors de l'appel.

# Il est possible pour une classe dérivée d'hériter de plusieurs parents, on l'écrit ainsi :

# In[23]:


class Chihuahua (Chien):
    def __init__ (self,name):
        self.name = name
        self.race = "Chihuahua"
        self.cri = "Wif ! "
    
    def decrire(self):
        print("Je suis petit et très méchant.")

roquet = Chihuahua("Quentin")
roquet.dire_nom()
roquet.crier(roquet.cri)
roquet.decrire()


# Chihuahua est donc une classe dérivée de la classe Chien elle-même dérivée de la classe Animal.
