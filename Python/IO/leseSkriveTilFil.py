# coding=utf-8
#Du trenger filen nøkler.txt for å kunne kjøre dette programmet.

def hashFunksjon(nøkler):
    '''
    Dette er en funksjon som lager en liste på formen [(tuppel),(tuppel),...], hvor tuppel består av 3-attributter;(nøkkel,verdi,binært).
    Funksjonen kjører igjennom hver nøkkel/ element i nøkler-listen som blir sendt inn som argument. Funksjonen regner ut modulo 128 på hver nøkkel (heltall/desimaltall),
    oversetter hver verdi til bineær representasjon, og fjerner suffixen 0b fra konverteringen som sier at verdien er bineær.
    Til slutt legger funksjonen nøkkelen, verdien, bineærVerdien til i listen som skal returneres som en tuppel.
    Når funksjonen har gjort dette for alle nøkler i parameterlisten nøkler, returnerer funksjonen den nye listen som inneholder tupplene.
    '''
    resultat = []                                                   #Oppretter en tom liste som vi skal legge til tuplene våre i, og returnerer til slutt.
    for nøkkel in nøkler:                                           #For hver nøkkel/element i listen nøkler(parameter-listen), ønsker vi å gjøre følgende... 
        verdi = nøkkel % 128                                        #Utfører modulooperasjon på nøkkel, og lager resultatet i variabelen verdi.
        binært = bin(verdi)[2:]                                     #Konverterer verdi-tallet til bineær representasjon og returner 0b**** hvor * er bineær representasjon og 0b er lagt til som suffix for å poengtere at det er bineært.
                                                                    #[:2] fjerner suffixen som vi vet har lengden til 2 karakterer. Dette vil si at tallet vårt begynner på indeks 2 i strengen. (husk 0-indeksert) [x:y], fra og med 'x', til 'y' (ikke inklusiv).
        resultat.append((nøkkel,verdi,binært))                      #Legger alle verdiene til på slutten av listen, som tuppel.
    return resultat                                                 #Returnerer listen med alle tuplene.


def skrivTilSkjerm(resultatSet):
    '''
    Dette er en funksjon som kjører igjennom listen resultatSet som er på formen [(nøkel,verdi,binært),(nøkel,verdi,binært),..],
    og så printer funksjonen ønsket informasjon (i dette tilfellet alle tre attributtene i tuplen) til indeksen i listen vi er på til skjerm.
    '''
    print("Nøkkel" + "\t" + "des" + "\t" + "bin")                   #Printer ut en header for å forklare brukeren betydningen av det som blir printet ut i tabellen.
    print("-" * 20)                                                 #Printer bare en streng for å poengtere slutt på header.
    for nøkkel,verdi,binært in resultatSet:                         #Her er det greit å nevne at selv om attributtene i tupplen i listen heter/er lagret som (nøkkel,verdi,binært),
                                                                    #trenger vi ikke å kalle variablene som vi ønsker å lagre respektiv tuppelattributt i, det samme som attributten. Vi kunne skrevet for k,d,t in resultatSet, hvor vi tenker at k = key, d = decimal, t = twoCompliment/binary).
        print(str(nøkkel) + "\t" + str(verdi) +"\t"+ str(binært))   #Printer informasjonen fra tuplene i listen til skjermen på brukervennlig format.



def lesOgReturnerNøkkler(filSti):
    '''
    Det er veldig viktig å bruke try-except når man jobber med lesing og skriving til fil. Dette fordi det er veldig
    lett å få exceptions/feil ved denne type programmering. Plutselig kan det være at filen man ønsker å åpne ikke finnes, og da vil
    det kaste en exception. Filen kan ha blitt korrupt, osv. 
    '''
    try:
        fil = open(filSti,"r")                  #Åpne filen som blir lokalisert av filsti, "r" - åpningsfunksjon. "r" = read/les,
                                                #og setter lesepekeren/filpekeren på starten av filen vi åpner.
        nøkler = []                             #Oppretter en tom liste, som vi skal fylle opp, med verdiene som befinner seg på hver linje i filen. En linje, en nøkkel.
        for linje in fil:                       #For hver linje med tekst som ønsker vi å utføre i filen. (hust at hver linje slutter med '\n' (tegnet for ny linje)).
            #print(str(linje))                  #Kommenter inn denne, hvis du vil se hva som er på hver linje.
            nøkkel = linje.strip()              #Siden vi leser en linje, og hver linje slutter med '\n' må sistnevnte fjernes. Det gjør vi med .strip()
            nøkkel = int(nøkkel)                #Siden vi ønsker å legge til en nøkkel som et tall og ikke en streng. Alt vi leser fra en fil, blir tolket som streng /str(). Så er det tall, må vi gjøre det om til tall.            
            nøkler.append(nøkkel)               #Legg til nøkkelen til linjen vi står på.
        fil.close()                             #Viktig å huske å lukke filen, spesielt  når man skriver til fil. Da blir alle endringer og alt som skal skrives til filen
                                                #'flushet', og vi er sikre på at alt blir lagret.
        return nøkler                           #Returnerer den nye listen vi har laget med alle nøklene i filen som int(heltall)
    
    except Exception as IOexception:
        print(str(IOexception))                 #Hvis exception, printes det ut hva som gikk feil, og programmet krasjer ikke.
        


def skriveTilFil(filSti,resultatSet):
    '''
    Dette er en metode for å skrive til fil, Det er også her viktig å bruke try-except når man skal jobbe med lesing og skriving til fil. Dette kalles også for IO (input output) og det er et vanlig tilfelle at IOexception blir kastet.
    Denne metoden skriver en header - beskrivelse til filen når den åpnes. Dette skjer bare en gang. Etter dette prøver funksjonen å skrive ønsket data til filen på ønsket format.
    Viktig å merke seg at man legger til '\n' (linjeskift) på slutten av hver linje. Dette for å skrive/fortelle filen at nå er denne linjen ferdig og man vil begynne å skrive på neste. Brukes bare når linjeskift er ønskelig.
    Hvis det av en eller annen grunn ikke går an å skrive til filen, kastes exception. Det blir så fanget av except, og så printet til terminalen/brukeren slik at man oppdager at skrivingen ikke var vellykket, og kan se hva som gikk feil.
    '''
    try:
        fil = open(filSti, "w")                 #Åpne filen som blir lokalisert av filsti, "w" - skrive funksjon. "w" = write/skriv. Hvis filen ikke eksisterer på gitt filsti, opprettes det en .txt fil med det navnet på gitt filsti,
                                                #for å skrive til en fil - på slutten av filen som allerede eksisterer, kan du bruke "a" - append / legg til.
        fil.write("Nøkkel:\tDes:\tBin:"+"\n")   #Skriver en linje på toppen av tekstfilen som beskriver hva informasjonen som kommer under betyr/er. '\t' = et trykk på tab-knappen (ekvivalent med 4 mellomrom). LEGG MERKE TIL(!) at jeg også skriver '\n' i strengen jeg skriver til filen, dette for å si at nå er denne linjen ferdig og jeg skal begynne på neste. Dette MÅ være med for å få linjeskift!!
        fil.write("-"*20 + "\n")                #Skriver en linje med tjue "-" tegn for å poengtere at på neste linje begynner dataen.   LEGG MERKE TIL '\n', Ønsker et linjeskift nå! 
        for tuppel in resultatSet:              #For hver tuppel i resultatSet, gjør følgende...
            nøkel = tuppel[0]                   #Henter ut nøkkel fra tuppel og lagrer i lokal variabel til funksjonen.
            modulo = tuppel[1]                  #Henter ut moduloresultat fra tuppel og lagrer i lokal variabel til funksjonen.
            binært = tuppel[2]                  #Henter ut binær representasjon fra tuppel og lagrer i lokal variabel til funksjonen.
            fil.write(str(nøkel) + "\t" + str(modulo) + "\t" + str(binært) +"\n") #Skriver ønsket informasjon/data til filen, + "\n" (tegnet for ny linje) for å poengtere at vi skal hoppe til ny linje og skrive på den.
        fil.close()                             #Lukker og flusher til filen når vi er ferdig å skrive til filen. På denne måten sørger vi for at alt vi ønsker å skrive til filen, faktisk blir skrevet.
        print(fil.closed)                       #Skriver en boolean True til skjermen om filen er lukket, og False om lukkingen av filen feilet.
        print("Skriving til fil vellykket.")    #Skriver en beskjed til brukeren om at skriving til fil var vellykket.
                
    except Exception as IOexception:
        print(str(IOexception))                 #Hvis det oppstår noen feil under prøving av skriving til filen, blir en exception kastet, da utføres denne linjen som printer hva som gikk feil til terminalen/brukerne, uten å krasje programmet.


def main():
    '''
    Leser fra fil, og behandler data fra filen. Printer så informasjonen.
    Skriver data vi behandler til ny fil på brukervennlig format
    '''
    filSti = "nøkler.txt"                                        #Dette kan være en absolutt filsti, eller en relativ (brukt i dette eksemplet). Oppretter en variabel som inneholder stien til filen vi ønsker å lese fra. Absolutt sti-eks: C:/Users/UserName/Desktop/nøkler.txt
    nøkler = lesOgReturnerNøkkler(filSti)                        #Leser igjennom linje for linje i filen, tar vare på informasjonen/ manipulerer informasjonen, returner den og tar vare på ønsket informasjon fra filen.
    resultatSet = hashFunksjon(nøkler)                           #Sender informasjonen vår inn til en funksjon som videre manipulerer og utfører noe på informasjonen og vi får tilbake ønsket data/repesentasjon av dataene fra filen vi leste fra og lagret.
    skrivTilSkjerm(resultatSet)                                  #Skriver ut informasjonen fra filen ferdig manipulert/prosessert til skjerm på en brukervennlig måte.


    filSti = "nøklerOversatt.txt"                                #Dette kan være en absolutt filsti, eller en relativ (brukt i dette eksemplet). Oppretter en variabel som inneholder stien til filen vi ønsker å skrive til. Absolutt sti-eks: C:/Users/UserName/Desktop/nøklerOversatt.txt
    skriveTilFil(filSti,resultatSet)                             #Funksjonskall til skriveTilFil, med argumentene filSti og resultatset, som prøver å åpne filen på angitt filsti. Hvis den ikke allerede eksisterer, blir filen opprettet. Prøver å skrive ønsket data til filen, skriver så en beskjed til brukeren hvis skrivingen var vellykket, eller hvis noe gikk galt.
    
    

main()
