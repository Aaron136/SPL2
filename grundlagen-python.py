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