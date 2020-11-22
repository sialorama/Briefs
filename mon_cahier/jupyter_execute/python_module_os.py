#!/usr/bin/env python
# coding: utf-8

# ## Python - Le module OS

# Le module os est un module  fournit par Python dont le but d’interagir avec le système d’exploitation, il permet ainsi de gérer l’arborescence des fichiers, de fournir des informations sur le système d’exploitation processus, variables systèmes, ainsi que de nombreuses fonctionnalités du systèmes…

# ###### os.getlogin()
# 
# renvoie le nom d’utilisateur courant.

# ###### Programme Python qui renvoie le nom d’utilisateur:

# import os 
# user = os.getlogin() 
# print(user) # imprime le nom d'utilisateur

# ###### Création d’un dossier à la racine du disque C:\
# import os
# 
# os.mkdir("c:/myFolder") # crée un dossier nommé myFolder sur le disque C:\

# ### La méthode os.path
# 
# Afin de pouvoir utiliser la méthode os.path, il faut préalablement importer le module pathlib. Le module pathlib est un module doté d’une interface orientée objet inclus dans python depuis la version 3.4 doté de méthodes très intuitives permettant d’interagir avec le système de fichiers d’une façon simple et conviviale.

# #### Tester l’existence d’un répertoire

# In[7]:


import os  
from pathlib import Path
print(os.path.exists("c:/users/"))
#affiche True


# #### Tester si un chemin est un répertoire ou un fichier avec les méthodes is_dir() et is_file()

# In[3]:


import os 
from pathlib import Path 
myDirectory = "C:/Users" 
p = Path(myDirectory) 
print(p.is_dir()) # affiche True
print(p.is_file()) # affiche False


# #### Obtenir le chemin du dossier parent avec la méthode parent

# In[4]:


from pathlib import Path 
from pathlib import Path 
myDirectory = "C:/Users/Public/" 
p = Path(myDirectory) 
print(p.parent) # Affiche 'C:\Users'
# parent renvoie aussi le dossier parent d'un fichier
myDirectory = "C:/Users/Public/Videos/Sample Videos/Wildlife.wmv" 
p = Path(myDirectory) 
print(p.parent) # Affiche 'C:\Users\Public\Videos\Sample Videos'


# #### Récuperation du contenu d’un dossier avec la méthode scandir() appliquée à la méthode Path()

# In[6]:



from pathlib import Path 
import os 
myDirectory="c:/users" 
p = Path(myDirectory) 
for x in os.scandir(p): 
    print(x)


# #### Afficher tous les fichiers d’une extension spécifique via la méthode glob()

# La méthode glob() est l’une des méthodes de l‘objet Path permettant d’afficher la liste des fichiers d’une extension donnée. Par exemple affichager des bibliothèques .dll du répertoire ‘ C:/Windows ‘

# In[9]:


from pathlib import Path  
p = Path('C:/Windows/') 
for f in list(p.glob('**/*.dll')):
    print(f)


# In[ ]:




