


from ast import Return
from distutils.errors import LibError
from os import remove
from re import I
from telnetlib import Telnet
from tkinter import Y

def Hej(name):
        print(f"Hej", name,"du är bäst")
Hej("Diana")

def f(x):
    return x+1
print(f(5))
print(f(9))

def f(x):
    x <1
    return -1*x
print(f(-3))
print(f(-5))

def f(x):
    return x**2
print(f(2))
print(f(10))

def summan(a,b):
    return a+b
print(summan(8,9))
print(summan(10,2))

def största(a,b,c):
    if a > b and a>c:
        print(a, "är störst.")
    elif c>b and c>a:
        print(c, "är störst")
    elif b>c and b>a:
     print(b, "är störst")
största(5,7,9)
största(6,10,5)
största(20,8,19)
def lista(x):
    summan=0
    for nr in x:
          summan+=nr
    print(summan)
lista([2,5,8])
lista([3,6,7,9,10])

import random

def tal(gammallista) :
    nylista = []
    for sak in gammallista:
        if sak not in nylista: 
            nylista.append(sak)
            print(nylista)
tal([2,3,4,5,7,8,2,3,5,6])
tal([2,2,3,5,3,7,4])

def primtal(nr):
    for i in range (2,nr):

        if nr % i== 0:
            return 'False'

    return 'true'
primtal(2)
primtal(3)
print(primtal(37))   
print(primtal(20))
 

def ord(world1):
    world2 = world1[::-1]
    if world1==world2:
        return'true'
    else: 
        return'false'    
print(ord("tenet"))
print(ord("love"))

