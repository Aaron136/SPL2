# zahlenraten.py
import random
max = 200
zufallszahl = random.randint(1,200)
gewonnen = False
versuche = 0
print("Bitte gib eine zahl zwischen 1", max, "eingeben")

while(gewonnen == False):
    zahl = input("Welche Zahl?")
    zahl = int(zahl)
    if (zahl == zufallszahl):
        gewonnen = True
        print("Du hast gewonnen!")

    if(zahl < zufallszahl):
        print("Die Zahl ist größer")
        versuche+1
        zahl = input("Welche Zahl?")

    if(int (zahl) > zufallszahl):
        print("Die Zahl ist kleiner")
        versuche+1
        zahl = input("Welche Zahl?")
