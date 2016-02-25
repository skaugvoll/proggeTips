#Laget av Sigve Skaugvoll
#Skrevet: 25.02-16
#Versjon: Python3.4.3

#Dette er et script for å demonstrere % formatteringen.
#Viktig og merke seg at % er den gammle syntaksen for å formatere.
#Den nye er nå: '{0}, {1}, {2}'.format('a', 'b', 'c') hvor .format() inneholder variablene/verdiene vi ønsker å sette inn, og tallet inni {} i strenger spesifiserer hvilken indeks i .format()-listen vi ønsker å sette inn.
#Vi kan velge at 'b' skal komme før 'a' med --> '{1}, {0}, {2}'.format('a', 'b', 'c') fordi 0 = a, 1 = b, 2 = c
#Vill på det sterkeste anbefale å lære seg det nye formaterings syntaksen, da den er veldig veldig fin og lett å bruke!
#Generelle formen for å spesifiser formaterings krav    ":" [[fill] align] [sign] ["#"] ["0"] [width] [","] ["." prec] [type]

#Så la oss komme igang med %.

#Det første vi må, er å vite litt om syntaksen
#% brukes for å spesifisere at her vil jeg bytte ut %-tegnet med en bestemet variabel eller verdi.
#etter %-tegnet, skal det følge en character som spesifiser datatypen (string,int,float) = (s,d,f)
#La oss se hvordan dette fungerer.

#først trenger vi noen variabler som vi ønsker å putte inn i en streng.
navn = input("Hva heter du? ")
alder = int(input("Hva er din alder: "))
snitt =float(input("Hva er ditt snitt [float]: "))

print() #Denne er her bare for å lage mellomrom mellom input og eksempel

#Så trenger vi strengen vi ønsker å putte variabel verdiene inn i, og hvilke variabler/verider som skal inn i strengen.
#For å spesifiere hvilke variabler eller verdier som skal inn, skriver vi %(v1,v2,v3,..vN) etter tekst strengen vår (merk. dette er ikke en ny streng!, eller del av " "-strengen som vi ønsker å putte inn i. Men kommer rett etter)
#Det er viktig og huske på at når vi ønsker å sette inn et float tall med %f, så er standard presisjon på floattallet satt til å være 6 tall etter komma. så skriver vi 4.555 får vi 4.555000 fordi det skal være
#6 tall bak komma hvis vi ikke spesifiserer det. Dette kan vi endre, så ta det med ro :)
#Strenger vi ønsker å bytte ut/ sette inn verdier i heter formatertStreng.

print("Eksempel 1: Innsetting")
formatertStreng = "Mitt navn er: %s, jeg er %dår og har et snitt på %f" %(navn,alder,snitt)

print() # denne er her bare for å lage mellomrom mellom dette og neste eksempel

#Legg merke til at det kommer et ',' rett etter '%s' i den formaterte strengenr og at ',' kommer med i den formaterte strenger. Altså så stopper datatype charactern selve utbyttings/innsettings uttryket
#og vi kan fortsette å skrive strengenr vår rett etter datatype erklæringen. 
#Så kan vi printe ut strengern, med det navnet, alderen og snittet vi skrev inn.
print(formatertStreng)

#Hmm, nå som vi har sett at dette funker, og skjønner hva %-tegnet og charactern som kommer etter betyr. Lurer du kansje på om det er alt. det kan vi jo gjøre med å bare plusse på
#variablene i strengen, f.eks. på denne måten formatertStreng = "Mitt navn er: "+navn", jeg er "+alder " år og har et snitt på " + snitt
#Men %-tegnet tillater oss å gi krav til utbyttingen/innsettingen av variabel/verdier.

#La oss si at vi ønsker å sette av 20tegn/characters til navnet, slik at det alltid vil oppta 20charaters eller flere, og at vi ønsker å formatere floattallet til å bare inneholde 2tegn etter komma.
#dette lar %-tegnet oss gjøre veldig enkelt, ryddig og effektivt!
#Syntaksen for dette er å plassere krav mellom %-tegnet og charatern som bestemmer datatypen. eks. %20s  Dette setter av 20tegn i strengen. hvis vi setter inn en verdi som er mindre en 20 tegn lang
#vil strengen bli printent med blanke tegn etterfulg av navnet. antall blanke tegn er antall characters satt av  - characters i verdi satt inn.

#syntaksen for å spesifisere hvor mange tall etter komma,[prosentPunktumHvormangetallDatatype] --> f.eks 2 tall etter komma --> %.2f 

#Nå la oss prøve dette med verdiene vi skrev inn først.

print("Eksempel 2: Formatering")
formatertStreng = "Mitt navn er: %20s, jeg er %dår og har et snitt på %.2f" %(navn,alder,snitt)
print(formatertStreng)

print() #Denne er her for å lage mellomrom mellom dette og neste eksempel

#Hmm, dette såg jo litt rart ut. navnet blir satt etter de blanke tegnene. Det var ikke så pent å se på. Dette kan fikses med å legge til - mellom % og antall plasser vi ønsker å oppta
#for å spesifisere at vi ønsker å sette inn veriden helt til venstre også sette inn blanke tegn. (med andre ord, sette inn verdien også blanke tegn. ikke motsatt som er standard slik vi så over).
#Viktig å legge merke til at det som kommer etter datatypen blir ikke med i formateringskravet. Ergo --> ',' vil komme etter at de 20 avsatte tegnene til navn.
print("Eksempel 3: Formatering med Krav")
formatertStreng = "Mitt navn er: %-20s, jeg er %dår og har et snitt på %.2f" %(navn,alder,snitt)
print(formatertStreng)

print() #Denne er her for å lage mellomromm mellom dette og neste eksempel

#Hvis du ønsker å sette av et hviss antall karaterer til float tallet også, med foramtierng på 2 tall etter komma gjøres det på denne måten [prosentAntallkaraktersomskalopptaesPunktumAntalltallbakkomma] --> %33.2f
#Dette vil sette av 33 karakterer til et floattall, med to tall etter komma.

print("Eksempel 4: Formatering med Krav.2")
formatertStreng = "Mitt navn er: %-20s, jeg er %dår og har et snitt på %33.2f" %(navn,alder,snitt)
print(formatertStreng)

print() #Dette er her for å lage mellomrom mellom dette og neste eksempel.

print("Eksempel 3: Formatering med Krav.3")
formatertStreng = "Mitt navn er: %-20s, jeg er %dår og har et snitt på %.2f" %(navn,alder,snitt)
print(formatertStreng)

print() #Dette er her for å lage mellomrom mellom dette og neste eksempel

#Hvis du ønsker å formatere et float tall, med ledende nuller i den plassen som blir satt av men ikke blir brukt av float tallet til variablen/verdien
#kan vi skrive [prosentNullAntallkaraktersomskalopptaesPunktumAntallsifferetterkommaDatatype] --> %010.2f
#Her blir det satt av 10 tegn til et float tall, med en presisjon på 2 tall etter komma. Hvis float tallet ikke opptar 10 siffer. blir det puttet inn så mange nuller
#som det trengs foran tallet før komma, slik at tallet floattallet opptar 10tegn

print("Eksempel 4: Formatering med krav.4")
formatertStreng = "Mitt navn er: %-20s, jeg er %dår og har et snitt på %010.2f" %(navn,alder,snitt)
print(formatertStreng)

print() #Dette er her for å lage mellomrom mellom dette og neste eksempel

#Dette kan taes videre, og føres til for eksempel formateringen av et integer det har helt samme syntaks, man kutter bare det som er spesifikt for float, altså tall etter komma.
#[prosentNullAntallkaraktersomskalopptaesDatatype]
#så hvis vi skriver %05d blir det satt av 5 tegn til integer, hvis integer er mindre en fem karakter blir det satt inn så mange 0er som mangler for at int skal være 5tegn
#framfor selve tallet.

print("Eksempel 5: Formatering med krav.5")
formatertStreng = "Mitt navn er: %-20s, jeg er %05dår og har et snitt på %.2f" %(navn,alder,snitt)
print(formatertStreng)

print() #Dette er her for å lage mellomrom mellom dette og neste eksempel

#Selvfølgelig siden du nå har lært å sette inn null framfor integer og float tall i formateringen, lurer du sikkert på om vi kan gjøre det samme for strings
#Svaret er ja! Da lurer du kansje på hvordan? Den enkleste måten å gjøre dette på er med den nye syntaksen. Introdusert øverst i dette scriptet i kommentaren.
#Man skriver altså {} i strengern hvor man ønsker å putte in variabel/verdi. Inni denne kan man oppgi forskjellige ting for å spesifisere forskjelligeting. for å gi bedskjed til python at det man skriver skal tolkes
#som formaterings krav skriver man ':' inni {}. Da vet Python at det som kommer nå er kravene. formen er i dette eksemplet velger jeg å bruke * som fyll karakter. ^ betyr at variablen/verdien skal være midt i fyllet
#20 betyr hvor mange characters som skal settes av til variablen/verdien. og fyll karakteren blir gjentatt så mange ganger som det mangler tegn for å fylle opp avsatt. 
#

print("Eksempel 6: Formatering med krav.6")
formatertStreng = "Mitt navn er: {:*^20}, jeg er  {}år og har et snitt på {:.2f}".format(navn,alder,snitt)
print(formatertStreng)
