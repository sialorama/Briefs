import mysql.connector

class Query:

    def __init__(self):
        self.mydb = mysql.connector.connect(host = "localhost", user = "root", password="root", database ="binomotron")
        self.cursor = self.mydb.cursor()

    def get_apprenants(self):
        array = []
        cursor.execute("SELECT id_apprenants FROM apprenants")
        for ligne in cursor.fetchall():
            array.append(ligne[0])
        mydb.close
        return(array)


    def add_crew(self, crew):
        self.cursor.execute("DELETE FROM `apprenant_groupe`;")
        for groupe in crew:
            for apprenant in crew[groupe]:
                sql = """INSERT INTO apprenant_groupe(id_apprenants, id_projet, id_groupe) VALUES (%s,%s,%s)"""
                value = (apprenant,1,groupe)
                self.cursor.execute(sql, value)
            self.db.commit()    
        self.db.close()

#Query().get_apprenants()
#Query().add_crew()
