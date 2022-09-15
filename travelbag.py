"""""
travelbag = ["kläder", "skor", "Laddare","Badkläder"]
print(travelbag[0])
print(travelbag[-1])
print(*travelbag)
travelbag.append("Hörlurar")
print(*travelbag)
travelbag.remove("skor")
print(*travelbag)
en_travel= travelbag.pop()
print(en_travel)
"""""

travelbag = ["kläder", "skor", "Laddare","Badkläder"]
name=input("vad heter du?")
print("välkomen", name, "till min progam.Jag ska resa och behöver din hjälp för att plocka upp mina saker.")
while True:
    menyval = input("1. Kolla i resväskan\n"
                   "2. Lägg sak i resväskan\n"
                   "3. Ta bort sak i resväskan\n"
                   "4. Avsluta program\n")
    if menyval == "1":
        print(*travelbag)
    elif menyval == "2":
      name=input()
      travelbag.append(name)
      print(*travelbag)
    elif menyval == "3":
      name=input()
      travelbag.remove(name)
      print(*travelbag)

    elif menyval == "4":
             break