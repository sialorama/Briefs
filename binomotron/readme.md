# Binomotron

## Algo

```python
def __init__(self, number_in_group):
    self.people = Query.get_apprenants(self)
    self.number_in_group = number_in_group
```
-Cette fonction var cree des varibale a partir de ces arguments ou d'autre fichier dés que la fonction est instancier</br>
-Recuprer les personne dans la basse de donne</br>
-Donne un argument qui est le nombre de persone dans le groupe


```python 
def compute(self):
    crew = {}
    cpt = 0
    random.shuffle(self.people)
```
-initialisation d'un dictonnaire vide</br>
-initialisation d'un compteur qui va nous servir de compteur dans la boucle while</br>
-randomisation de la liste de persone </br></br>

```python
while(len(self.people) >= self.number_in_group):
            cpt+=1
            newarray = []
            for _ in range(self.number_in_group):
                newarray.append(self.people[0])
                self.people.remove(self.people[0])
            crew[cpt] = newarray
````

-Rentre dans une boucle tant que la taille de **[people]** et superieur a la taille de **groupe** </br>
-Initialise une liste qui va permertre de stocker les membres du **number_in_group**</br>
-Boucle le nombre de fois qui il a de persone dans le **number_in_group**</br>
-Recupere et stock la premier persone du tableau </br>
-La suprime du tableau</br>
-Ajoute une cle au dictionnaire et stocke les perssone dans ce dictionnaire</br>

```python
if len(self.people) > 0 :
    crew[cpt+1] = self.people
return(crew)
```
-Si people est pas vide on ajoute les dernier persone au dictionnaire

## Query

```python
def __init__(self):
        self.mydb = mysql.connector.connect(host = "localhost", user = "root", password="root", database ="binomotron")
        self.cursor = self.mydb.cursor()
````
-Cette fonction var cree la variable l'instance de **mysql.connector** et nous connecter a la base de donne


```python
def get_apprenants(self):
    array = []
    cursor.execute("SELECT id_apprenants FROM apprenants")
    for ligne in cursor.fetchall():
        array.append(ligne[0])
    mydb.close
    return(array)
```

-Initialise une liste vide </br>
-Selectionne la table</br>
-Place tout les perssone dans la liste</br>
-ferme la base de donne </br>
-Return la liste</br>


```python
def add_crew(self, crew):
    self.cursor.execute("DELETE FROM `apprenant_groupe`;")
    for groupe in crew:
        for apprenant in crew[groupe]:
            sql = """INSERT INTO apprenant_groupe(id_apprenants, id_projet, id_groupe) VALUES (%s,%s,%s)"""
            value = (apprenant,1,groupe)
            self.cursor.execute(sql, value)
        self.db.commit()    
    self.db.close()
```

-Vide la table
-Parcour crew
-Parcour les valeur de crew
-Insert les element dans le table 
-Commit
-Ferme la base




