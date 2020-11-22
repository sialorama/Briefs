#!/usr/bin/env python
# coding: utf-8

# # MySql

# ### Utiliser une base de donnée MySQL
# Pour cette partie, on a installé le paquet python3-mysql.connector. 

# A partir de la table arrets disponible dans la base de données Breizhibus, afficher tous les arrêts dans l'ordre alphabétique de leur nom :
#        SELECT *
#        FROM arrets
#        ORDER BY nom

# ### Renommer une tables
#  
#      RENAME TABLE old_table TO new_table;
#      ou
#      RENAME TABLE old_table1 TO new_table1,
#                  old_table2 TO new_table2,
#                  old_table3 TO new_table3;

# ### Ajouter des valeur à une table
#     INSERT INTO tableName (colonne1, colonne2, ...) VALUES (valeur1, valeur2, ...);

# ##### MySql : table arret_ligne dans Brizhibus pour les lignes R, V, B
# 
# INSERT INTO `arrets_lignes` (`id_ligne`, `id_arret`) VALUES ('1', '1'), ('1', '2'), ('1', '3'), ('2', '2'), ('2', '4'), ('2', '6'), ('3', '4'), ('3', '5'), ('3', '6'), ('3', '1');
# 

# ##### MySql : table arret_ligne dans Brizhibus pour la ligne N
# 
# INSERT INTO `arrets_lignes` (`id_ligne`, `id_arret`) VALUES ('6', '1'), ('6', '3'), ('6', '5');

# ##### Requête pour retourner la liste des lignes :
# SELECT * FROM lignes;

# ##### Requête pour trouver les arrêts d'une ligne :
# SELECT * FROM arrets
# JOIN arrets_lignes ON arrets.id_arret = arrets_lignes.id_arret
# WHERE id_lignes = 1;
# Où 1 peut-être n'importe quelle id de ligne.

# ![join_on_where Logo](.\images\join_on_where.png)

# ##### Les arrêts desservit par la ligne rouge : Join
# 
# SELECT * FROM `arrets` JOIN lignes ON lignes.id_ligne=arrets.id_arret WHERE id_ligne=1

# ### Ajouter une colonne dans une table
# 
# ###### La syntaxe pour ajouter une colonne dans une table MySQL est la suivante:
#         ALTER TABLE tableName
#             ADD newColumn type
#               [ FIRST | AFTER columnName ]
#       
# ###### Exemple 1: Ajouter une seule colonne
#         ALTER TABLE users
#           ADD age int NOT NULL
#             AFTER name;
#           
# ###### Exemple 2: Ajouter plusieurs colonnes
#         ALTER TABLE users
#           ADD age int NOT NULL
#             AFTER name,
#           ADD address varchar(50) NOT NULL
#             AFTER age;

# ### Modifier une colonne dans une table
# 
# ###### La syntaxe pour modifier une colonne dans une table MySQL est la suivante:
#         ALTER TABLE tableName
#             MODIFY columnName type
#               [ FIRST | AFTER columnName ];
# ###### Exemple:
#         ALTER TABLE users
#           MODIFY address varchar(100) NULL;

# ### Renommer une colonne dans une table
# 
# ###### La syntaxe pour renommer une colonne dans une table MySQL est la suivante:
#         ALTER TABLE tableName
#             CHANGE COLUMN oldName newName 
#               type
#               [ FIRST | AFTER columnName ]
# 
# ###### Exemple:
#         ALTER TABLE users
#           CHANGE COLUMN name lastname
#             varchar(50) NOT NULL;

# #### Créer la base et insérer des données

# In[ ]:


# Nous allons utiliser le module mysql.connector pour nous connecter au serveur MariaDB ou MySQL et créer notre base de données permettant de stocker un catalogue de produits.
import mysql.connector

baseDeDonnees = mysql.connector.connect(host="localhost",user="catalogue",password="JieTh8Th", database="Catalogue")
cursor = baseDeDonnees.cursor()
cursor.execute("CREATE TABLE Produits (reference CHAR(5) NOT NULL PRIMARY KEY, nom TINYTEXT NOT NULL, prix FLOAT NOT NULL)ENGINE=InnoDB DEFAULT CHARSET=utf8;")
baseDeDonnees.close()


# In[ ]:


Nous allons à présent insérer des données dans cette table :
    
import mysql.connector 
baseDeDonnees = mysql.connector.connect(host="localhost",user="catalogue",password="JieTh8Th", database="Catalogue")
curseur = baseDeDonnees.cursor()
curseur.execute("INSERT INTO Produits (reference, nom, prix) VALUES (%s, %s, %s)", ("ARB42", "Canapé deux places noir", 199.99))
baseDeDonnees.commit()
baseDeDonnees.close()


# In[ ]:


Il est également possible d'insérer des données depuis un dictionnaire :

import mysql.connector 
baseDeDonnees = mysql.connector.connect(host="localhost",user="catalogue",password="JieTh8Th", database="Catalogue")
curseur = baseDeDonnees.cursor()
produits = [
	{"reference":"EIS3P", "nom":"Chaise de salle à manger", "prix":25},
	{"reference":"BA9KI", "nom":"Commode blanche", "prix":139.90},
	{"reference":"OI4HE", "nom":"Table basse", "prix":24.95},
	{"reference":"IOM9X", "nom":"Lit double", "prix":699.99}
]
for fiche in produits:
	curseur.execute("INSERT INTO Produits (reference, nom, prix) VALUES (%(reference)s, %(nom)s, %(prix)s)", fiche)
baseDeDonnees.commit()
baseDeDonnees.close()


# #### Récupérer des données
# 
# On peut utiliser fetchone pour récupérer le premier résultat ou retourner tous les résultats avec fetchall. Voici comment récupérer le premier résultat d'une requête SELECT.

# In[ ]:


import mysql.connector 
baseDeDonnees = mysql.connector.connect(host="localhost",user="catalogue",password="JieTh8Th", database="Catalogue")
curseur = baseDeDonnees.cursor()
curseur.execute("SELECT reference, nom, prix FROM Produits")
print(curseur.fetchone())
('ARB42', 'Canapé deux places noir', 199.99)
baseDeDonnees.close()


# In[ ]:


On peut retourner tous les résultats avec fetchall :

>>> import mysql.connector 
>>> baseDeDonnees = mysql.connector.connect(host="localhost",user="catalogue",password="JieTh8Th", database="Catalogue")
>>> curseur = baseDeDonnees.cursor()
>>> curseur.execute("SELECT reference, nom, prix FROM Produits")
>>> for ligne in curseur.fetchall():
...     print(ligne)
... 
('ARB42', 'Canapé deux places noir', 199.99)
('BA9KI', 'Commode blanche', 139.9)
('EIS3P', 'Chaise de salle à manger', 25.0)
('IOM9X', 'Lit double', 699.99)
('OI4HE', 'Table basse', 24.95)
>>> baseDeDonnees.close()

