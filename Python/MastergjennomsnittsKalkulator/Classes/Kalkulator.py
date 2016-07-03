class Kalkulator:
    def __init__(self):
        self.studiepoeng = 0 # summer alle studiepoeng
        self.gjennomsnitskarakter = None #gjennomsnittskarater
        self.tempKarakter = 0 # emnekarakter * emnestudiepoeng

    def regnGjennomsnittet(self,emner):
        tempKarakter = 0
        if(len(emner) == 0):
            self.tempKarakter = 0
            self. studiepoeng = 0
            self.gjennomsnitskarakter = 0
            return

        for emne in emner:
            studiepoeng = 0
            karakter = 0
            aktuelltEmne = emne.getInfo()
            for key in aktuelltEmne:
                if key == "Studiepoeng":
                    studiepoeng = aktuelltEmne[key]
                    self.studiepoeng += aktuelltEmne[key]
                elif key == "Karakter":
                    if(aktuelltEmne[key] == "A"):
                        karakter = 5
                    elif(aktuelltEmne[key] == "B"):
                        karakter = 4
                    elif (aktuelltEmne[key] == "C"):
                        karakter = 3
                    elif (aktuelltEmne[key] == "D"):
                        karakter = 2
                    elif (aktuelltEmne[key] == "E"):
                        karakter = 1
                    else:
                        karakter = 0

            self.tempKarakter += karakter * studiepoeng
        self.gjennomsnitskarakter = self.tempKarakter / self.studiepoeng

    def getGjennomsnitt(self):
        if(self.gjennomsnitskarakter >2.5 and self.gjennomsnitskarakter < 3):
            return "C-grense"
        elif self.gjennomsnitskarakter > 3 and self.gjennomsnitskarakter < 4:
            return "B-grense"
        else:
            return str(self.gjennomsnitskarakter)

