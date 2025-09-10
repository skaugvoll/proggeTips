from tkinter import *
from Kalkulator import Kalkulator
from Fag import Fag



class userInterface(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        self.lb
        self.fagListe = []
        self.addBtn
        self.delBtn
        self.fag
        self.karakter
        self.kalkulator = Kalkulator()



    def initUI(self):
        self.parent.title("NTNU Gjennomsnittskalkulator")
        self.pack()
        l = Label(self,text="IMEs masterkalkulator")
        l.pack()
        self.createListView()
        self.createInputField()
        self.createBtns()
        self.createLabel("Ditt mastersnitt er")
        self.karakter = Label(self.parent, text="[Ikke nokk data]")
        self.karakter.pack()

    def createListView(self):
        self.lb = Listbox(self, width=60, height=30)
        self.lb.pack(expand=True, pady=(2,2))

    def fillListView(self): # Listbox
        self.lb.pack(expand=True, pady=(2,2))

    def updateListView(self, fag):
        if(fag == None ):
            print("Not fag object")
        else: #bare et fag sendt inn
            if(not self._checkExsistInView(fag)):
                self.fagListe.append(fag)
                self._addToListBox(fag.toString())
        #else: # en liste med fag er sendt inn
        #    for subject in fag:
        #        if(not self._checkExsistInView(subject)):
        #            self._addToListBox(fag)
        #            self.fagListe.append(subject)
        #        else:
        #            pass
        self.fillListView() #fyll inn fagene på skjermen


    def _checkExsistInView(self,fag):
        if(fag not in self.fagListe):
            return False
        else:
            return True

    def _addToListBox(self,fag):
        for i, listbox_entry in enumerate(self.lb.get(0, END)):
            if listbox_entry == fag:
               break

        self.lb.insert(END,fag)



    def _delFromListBox(self,fag):
        for i, listbox_entry in enumerate(self.lb.get(0, END)):
            if listbox_entry == fag.toString():
                self.lb.delete(i)
        for j in range(len(self.fagListe)):
            if(self.fagListe[j].toString() == fag.toString()):
                self.fagListe.__delitem__(j)



    def createInputField(self):
        # Inputbox
        label = Label(self,text="Fyll inn: Emne navn, Emnekode, Studiepoeng, Karakter")
        label.pack(after=self.lb)
        self.fag = Text(self, width=35, height="2", bg = "black", fg = "orange" )
        self.fag.config(insertbackground="orange")
        self.fag.focus_set()
        self.fag.pack(side="left", padx=1)

    def createBtns(self):
        #add button
        self.addBtn = Button(self, text="Add", height=2, width=5, fg = "orange", bg = "black", command = self.addBtnClicked)
        self.delBtn = Button(self, text="Del", height=2, width=5, fg = "orange", bg = "black", command = self.delBtnClicked)
        self.addBtn.pack(side="right",padx=1)
        self.delBtn.pack(side="right")


    def addBtnClicked(self):
        input = [self.fag.get("1.0",END).rstrip()]
        info = input[0].split(",")
        if(input[0] =="\n" ):
            pass
        elif(len(info)==4):
            fag = self._createFag(info[0],info[1],info[2],info[3])
            self.updateListView(fag)
            self._calcAndShowAverage()
        else:
            print("Not valid")


    def _calcAndShowAverage(self):
        #calculate currently average
        self.kalkulator.regnGjennomsnittet(self.fagListe)
        try:
            self.karakter.config(text=self.kalkulator.getGjennomsnitt())
        except Exception:
            self.karakter.config(text="[Not enough Data]")


    def delBtnClicked(self):
        print("delbtn clicked")
        #pass
        input = [self.fag.get("1.0",END).rstrip()]
        info = input[0].split(",")
        if(input[0] =="\n" ):
            pass
        elif(len(info)==4):
            fag = self._createFag(info[0],info[1],info[2],info[3])
            self._delFromListBox(fag)
            self._calcAndShowAverage()
        else:
            print("Not valid")


    def createLabel(self,text):
        label = Label(self.parent,text=text)
        label.pack()


    def _createFag(self,navn,kode,sp,k):
        return Fag(navn,kode,float(sp),k)


