# Först, med hjälp av input-kommandot, får vi tre heltalsinmatningar från användaren.
A = int(input("Snälla, ange nummer ett: "))
B = int(input("Snälla, ange nummer två: "))
C = int(input("Snälla, ange nummer tre: "))
# Sedan, med hjälp av ett If, kontrollerar vi om kvadraten på varje tal är lika med summan av kvadraterna av de andra två talen eller inte.
if A * A == B * B + C * C or B * B == A * A + C * C or C * C == A * A + B * B:
    print("Ja")
else:
    print("Nej")
Fråga1 = input(
    "Nu vet du att dessa tal är en pythagoras tal eller inte, vill du se många Pythagoras tal?\nA)Ja\n B) Nej\n"
)
# Först definierar vi gränsvariabeln och tilldelar den värdet 100.
if Fråga1 == "Ja":
    GränsVariabel = 100
    # Sedan fortsätter vi med en for loop som loopar från ett till gränsvaribeln.
    for A in range(1, GränsVariabel):
        B = A + 1
        C = B + 1
        # I fortsättningen av for-slingan skriver vi en while-loop som upprepas och körs tills det mindre c:et är lika med gränsvariablen. I while-slingan, skriv en annan while-loop, som lägger till en enhet till c tills c*c är mindre än a*a + b*b.
        while C <= GränsVariabel:
            while C * C < A * A + B * B:
                C = C + 1
            if C * C == A * A + B * B and C <= GränsVariabel:
                print(A, B, C)
            B = B + 1

elif Fråga1 == "Nej":
    print("Programmet avslutas")
