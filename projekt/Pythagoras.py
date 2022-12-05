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
    "Nu vet du att dessa tal är en pythagoras tal eller inte, vill du Vill du se Pythagoras tal mindre än 100? A) Ja\n, B) Nej\n"
)
if Fråga1 == "A":
    c, m, limits = 0, 2, 100
# Limiting c would limit
# all a, b and c
while c < limits:
    # Now loop on n from 1 to m-1
    for n in range(1, m):
        a = m * m - n * n
        b = 2 * m * n
        c = m * m + n * n
        # if c is greater than
        # limit then break it
        if c > limits:
            break
        print(a, b, c)
    m = m + 1

else:
    print("Programet avslutas")
