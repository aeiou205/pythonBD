"""Conexxion a una base de datos con python"""

"""1 revisar que base de datos tienes alojadas en el sistem,a """
#Generar una bd con registros en mysql 
#Buscar las sentencias basicas como lo es 
import sqlite3

class DataBases:
    #create constructor
    def __init__(self, bs, con, cur):
        self.bs= bs
        self.con = con
        self.cur = cur
  
    # Create table 
    def createTable(self):
        self.cur.execute('''CREATE TABLE stocks
                    (date text, trans text, symbol text , qty real, price real)''')
        self.sentence()
    # Insert a row of data 
    def sentence(self):    
        self.cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
        self.showData()
    
    # Show Data
    def showData(self):
        for row in self.cur.execute('SELECT * FROM stocks ORDER BY price'):
            print(row)

    # Save (commit) the changes
    def saveChanges(self):
        self.con.commit()
        self.con.close()

def main():
    print("hola")    
    bs=input(" Inserte el nombre de la base de datos: ")
    con = con=sqlite3.connect(bs)
    cur = con.cursor()
    basedata=DataBases(bs,con,cur)
    basedata.createTable()


if __name__ == '__main__':
    main()
