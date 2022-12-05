# Först måste vi fråga av användare  om vilken sektion hen vill gå till.
from derivata import derivata

Namn = input("Hej!, Vad heter du?")
print("Välkommen", Namn, "till min program", "Vilken delen vill du gå till?\n")
Manyval = input("A) pythagoras tal\n ", "B) Derivata\n", "C) Math sepel\n")
if Manyval == "B":
    derivata()
