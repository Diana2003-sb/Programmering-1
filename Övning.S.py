"""""
import random

nummer = random.randint(1, 100)
Antal_gissningar = 0
Användare_namn = input("Hej, vad heter du?")
print("Bra", Användare_namn, "Jag gissar ett nummer meellan 1 och 100 ")
while Antal_gissningar < 5:
    gissa = int(input())
    Antal_gissningar += 1
    if gissa < nummer:
        print("Din gissning är för låg")
    elif gissa > nummer:
        print("Din gissning är för hög ")

    elif gissa == nummer:
        break
if gissa == nummer:
    print("Du gissade numret\n" + str(Antal_gissningar) + "försök")
else:
    print("Du kunde inte gissa numret, nummret var"  + str(nummer))
"""

"""
def leap(year): 
    if year %4==0:
      print("det ä ett skottår")
    else:
         print("det är inte ett skottår. Fösrök igen")

year1 =int(input("skriv ett tal \n")) 
leap(year1)
"""
# Travelbag
# Skelettkod till uppgiften


accounts = {"diana": "donya-1382", "Alex": "12345", "lucy": "2000", "dinna": "2010"}
logged_in = False
while True:
    tries = 0

    menyval = input(
        "1. Skapa konto\n"
        "2. Logga in\n"
        "3. Läs en rolig historia\n"
        "4. Logga ut\n"
        "5. Avsluta program\n"
    )
    # TODO Skapa ett konto genom att lägga till ett key-value par i accounts
    # username = key
    # , password = value
    # Bonus: Kolla först så att användaren inte redan finns
    if menyval == "1":
        user1 = input("username: ")
        pass1 = input("password: ")

        if user1 in accounts:
            print(f"Det här konto har redean registerat på hemsidan")

            break
        else:

            accounts.update({user1: pass1})
            print(accounts)
            print("du har skapat en konto.")

    elif menyval == "2":
        # TODO Användaren ska få logga in med username och password
        # Ändra variabeln logged_in till True om de lyckas logga in
        # Bonus: Ge användaren ett visst antal försök att logga in
        while tries < 3:
            user2 = input("username: ")
            pass2 = input("passwords: ")
            if user2 in accounts and accounts[user2] == pass2:
                print("logged_in")
                logged_in = True
                break
            else:
                print("fel med username eller password, försök igen")
            tries += 1

    elif menyval == "3":
        while tries < 3:
            user3 = input("Username:  ")
            pass3 = input("Password:  ")
            if user3 in accounts and accounts[user3] == pass3:
                print(
                    "logged in, visste du att Kalle Anka var länge förbjudet i Finland eftersom han inte har byxor.. Hahahaha"
                )
                logged_in = True
                break
            else:
                print(
                    "fel med username eller password försök igen\n var inte orolig tänk på att det är omöjligt att andas och svälja samtidigt. Hahahaha"
                )
            tries += 1

    elif menyval == "4":
        # TODO Ändra variabeln logged_in till False
        # Bonus: Fråga om de är säkra först
        while tries < 3:
            answer1 = input("är du säker på att logga ut? \n a)Ja \n b)Nej \n")
            if answer1 == "a":
                print("logged out")
                logged_in = False
                break
            else:
                print("du är fortfarande in i programmet")
                break
    elif menyval == "5":
        print("programmet avslutas")
        break
