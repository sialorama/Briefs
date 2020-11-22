#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Numpy est une extension du language de programmation Python, 
#destinée à manipuler des matrices ou tableaux multidimensionnels ainsi que des fonctions 
#mathématiques opérant sur ces tableaux
import numpy as np


# # Creation de vecteurs et des matrices

# In[119]:


#Creation d'une matrice :
b = np.array([i for i in range(6)])
b


# In[120]:


a = np.arange(1, 41, 2)
a


# In[121]:


#Redimensionnement :
a = a.reshape(4,5)
a


# In[122]:


b = b.reshape(2,3)
b


# In[123]:


#Conversion :
c = b.astype(np.float)


# In[124]:


#Typage des données : 
print(f"La matrice de a est de type : {a.dtype}")
print(f"La matrice de b est de type : {b.dtype}")
print(f"La matrice de c est de type : {c.dtype}")


# In[125]:


#creation d'une matrice sans reshape:
d = np.ones((3,4),"int32")
print(f"La matrice d est : {d.dtype}\n{d}")


# # Extraction des valeurs

# In[126]:


#Plage d'indices:
b


# In[127]:


b[1,2]


# In[128]:


b[0]


# In[129]:


b[0, 1:3]


# Ecriture générique:
# 
# b[<font color='red'>début:fin</font>, <font color='green'>début:fin</font>] 
# 
# #red : selection de la ligne 
# #green : selection de l'élément(s) dans la ligne

# In[130]:


#Indiçage booléen:
a


# In[131]:


a<22


# In[132]:


a[a<22]


# In[133]:


#Tri et recherche:
np.max(a, axis=0) # axis = 0 -> recherche sur colonne


# In[134]:


np.min(a, axis=1) # axis = 1 -> recherche sur ligne


# # Calcul sur les vecteurs et les matrices:

# In[135]:


#Calcul statistiques : 
b


# In[136]:


#moyenne:
np.mean(b)


# In[137]:


#moyenne ligne ou colonne:
print(f"Moyenne de toutes les colonnes : {np.mean(b, axis = 0)}") 
print(f"Moyenne de toutes les lignes : {np.mean(b, axis = 1)}") 


# In[138]:


#médiane:
a


# In[139]:


np.median(a, axis=0)


# In[140]:


np.median(a, axis = 1)


# In[3]:


#variance:
import numpy as np
a = np.arange(1, 41, 2)
a = a.reshape(4,5)
a


# In[4]:


np.var(a, axis=0)


# In[5]:


np.var(a, axis=1)


# In[16]:


#quantile
print("Q2 quantile of arr : ", np.quantile(a, .50)) 
print("Q1 quantile of arr : ", np.quantile(a, .25)) 
print("Q3 quantile of arr : ", np.quantile(a, .75)) 


# In[18]:


#somme
np.sum(a, axis=0)


# In[19]:


np.sum(a, axis=1)


# In[21]:


#somme cumulé
np.cumsum(a)


# In[23]:


#Multiplication entre matrices
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
np.dot(a,b)


# In[24]:


#Multiplication entre vecteurs
np.multiply(a,b)


# #### Lien utile pour la manipulation de Numpy:
# http://eric.univ-lyon2.fr/~ricco/cours/slides/PH%20-%20matrices%20avec%20numpy.pdf

# In[ ]:




