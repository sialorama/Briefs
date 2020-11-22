#!/usr/bin/env python
# coding: utf-8

# # Pandas

# In[2]:


#pandas est un outil d'analyse et de manipulation de data open source rapide,  puissant flexible et facile à utiliser.
#pandas est une librairie Python. 

#Groupe : Amaury, Erwan, Jamal, Julien

#Import du module:
import pandas

#Test de notre version de pandas:
pandas.__version__


# # Création de données

# In[196]:


testDataFrame = pandas.DataFrame([["Q-Bert",22, "male"],[None, 35, "male"],["Miss Pac-Man", 58, "female"]],
        index = [0, 1, 2],
        columns =["Name", "Age", "Sex"])

#Possibilité d'importer un fichier .csv également.

print(testDataFrame)


# # Lecture des données

# In[197]:


testDataFrame


# # Exploration des Data Frames

# In[198]:


for colone,item in testDataFrame.iteritems():
    print(colone, item)


# # Les attributs du Data Frame

# In[199]:


#loc -> Access a group of rows and columns by label(s) or a boolean array.
#iloc -> Purely integer-location based indexing for selection by position.

#size -> Return an int representing the number of elements in this object.
testDataFrame.size


# # Les méthodes du Data Frame 

# In[200]:


testDataFrame.head(1)


# In[202]:


testDataFrame.tail(1)


# In[217]:


#Renvoyer la moyenne des valeurs de la colonne Age :
print("L'âge moyen est :",testDataFrame.Age.mean())

#Alternative : testDataFrame['Age'].mean()

#Voici d'autres méthodes importantes :
print("L'âge minimum est :",testDataFrame.Age.min())
print("L'âge maximum est :",testDataFrame.Age.max())
print("L'écart-type de l'âge est :",testDataFrame.Age.std())
print("L'âge médian est :",testDataFrame.Age.median())

#Autres méthodes possibles : le produit des valeurs avec prod(), leur somme avec sum(), la variance normalisée avec var()
#Avec apply() on peut appliquer une fonction passée en argument, mad() donne la valeur absolue des écarts.
#Avec count() on peut compter les cases non-vides.


# In[204]:


#Possibilité intéressante : sortir automatiquement un tableau descriptif :
testDataFrame.describe()


# # Sélection d'une colonne dans un Data Frame

# In[205]:


#Output du contenu d'une "série" (~ colonne) entière et du type de ses valeurs:
#Une série est un vecteur de valeurs d'une variable.
testDataFrame["Age"]


# # La méthode groupby

# In[206]:


#Utilisation de la méthode grouby sur le critère sexe afin d'afficher la moyenne d'âge par sexe.
print(testDataFrame.groupby(["Sex"]).mean())


# # Filtrage

# In[220]:


#Filtrage sur un label particulier avec la fonction filter:
testDataFrame.filter(["Age"])

#On peut également choisir un axe de filtrage ou un regex:
#DataFrame.filter(items=None, like=None, regex=None, axis=None)


# # Slicing

# In[208]:


#Slice des deux premiers charactères des valeurs de la série Name grâce à la méthode slice.
testDataFrame["Name"].str.slice(start = 2)


# # Sélection des lignes

# In[221]:


#On sélectionne les lignes 1 et 2 avec la méthode iloc:
testDataFrame.iloc[[1,2]]

#On peut aussi sélectionner des lignes consécutives:
testDataFrame.iloc[1:2]


# # Loc

# In[210]:


#loc -> Access a group of rows and columns by label(s) or a boolean array.
testDataFrame.loc[1]


# # Tri

# In[211]:


#Tri descendant selon les indexes de lignes avec sort_index:
testDataFrame.sort_index(axis = 0, ascending = False)


# In[212]:


#Tri selon les séries avec sort_values:
testDataFrame.sort_values(by = 'Age') 


# # Valeurs manquantes

# In[216]:


#Vérifions si nous avons des valeurs manquantes dans notre tableau avec la méthode isnull:
testDataFrame.isnull()


# In[215]:


#Remplissage des valeurs manquantes avec une valeur unique grâce à fillna :
testDataFrame.fillna("Inconnu")

