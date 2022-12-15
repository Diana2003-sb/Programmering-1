def Derivera(KVärde, AVärde):
    return "{0} *x^{1}".format(KVärde * AVärde, AVärde - 1)


def Derivera2(Kvärde, AVärde, VärdepåX1):
    return (Kvärde * AVärde) * VärdepåX1 ** (AVärde - 1)


def Menyval2():
    print("Välkommen till Derivatavsnittet!")
    # Fråga användare om värden k, m och a
    KVärde = int(input("k = "))
    AVärde = int(input("x** "))
    MVärde = int(input("m = "))

    # Ekvationen för rätt linje är y=kx^a+m

    print(Derivera(KVärde, AVärde))

    # Man deriverar så att y`= k*a*x^a-1+0
    # Här frågar vi användraen om hen vill sätta ett tal istället för X eller inte
    VärdepåX = input("Vill du räkna f(x)?\n A)Ja\n B)Nej\n")
    if VärdepåX == "Ja":
        VärdepåX1 = int(input("x= "))
        # Sätt vi talet på X

        print(Derivera2(KVärde, AVärde, VärdepåX1))
    # Programet avslutas
    else:
        print("Programmet Avslutas")
