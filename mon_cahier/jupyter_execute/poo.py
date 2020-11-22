#!/usr/bin/env python
# coding: utf-8

# # Programmation Orientée Objet
# 
# ## Définition
# 
# Citation de Steve Job :
# [Article sur Developpez.com](https://www.developpez.com/actu/91705/Comment-pourriez-vous-expliquer-l-oriente-objet-Steve-Jobs-a-essaye-d-expliquer-ce-concept/)
# 
# ## Les objets dans Python
# 
# Un objet est composé d'une classe est d'une instance. La classe est le code qui permet de créer l'objet. Elle se déclare, un peu comme une fonction, mais le code n'est pas éxécuté. Les instances sont des variables qui permettent de manipuler les objets dans le code. En python :
# 
# - une classe se déclare ainsi : `class Nom_classe :`. 
# - une instance se créée en initialisant une variable avec un constructeur : `var1 = Nom_classe()`
# 
# Le constructeur est le nom de la classe suivi de ().

# In[22]:


#déclaration d'une classe, qui est le modèle pour les objets
class Monty:
    pass

#fonction main() pour le programme principal
def main():
    #création d'instances de classe Monty, qui permet la manipulation d'objets créés à partir de cette classe
    monty1 = Monty()
    monty2 = Monty()

    #Les variables contiennent les espaces mémoires des objets
    print(monty1)
    print(monty2)

main()


# A partir d'une classe, il est possible de créer autant d'instances que besoin. Dans le code au-dessus, les deux instances *monty1* et *monty2* sont créées à partir de la classe *Monty*. Bien que tous les deux de type *Monty*, ils sont deux objets différents.

# ## Constructeur
# 
# Le constructeur retourne l'espace mémoire atttribué à l'objet. C'est ce qui permet de manipuler l'objet dans le code. A chaque création d'une instance, un espace mémoire différent est alloué. C'est ainsi que le compilateur fait la différence entre plusieurs instances de même classe.
# 
# Il est possible de surcharger le constructeur pour exécuter du code à la création de l'objet. En général, cela sert à initialiser certaines valeurs. Pour cela, il faut mettre ce code dans la fonction `__init__(self) :`, définie dans la classe elle-même.Attention, puisque le constructeur retourne l'emplacement mémoire de l'objet, il ne peut retrouner rien d'autre. **Il n'y a jamais de `return`dans un constructeur**.

# In[23]:


class Monty:
    #surcharge du constructeur
    def __init__(self):
        #self est l'objet lui-même
        print(self)
        #initialisation d'une variable d'instance "metier"
        self.metier = "comédien"

#fonction main() pour le programme principal
def main() :
    #instanciation de 2 objets de type Monty
    monty1 = Monty()
    monty2 = Monty()

    print(monty1)
    print (monty1.metier)
    print(monty2)
    print (monty2.metier)

    #accès en écriture à la variable d'instance "metier"
    monty2.metier = "réalisateur"
    #accès en lecture à la variable d'instance "metier"
    print(monty2.metier)
    print(monty1.metier)

main()


# Par convention, `self`est toujours passé en argument au constructeur. Il fait référence à l'objet lui-même (et contient donc sont emplacement mémoire, comme le prouve le code ci-dessus).
# `self.var`permet d'initialiser une variable. Cette variable est mise en mémoire dans l'objet. Pour la lire, ou la modifier, il suffit de faire `moninstance.var`. Le point est l'opérateur qui permet de trouver les variables dans l'objet.

# In[24]:


class Monty:
    #constructeur avec une valeur d'initialisation en paramètre
    def __init__(self, nom):
        #initialisation d'une variable à partir d'un paramètre
        self.nom = nom
        self.metier = "comédien"

#fonction main() pour le programme principal
def main() :
    #création d'instances avec passage de valeurs en paramètre
    monty1 = Monty("Cleese")
    monty2 = Monty("Gilliam")
    print (monty1.nom)
    print (monty2.nom)
    
main()


# Il est possible d'initialiser les variables d'instance à la création en passant les valeurs en paramètre. Puis, dans le constructeur, il est suffit des les attribuer `self.var = parametre`.
# 
# Vous pouvez créer autant de variables d'instance que vous avez besoin. De même, il est possible de passer en paramètre autant de valeurs que besoin.

# In[25]:


class Monty:
    #dictionnaire d'une taille indéterminée en paramètre
    def __init__(self, **infos):
        #parcours le dictionnaire pour récupérer les clés et les valeurs
        for variable, valeur in infos.items():
            #création de variable avec la clé et initialisation avec la valeur
            setattr(self, variable, valeur)
            
#Fonction main() pour le programme principal
def main() :
    #dictionnaire            
    infos1 = {"nom":"Cleese", "metier":"comédien"}
    infos2 = {"nom":"Gilliam", "metier":"réalisateur"}

    #passage de dictionnaires en paramètre
    monty1 = Monty(**infos1)
    monty2 = Monty(**infos2)

    #les variables du dictionnaire sont accessibles dans l'objet
    print(monty1.nom)
    print(monty2.nom)
    print(monty2.metier)
    
main()


# Lorsqu'il y a plusieurs variables à initialiser, il est possible de passer un dictionnaire en paramètre du constructeur. `**`.Ce dictionnaire contient les noms et les valeurs des variables. Dans ce cas il faut signaler que nous avons un paramètres de taille indéterminée grâce au `**`.
# Il faut le faire à la déclaration du constructeur et lors de son appel dans le code.
# Ensuite, dans le constructeur, il suffit de parcourir le dictionnaire et d'utiliser la fonction `setattr(self, nom_variable, valeur_variable)`. Ainsi, toutes les variables d'instances sont créées automatiquement.

# ## Méthodes
# 
# Une classe peut aussi contenir des fonctions, dans ce cas, elles sont appelées *méthodes*.

# In[26]:


class Monty:
    
    def __init__(self, nom):
        self.nom = nom
        
    # méthode saluer(), déclarée comme une fonction
    def saluer(self, qui) :
        return self.nom + " dit bonjour à " + qui
    
#fonction main() pour le programme principal
def main() :
    monty1 = Monty("Cleese")
    monty2 = Monty("Gilliam")
    print (monty1.saluer(monty2.nom))
    
main()


# Une méthode se déclare comme une fonction, mais dans la classe. Pour l'appeler, il faut le faire avec une instance. Comme pour les variables, il faut utiliser le point pour l'appeler avec une instance. Par convention, la méthode prend toujours `self`en paramètre. Contrairement au constructuer, la méthode peut avoir un `return` et prend autant de paramètre qu'il y a besoin.

# In[33]:


from datetime import datetime

class Monty:
    
    def __init__(self, nom):
        self.nom = nom
        
    # méthode saluer(), déclarée comme une fonction
    def saluer(self, qui) :
        return self.nom + " dit : " + self.formuler_salut(qui)
    
    #méthode qui ne sert que dans la classe
    def formuler_salut(self, qui) :
        formule = "Good morning "
        heure = datetime.now().hour
        
        if(heure > 11) :
            formule = "Good afternoon "
        if(heure > 18) :
            formule = "Good evening "
            
        return formule + qui
    
#fonction main() pour le programme principal
def main() :
    monty1 = Monty("Cleese")
    monty2 = Monty("Gilliam")
    print (monty1.saluer(monty2.nom))
    
main()


# une méthode peut être appelée dans une autre méthode en utilisant le self : `self.methode()`.

# ## Collection d'objets
# 
# Puisque l'avantage des objets est d'en instancier autant que voulu, il n'est pas rare de le faire sous forme de collection.

# In[38]:


class Monty:
    
    def __init__(self, **infos):
        #parcours le dictionnaire pour récupérer les clés et les valeurs
        for variable, valeur in infos.items():
            #création de variable avec la clé et initialisation avec la valeur
            setattr(self, variable, valeur)
        
#lire data
def lire_data():
    #ce dictionnaire simule la lecture d'une source de données
    equipe = [{"nom" : "Cleese", "metier":"comédien"}, {"nom" : "Gilliam","metier":"realisateur"}, {"nom":"Chapman", "metier":"comédien"}, {"nom":"Jones", "metier":"comédien"}, {"nom":"Palin", "metier":"comédien"},{"nom":"Idle", "metier":"comédien"}]
    return equipe
    
#fonction main() pour le programme principal
def main() :
    membres = lire_data()
    objets = []
    
    #boucle pour créer une collection d'objets
    for membre in membres :
            nouveau = Monty(**membre)
            objets.append(nouveau)
    
    #boucle pour parcourir la collection d'objets
    for monty in objets :
        print(monty.nom)
    
main()


# L'avantage de la collection c'est qu'il n'y a besoin d'une variable par instance puisqu'elles sont toutes stockées dans une liste (ou un dictionnaire, c'est aussi possible). Il suffit alors de la parcourir pour travailler avec les instances.

# In[ ]:




