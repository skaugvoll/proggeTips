import mysql.connector
from mysql.connector import errorcode

#Connection configurations
#hostName could be for example 'mysql.stud.ntnu.no'
config = {'user': 'username',
          'password':'psswrd',
          'host':'hostName',
          'database':'dataBaseName',
          }

#Establish connection to the database with config-user information
def getConnection():
    #make the connection object global so we can use it globally in our code
    global cnx
    cnx = mysql.connector.connect(**config)
    #make the cursor object globally, this object will execute the SQL-query
    global cursor
    cursor = cnx.cursor()

#close the connection to the databae
def closeConnetion():
    cursor.close()
    cnx.close()

#Try and connect to database, otherwise print error message.
def connectToDB():
    try:
        #Try to connect to database with config
        getConnection()
        #if connection successful
        print("Connection established to database")
    #if connection attempt failed, do:
    except mysql.connector.Error as err:
        if(err.errno == errorcode.ER_ACCESS_DENIED_ERROR):
            print("Something is wrong with your user name or password")
        elif(err.errno == errorcode.ER_BAD_DB_ERROR):
            print("Database does not exist")
        else:
            print(err)


#Creates SQL-query with testData to be uploaded
#Person = Database schema tabel name
add_person = ("INSERT INTO Person (Navn,Mobil, Epost) VALUES ('NTNU',73595000,'postmottak@adm.ntnu.no')")

#try and push data to the schema tabel
def pushToDB():
    #insert new person
    cursor.execute(add_person)
    #make sure data is committed to the database
    cnx.commit()

#SQL-statment to execute on database (retrive tuples)
#Navn, Mobil = Attributes in database scheme Person tabel
#Person = tabelName
query = ("SELECT Navn, Mobil FROM Person")

#query a select-statment from the database
def pullFromDB():
    cursor.execute(query)
    toString()

#format the output from the query
def toString():
    for (Navn, Mobil) in cursor:
        print() #print a space between each tuple that is beeing printed
        print("Person")
        print("Navn: " + Navn)
        print("Mobil: " + str(Mobil))


#Function to run testScript, Try to connect, push and pull data. then prensent data or errors to user.
def main():
    connectToDB()
    print("Will now try and push to database")
    pushToDB()
    print("It worked! lets see if we can retrive from the database as well")
    pullFromDB()
    print("did it work?, if so the database connection will now be closed")
    closeConnetion()

#run testScript
main()
