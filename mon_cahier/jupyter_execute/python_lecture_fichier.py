#!/usr/bin/env python
# coding: utf-8

# # Python Traitement de fichiers

# ## La gestion des fichiers

# La fonction clé pour travailler avec des fichiers en Python est la open()fonction.
# 
# La open()fonction prend deux paramètres; nom de fichier et mode .

# 
# ###### Il existe quatre méthodes (modes) différentes pour ouvrir un fichier:
# 
# "r"- Lire - Valeur par défaut. Ouvre un fichier en lecture, erreur si le fichier n'existe pas
# 
# "a" - Ajouter - Ouvre un fichier à ajouter, crée le fichier s'il n'existe pas
# 
# "w" - Ecrire - Ouvre un fichier pour l'écriture, crée le fichier s'il n'existe pas
# 
# "x" - Créer - Crée le fichier spécifié, renvoie une erreur si le fichier existe

# ###### Pour ouvrir un fichier en lecture, il suffit de spécifier le nom du fichier:
# f = open("demofile.txt")

# In[4]:


f = open("test.txt", "r")
print(f.read())


# In[16]:


#Lire  deux lignes en utilisant la readline()méthode
f = open("test.txt", "r")
print(f.readline())


# In[17]:


#Renvoie les 5 premiers caractères du fichier:
f = open("test.txt", "r")
print(f.read(5))


# In[7]:


#Parcourir le fichier ligne par ligne:
f = open("test.txt", "r")
for x in f:
  print(x)


# In[8]:


#Fermer le fichier à la fin d'utilisation
f = open("test.txt", "r")
print(f.readline())
f.close()


# Écrire dans un fichier existant
# Pour écrire dans un fichier existant, vous devez ajouter un paramètre à la open()fonction:
# 
# "a" - Ajouter - ajoutera à la fin du fichier
# 
# "w" - Ecrire - écrasera tout contenu existant

# In[9]:


#Ouvrez le fichier "test2.txt" et ajoutez le contenu au fichier test:
f = open("test.txt", "a")
f.write("!!! Now the file has more content !!!")
f.close()

#open and read the file after the appending:
f = open("test.txt", "r")
print(f.read())


# In[10]:


#Ouvrir le fichier "demofile3.txt" et écrasez le contenu:
f = open("test2.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("test2.txt", "r")
print(f.read())


# ### Créer un nouveau fichier

# Pour créer un nouveau fichier en Python, utilisez la open()méthode, avec l'un des paramètres suivants:
# 
# "x" - Créer - créera un fichier, renvoie une erreur si le fichier existe
# 
# "a" - Ajouter - créera un fichier si le fichier spécifié n'existe pas
# 
# "w" - Ecrire - créera un fichier si le fichier spécifié n'existe pas

# In[11]:


#Créer un fichier monfichier.txt
f = open("monfichier.txt", "x")


# In[12]:


#Créerz un nouveau fichier s'il n'existe pas:

f = open("monfichier2.txt", "w")


# ### Supprimer un fichier

# In[13]:


#Supprimez le fichier monfichier2.txt:

import os
os.remove("monfichier.txt")


# ### Vérifiez si le fichier existe:

# In[14]:


import os
if os.path.exists("test2.txt"):
  os.remove("test2.txt")
else:
  print("The file does not exist")


# ### Supprimer le dossier

# In[ ]:


import os
os.rmdir("mmondossier")

