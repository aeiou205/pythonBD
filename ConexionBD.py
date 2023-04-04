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
        self.insertRows()
        
    # Insert a row of data 
    def insertRows(self):    
        t = ('RHAT',)
        self.cur.execute('SELECT * FROM stocks WHERE symbol = ?', t)
        purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
        self.cur.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)',purchases)
        self.showRaws()
    
    # Show Data
    def showRaws(self):
        for row in self.cur.execute('SELECT * FROM stocks ORDER BY price'):
            print(row)
        self.saveChanges()

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
