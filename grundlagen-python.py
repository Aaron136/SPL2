# grundlagen-python.py

# Kommentare erfolgen mit hashtag

# Ausgabe von Daten 
print("Hello World")

# Variable definieren (kann ohne Typ erfolgen)
heimat = "Erde"

print(heimat, "an World: ", "Hallo")

# Eingabe
wer = input("Und wer bist du? ")

# und gibt den Text wieder aus
print("Hallo", wer)

if(wer == "ich"):
    print ("Hallo Du!")
else:
    print ("Hallo ", wer)

lieblingszahl = input("Was ist deine Lieblingszahl?")
print("Super, ich mag die Zahl ", lieblingszahl)
print("Aber die groessere Zahl", int (lieblingszahl)+10, "mag ich noch mehr!")

runden = input("Wie viele Runden sollen wir spielen")
runden = int(runden)

for runde in range(1,runden):
    print ("Runde", runde, "von", runden, ": Sieger:","ich")

# zufallszahl erzeugen
zufallszahl = random.randint(1,6)
# zufallszahl 1 3 5 ich bin sieger
# sonst computer
if (zufallszahl == 1 or zufallszahl == 3 or zufallszahl == 5):
    sieger = "ich"
else:
    sieger = "computer"
   print("Runde", runde, "von", runden, ": Sieger:", sieger, ": gewuerfelt wurde:", zufallszahl)
if (siege_ich > siege_computer):
    print("Du gewinst!")
elif(siege_ich < siege_computer):
    print("Du verlierst!")
else:
    print("Unentschieden")
print ("Game Over")