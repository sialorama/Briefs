#!/usr/bin/env python
# coding: utf-8

# # Propriétés des objets en POO

# ## Encapsulation
# 
# L'encapsulation est un principe qui consiste à cacher ou protéger certaines données d'un objet. C'est un moyen de protéger les attributs d'objets, en faisant en sorte qu'ils en soient aps accessibles depuis l'extérieur de la classe.
# 
# Il peut être pratique de sécuriser certaines données d'un objet, par exemple faire en sorte qu'un attribut ne soit pas modifiable, ou alors mettre à jour un attribut dès qu'un autre attribut est modifié. Il est souvent utile de pouvoir contrôler l'accès en lecture ou en écriture sur certains attributs.
# 
# Cela présente néanmoins l'inconvénient de devoir ecrire des accesseurs et des mutateurs pour les objets. Cela peut être assez lourd, c'est pourquoi, en Python, on ne crée des propriétés que pour les objets dont on attend une action particulière. Pour les autres, on continue à y accéder directement par `objet.attribut`.

# ## Accesseurs et mutateurs
# 
# Les accesseurs donnent accès à l'attribut. On utilise généralement le préfixe `get` pour définir un accesseur. <br>
# Les mutateurs permettent de modifier un attribut. On utilise le préfixe `set` pour les définir.
# 
# par convention, on note `_attribut` un attribut qu'on ne doit pas pouvoir appeler depuis l'extérieur de la classe sans passer par les accesseurs et les mutateurs.

# ## Propriétés

# <q> Les propriétés sont un moyen transparent de manipuler des attributs d'objet. Elles permettent de dire à Python : « Quand un utilisateur souhaite modifier cet attribut, fais cela ». De cette façon, on peut rendre certains attributs tout à fait inaccessibles depuis l'extérieur de la classe, ou dire qu'un attribut ne sera visible qu'en lecture et non modifiable. Ou encore, on peut faire en sorte que, si on modifie un attribut, Python recalcule la valeur d'un autre attribut de l'objet.</q> (source : [Openclassroom](https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/232793-definissez-des-proprietes#/id/r-232744))

# ## Exemple

# In[9]:


class Chat :
    def __init__(self, race):
        self.race = race
        self._nb_pattes = 4
    
    def _get_nb_pattes(self):
        return self._nb_pattes
    
    def _set_nb_pattes(self, nouveau_nb):
        self._nb_pattes = nouveau_nb*2
        
    nb_pattes = property(_get_nb_pattes, _set_nb_pattes)
        


# In[10]:


cat = Chat("sphinx")
print(cat.nb_pattes)
cat.nb_pattes = 3
print(cat.nb_pattes)


# In[13]:


# alternative avec des décorateurs :
class Chat :
    def __init__(self, race):
        self.race = race
        self._nb_pattes = 4
    
    @property
    def nb_pattes(self):
        return self._nb_pattes
    @nb_pattes.setter
    def nb_pattes(self, nouveau_nb):
        self._nb_pattes = nouveau_nb*2
        


# In[16]:


kiki = Chat("sphinx")
print(kiki.nb_pattes)
kiki.nb_pattes = 3
print(kiki.nb_pattes)


# ## Sources :
# [openclassroom](https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/232793-definissez-des-proprietes) <br>
# [pierre giraud cours python ](https://www.pierre-giraud.com/python-apprendre-programmer-cours/oriente-objet-visibilite-attribut/)
