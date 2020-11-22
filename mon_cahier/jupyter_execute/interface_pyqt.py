#!/usr/bin/env python
# coding: utf-8

# # Interfaces graphiques avec PyQt

# [PyQt5](https://riverbankcomputing.com/software/pyqt/intro) est une librairie Python qui permet de créer facilement des interfaces graphiques (GUI - IHM).<br>
# Il existe de nombreuses autres bibliothèques concurentes, comme par exemple [Qt for Python](https://www.qt.io/qt-for-python), dont l'API est similaire, et qui contrairement à PyQt est distribuée sous licence LGPL, ce qui permet de l'utiliser gratuitement pour des projets commerciaux. Il est relativement aisé de passer de l'une à l'autre si nécessaire.

# ## Hello World !
# 
# Après avoir importé les modules nécessaires, Qt requiert de commencer par créer une `QApplication`. Chaque interface graphique (GUI) doit comporter exactement _une_ instance de QApplication. La majorité des modules Qt ne fonctionneront pas tant que la commande `app = QApplication([])` n'aura pas été exécutée.<br>
# Des arguments peuvent être passés entre les crochets `[]`. Dans notre exemple ci-dessous, notre app n'utilise aucun paramètre, nous laissons donc les crochets vides.
# 
# Une autre étape importante à ne pas oublier est de demander au programme de prendre le contrôle sur Qt, en lui demandant de "faire tourner l'application jusqu'à ce que l'utilisateur la ferme". Ceci est permis par la commande `app.exec_()`. 

# ```python 
# from PyQt5.QtWidgets import QApplication, QLabel
# 
# app = QApplication([])
# label = QLabel('Hello World!') # creation d'un label
# label.show() # affichage du label sur l'écran
# app.exec_()
# ```

# ## Widgets
# 
# Tous ce qu'on peut voir dans une app PyQt est appelé _widget_.<br>
# Les plus courants sont :
# *    __QLabel__ : étiquette
# *    __QComboBox__ : liste déroulante combinée à une zone de texte (boîte combinée)
# *    __QCheckBox__ : case à cocher
# *    __QRadioButton__ : bouton radio, dont l'objectif est de choisir une et une seule option (utilisés en groupe)
# *    __QPushButton__ : bouton poussoir
# *    __QTableWidget__ : tableau
# *    __QLineEdit__ : champs de remplissage de texte (zone de texte)
# *    __QSlider__ : curseur sur glissière graduée
# *    __QProgressBar__ : barre de progression, pour traduire l'etat d'avancement d'un travail 
# 

# ## Layouts (disposition)
# 
# Une GUI étant généralement constituée de plusieurs Widgets, il est nécessaire de fournir à PyQt les instructions pour les positionner. <br>
# On utilise par exemple `QVBoxLayout()` pour empiler les Widgets verticalement, ou  `QHBoxLayout()` pour les disposer horizontalement.<br> 
# 
# `QGridLayout` permet de placer les éléments sur une grille, on passe leur position (ligne, colonne) en arguments.
# 
# ```python
# self.layout = QGridLayout()   # Création de la grille de placement
# self.layout.addWidget(self.libelle, 0, 0)  # Placement du label en haut de l'UI
# self.layout.addWidget(self.bouton1, 1, 0) 
# self.layout.addWidget(self.bouton2, 1, 1)
# ```
# 
# 
# Il exite beaucoup d'autres types de layouts, à retrouver dnas la [documentation Qt](http://doc.qt.io/qt-5/layout.html)

# ## Styles
# 
# ### Styles buit-in
# Les styles disponibles dépendent de la platefonrme qur laquelle on travaille, mais sont généralement 'Fusion', 'Windows', 'WindowsVista' (Windows uniquement) and 'Macintosh' (Mac uniquement).<br>
# Pour les appliquer, on utilise `app.setStyle(...)`:
# ```python
# from PyQt5.QtWidgets import *
# app = QApplication([])
# app.setStyle('Fusion')
# ...```

# ### Couleurs
# Pour personnaliser les couleurs, on utilise le module QPalette et la commande `app.setPalette(...)`.<br>
# L'exemple ci-dessous affiche le texte du bouton poussoir en rouge :
# 
# ```python
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QPalette
# from PyQt5.QtWidgets import QApplication, QPushButton
# 
# app = QApplication([])
# app.setStyle('Fusion')
# palette = QPalette()
# palette.setColor(QPalette.ButtonText, Qt.red)
# app.setPalette(palette)
# button = QPushButton('Hello World')
# button.show()
# app.exec_()
# 
# 
# ```
# Voir [ici sur GitHub](https://gist.github.com/mstuttgart/37c0e6d8f67a0611674e08294f3daef7) un exemple de palette Dark Theme complète, qui donne également un bon apperçu des possibilités offertes par ce module Palette.

# ### Style sheets
# Une autre façon de mofifier l'apparence d'une app est d'utiliser *style sheet*. La syntaxe utilisée entre accolades est alors similaire au CSS.
# 
# ```python
# app = QApplication([])
# app.setStyleSheet("QPushButton { margin: 10ex; }")```
# 
# Voir [la documentation complète](https://doc.qt.io/qt-5/stylesheet-syntax.html)

# ## Signaux et 'slots'
# 
# Qt utilise des mécanisqmes appelés _Signaux_ pour établir la réaction à un événement comme un clic utilisateur sur un bouton. La syntaxe utilisée est la suivante : `button.clicked.connect(...)` : `button.clicked` est le signal, `.connect` permet d'installer un *slot*, qui est simplement une fonction appelée lorsque le signal est activé.
# 
# Le terme *slot* est inportant en C++, où les slots sont déclarés d'une façon particulière, en Python, n'importe quelle fonction peut être un slot.

# ```python
# from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QMessageBox, QLabel
# 
# class Fenetre(QWidget):
# 	def __init__(self):
# 		QWidget.__init__(self)
# 		self.setWindowTitle("Deux possibilités")
# 		self.setGeometry(500,100,300,200)
# 
# 		self.bouton1 = QPushButton("bouton du haut")
# 		self.bouton1.clicked.connect(self.appui_bouton1)
# 		self.bouton2 = QPushButton("bouton du bas")
# 		self.bouton2.clicked.connect(self.appui_bouton2)
# 		self.reponse = QLabel()
# 		self.reponse.setText("Appuyez sur le bouton du haut.")
# 
# 		layout = QVBoxLayout()
# 		layout.addWidget(self.bouton1)
# 		layout.addWidget(self.bouton2)
# 		layout.addWidget(self.reponse)
# 		self.setLayout(layout)
# 
# 	def appui_bouton1(self):
# 		self.reponse.setText("Ok, c'est bien le bouton du haut.")
# 
# 	def appui_bouton2(self):
# 		self.alert = QMessageBox()
# 		self.alert.setText('Vous avez appuyé sur le bouton du bas !')
# 		self.alert.exec_()
# 
# def main():
# 	app = QApplication([])
# 	fen = Fenetre()
# 
# 	fen.show()
# 	app.exec_()
# 
# main()
# ```

# In[ ]:




