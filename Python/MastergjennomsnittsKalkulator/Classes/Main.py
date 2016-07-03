from Fag import Fag
from Kalkulator import Kalkulator
from GUI import userInterface
from tkinter import *

#obligatoriske fag
IT1901 = Fag("Informatikk prosjektarbeid 1","IT1901",7.5,'C')
IT2901 = Fag('Informatikk prosjektarbeid 2',"IT2901",15,'E')
TDT4100 = Fag("Objektorientert programmering","TDT4100",7.5,'A')
TDT4120 = Fag("Algoritmer og datastrukturer","TDT4120",7.5,'D')
TDT4140 = Fag("Programvareutvikling","TDT4140",7.5,'B')
TDT4145 = Fag("Datamodellering og databasesystemer","TDT4145",7.5,'B')
TDT4160 =  Fag("Datamaskiner grunnkurs","TDT4160",7.5,'B')
# EVT. byttes ut med TDT 4160 --> TDT4186 = Fag("Operativsystemer","TDT4186",7.5,None)

#3 valgfrie IT / TDT fag
IT2805 = Fag("Webteknologi", "IT2805",7.5,'A')
TDT4110 = Fag("ITGK","TDT4110",7.5,'C')
TDT4180 = Fag("Menneske-Maskin interaksjon","TDT4180",7.5,'C')

#ikke valgt som å telle, men har mulighet.
IT1603 = Fag("IKT, kultur og samfunn","IT1603",7.5,'D')

emneliste = [IT1901,IT2901,TDT4100,TDT4120,TDT4140,TDT4145,TDT4160,IT2805,TDT4110,TDT4180]

def calc(listeMedFag):
    kalk = Kalkulator()
    kalk.regnGjennomsnittet(listeMedFag)
    gjsnitt = str(kalk.getGjennomsnitt())
    print("Antall Fag: " + str(len(listeMedFag)) + "\nGir snitt " + gjsnitt)
    return gjsnitt

#calc(emneliste)

def main():
    #lag vindu,
    root = Tk()
    #lag kalkulator objekt
    kalk = Kalkulator()
    #modifiser vindu:
    GUI = userInterface(root)
    #GUI.createListView()
    #GUI.createInputField()
    #GUI.createBtns()
    #GUI.createLabel("Ditt mastersnitt er")
    #kalk.regnGjennomsnittet(emneliste)
    #GUI.createLabel(kalk.getGjennomsnitt())

    #set vindu, størrelse
    root.geometry("400x620")
    #start vindu / vis vindu
    root.mainloop()

main()