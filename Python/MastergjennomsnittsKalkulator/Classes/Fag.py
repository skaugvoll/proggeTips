class Fag:
    def __init__(self,navn,emnekode,studiepoeng,karakter):
        self.navn = navn
        self.emnekode = emnekode
        self.studiepoeng = studiepoeng
        self.karakter = karakter

    def giNavn(self,navn):
        if(self.validerNavn(navn)):
            self.navn = navn

    def getInfo(self):
        return {"Navn" : self.navn, "Emnekode" : self.emnekode , "Karakter" : self.karakter, "Studiepoeng" : self.studiepoeng}

    def toString(self):
        return (str(self.emnekode) + " " + str(self.navn) + " ,Studiepoeng: " + str(self.studiepoeng) + " ,Karakter: " + str(self.karakter))