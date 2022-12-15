import random

# Vi skriver tre funktioner som heter Lättpoäng, Vanligtpoäng och SvårtPoäng för att få poängkoefficiente
def LättPoäng():
    return 1


def VanligtPoäng():
    return 2


def SvårtPoäng():
    return 3

    # Vi skriver tre funktioner som heter LättPlus, vanligtPlus, svårPlus enligt de tre tillgängliga nivåerna för att få två slumpmässiga siffror med hjälp av randomfångsfunktionen för att utföra beräkningar.


def Lättplus():
    NummerEtt, NummerTvå = random.randrange(1, 100), random.randrange(1, 100)
    return [NummerEtt, NummerTvå]


def VanligtPlus():
    NummerEtt, NummerTvå = random.randrange(100, 10000), random.randrange(100, 10000)
    return [NummerEtt, NummerTvå]


def SvårtPlus():
    NummerEtt, NummerTvå = random.randrange(10000, 1000000000), random.randrange(
        10000, 1000000000
    )
    return [NummerEtt, NummerTvå]


def Manyval3():

    # Först frågar vi användaren spelets svårighetsgrad
    FickKorrektNivå = False
    while not FickKorrektNivå:
        Nivå = input("välja önskad nivå (Lätt, Vanligt, Svårt): ")
        if Nivå in ["Lätt", "Vanligt", "Svårt"]:
            FickKorrektNivå = True
            Poäng = 0
            KorrektaSvar = 0
            FelSvar = 0

    # Så länge användaren inte har lämnat kommer han att få matematiska frågor kontinuerligt, så för att börja måste vi lägga in koderna i while.
    SlutApp = False
    # Till en början, genom att kontrollera användarens valda nivå med if, definierar vi två variabler nummerEtt och nummerTvå och värderar dem med de funktioner vi definierade ovan.
    while not SlutApp:
        if Nivå == "Lätt":
            NummerEtt, NummerTvå = Lättplus()

        elif Nivå == "Vanligt":
            NummerEtt, NummerTvå = VanligtPlus()
        elif Nivå == "Svårt":
            NummerEtt, NummerTvå = SvårtPlus()
        # Sedan räknar vi även ut rätt svar inuti While och lagrar det i variabeln RättSvar för jämförelse och betyg till användaren.
        RättSvar = NummerEtt + NummerTvå
        # Sedan skapar vi en variabel med namnet fråga och lagrar frågan vi ska ställa användaren i den.
        Fråga = "{0} + {1} = ".format(NummerEtt, NummerTvå)
        Svar = input(Fråga)
        Svar = int(Svar)

        # Sedan även inuti While, enligt den nivå som valts av användaren, sätter vi poängkoefficienten i variabeln PoängNivå. Sedan jämför vi användarens svar med rätt svar. Beroende på om det är rätt eller felaktigt lägger vi till eller subtraherar till hans poäng, vi lägger till en enhet till hans rätta eller felaktiga svar.
        if Nivå == "Lätt":
            PoängNivå = LättPoäng()
        elif Nivå == "Vanligt":
            PoängNivå = VanligtPoäng()
        elif Nivå == "Svårt":
            PoängNivå = SvårtPoäng()

        if Svar == RättSvar:
            Poäng += PoängNivå
            RättSvar += 1
            print("Jaaaa, Din poäng är:{0}".format(Poäng))
        else:
            Poäng -= PoängNivå
            FelSvar += 1
            print("otur men ge inte upp, Din poäng är:{0}".format(Poäng))
        # Det är också nödvändigt att kontrollera om användarens svar var bland våra förväntade eller inte. Om det är korrekt sätter vi värdet på variabeln FortsättSvar till True, så att användaren inte kommer att få utgångsfrågan igen.

        FortsättSvar = False
        while not FortsättSvar:
            AnvändareFortsätt = input("Vill du forstätta spela? (Ja/Nej)")
            if AnvändareFortsätt == "Nej":
                SlutApp = True
            if AnvändareFortsätt in ["Ja", "Nej"]:
                FortsättSvar = True
        # I slutet, efter huvud-While, lägger vi följande kodbit och den exekveras när användaren vill avsluta programvaran och spelstatistiken, som inkluderar poäng, antal besvarade frågor, korrekta svar och felaktiga svar.
    else:
        print("Din poäng är: {0}".format(Poäng))
        print("du svarde på {0} frågor".format(KorrektaSvar + FelSvar))
        print("dina Rätt svar: {0}".format(KorrektaSvar))
        print("Dina Fel svar: {0}".format(FelSvar))
