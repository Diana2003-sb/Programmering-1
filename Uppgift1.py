from unicodedata import name

Name=(input("Vad heter du?"))
print("Hej!",Name,"väkommen till Quiz")
age=int(input("Om vi ​​vill starta tävlingen måste jag veta hur gammal är du?"))

if age >= 18:
    print("du är myndig", "vill du svara på svåraste frågorna eller enklare?")
    answer1=input("A. Svåraste \n B. Enklare\n "" ").capitalize()
    if answer1 == "Svåraste":
        input("du vill svara på svåraste frågorna, prees enter to continiue.")
    elif answer1 == "Enklare":
        input("du vill svara på enklare frågorna, prees enter to continiue.")
Point=0
if answer1 == "Enklare": 
    print("I vilket land ligger staden Rom? ")
    answer2 =input().capitalize()
    if answer2 == "Italien": 
        Point+= 2
        print("Rätt")
    else: 
        Point-=2
        print("Fel")

    print("Vilket år föddes Michael Jackson?")
    answer3= input("A. 1945\n B. 1958\n C. 1960\n "" ")
    if answer3 == "B":
        Point+= 2
        print("Rätt")
    else:
        Point-= 2
        print("fel")
    print("I vilket land är TV-kanalen Al-Jazira baserad?")
    answer4= input(). capitalize()
    if answer4 == "Quatar":
        Point+= 2
        print("Rätt")
    else:
        Point-= 2
        print("Fel")

    print("Vad kallas stjärnan på israels flagga?")
    answer5= input(). capitalize()
    if answer5 == "Davidstjärnan":
        Point+= 2
        print("bra jobbat!, du har fått",Point)
    else:
        Point-= 2
        print("fel!, du har fått",Point)
        
if answer1 == "Svåraste":
    point=0
    print("Vem uppfann grammofonen?")
    Answer7= input().capitalize()
    if Answer7 == "Berliner":
        point += 3
        print("Rätt")
    else:
        point-=3
        print("fel")
    print("Under vilket år släpptes The Godfather först?")
    Answer8= input("A. 1972\n B. 1980\n C. 1975\n """)
    if Answer8 == "A":
        point+=3
        print("Rätt")
    else:
        point-=3
        print("fel")
    print("Vad är världens minsta fågel?")
    Answer9= input("A. Björktrast\n B. Bee Hummingbird\n C. Entita\n """)
    if Answer9=="B":
        point+=3
        print("Rätt")
    else:
        point-=3
        print("Fel")
    print("Vilken klubb vann FA-finalen 1986?")
    Answer10= input().capitalize()
    if Answer10=="Liverpool":
        point+=3
        print("Rätt")
    else:
        point-=3
        print("Fel")
    
    print("Du har fått", point)
    if point in [6,9,12]:
        print("Bra jobbat, VAD DUKTIGT DU ÄR!")
    else:
        print("Tappa inte hoppet!")
