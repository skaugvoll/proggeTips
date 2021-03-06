# coding=utf-8
import sqlite3

#self.connection.commit()
#commiter den aktuelle transaksjonen/endringen som gjores. Hvis denne ikke blir kallt,
#vill at som er gjort siden forje kommit utfort ikke bli "tilgjengelig/synlig" for andre som er
#koblet til databasen. Dette kan skape problemer! saa like greit aa bare gjore alle endringer synlig for
#andre med en gang.

class SQLLite:
    '''
    Dette er en klasse for å kommunisere med en SQLlite database.
    '''
    def __init__(self,path):
        '''
        Denne metoden blir kalt med en gang det lages et objekt av denne klassen/scriptet. Og kan tenkes på som en konstruktør
        Metoden setter verdien/ oppretter globale/static variabler til klassen slik at alle metodene i klassen
        kan snakke med samme variabler og instanser som tilhorer klassen.
        '''
        self.path = path;
        self.connection = None
        self.cursor = None

    def establishConnection(self):
        '''
        Denne metoden prover aa etablere forbindelse mellom objektet og databasen.
        Naar forbindelsen er satt, initialiseres self.cursor variablen som en instans av en peker til databasen.
        Denne pekeren er den som kan kommunisere med databasen og utforer SQL-querys/statements.
        :return: True hvis etablert forbindelse og opprettelse av cursor instans vellykket. returnerer False hvis det misslykket.
        '''
        try:
            self.connection = sqlite3.connect(self.path)
            self.cursor = self.connection.cursor()
            return True
        except:
            return False
        
    def executeInsertStatement(self,query):
        '''
        Denne metoden tar inn en SQL-insert statement og ber self.cursor instansne om aa utfore.
        Etter at cursor har utfort innsettingen til databasen, commiter den utforelsen og gjor endringen synlig for andre som snakker med databasen.
        :param: SQL-statement.
        :return: True hvis det gikk aa sette inn og commite, False hvis det ikke gikk.
        '''
        try:
            self.cursor.execute(query)
            self.connection.commit()
            return True
        except:
            return False
        
    def executeQueryStatement(self, query="SELECT * FROM Friends"): # denne mtoden kan ogsaa gjore som executeInsertStatement og ta inn en query/statement som parameter
        '''
        Denne metoden utforer hentinger/data-henting fra databasen.
        :return: liste med alle tupplene fra databasen. False hvis det ikke gikk.
        '''
        self.cursor.execute(query)
        return self._createResultSet()

    def _createResultSet(self):  # _ framfor funksjons/metode navnet sier at dette er en private-metode. eks: _privatMetode 
        '''
        Dette er en privat-methode som lager en liste kalt resultSet,
        ResultSet bestaar av tuplene/objekten i database tabellen
        :return: resultSet en liste med tupler/objektene i databasen.
        '''
        resultSet = []
        for row in self.cursor:
            resultSet.append(row)
            print(row)
        return resultSet
            
    def closeConnection(self):
        '''
        Denne funksjonen commiter forst alle endringen som er blitt gjort siden forje commit, slik at alle endringer blir
        synlig for andre som er tilkoblet databasen. Saa lukker den forbindelsen mellom objektet og databasen.
        :return: True hvis commit og forbindelse var sukksessfult, False hvis noe gikk galt. 
        '''
        try:
            self.connection.commit()
            self.connection.close()
            return True
        except:
            return False
        

def main():
    path = "testDatabase.db" #Hvis ikke databasen er lagret akkurat samme plass som script, endres denne. Kan bruke relativ og absolutt vei/path.
    relativPath = "Resources/testDatabase.db"
    absoluttPath = "C:/Users/SigveAndreEvensen/Desktop/testDatabase.db"
    conn = SQLLite(path) # oppretter et objekt 'conn' av SQLite.py klassen, sender inn path som argument/parameter til konstruktøren. 
    conn.establishConnection() # etablerer forbindelse mellom objektet og databasen
    conn.executeInsertStatement("insert into Friends values('Thomas.',23,'97182999')") # Setter inn ny tuppel/objekt i database tabellen Friends
    conn.executeQueryStatement()
    conn.closeConnection() # lukker commiter innsettingen og lukker forbindelsen mellom conn objektet og databasen.

main()
