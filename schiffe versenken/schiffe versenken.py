import random
Raster = [['.' for _ in range(6)] for _ in range(6)]
Schiffe = [['.' for _ in range(6)] for _ in range(6)]  
def markiere_punkte(feld, start_zeile, start_spalte, richtung, anzahl):
    if richtung == 'horizontal':
        for i in range(anzahl):
            feld[start_zeile][start_spalte + i] = 'X'
    elif richtung == 'vertikal':
        for i in range(anzahl):
            feld[start_zeile + i][start_spalte] = 'X'
def platziere_schiff(anzahl):
    while True:
        richtung = random.choice(['horizontal', 'vertikal'])
        if richtung == 'horizontal':
            start_zeile = random.randint(0, 5)
            start_spalte = random.randint(0, 6 - anzahl)
        else:
            start_zeile = random.randint(0, 6 - anzahl)
            start_spalte = random.randint(0, 5)
        if alle_felder_frei(Schiffe, start_zeile, start_spalte, richtung, anzahl):
            markiere_punkte(Schiffe, start_zeile, start_spalte, richtung, anzahl)
            break
def alle_felder_frei(feld, start_zeile, start_spalte, richtung, anzahl):
    if richtung == 'horizontal':
        for i in range(anzahl):
            if feld[start_zeile][start_spalte + i] != '.':
                return False
    else:
        for i in range(anzahl):
            if feld[start_zeile + i][start_spalte] != '.':
                return False
    return True
platziere_schiff(4)  
platziere_schiff(3)  
treffer = 0
versuche = 0
max_versuche = 10
while treffer < 7 and versuche < max_versuche:  
    print("Aktuelles Raster:")
    for zeile in Raster:
        print(' '.join(zeile))

    print(f"Verbleibende Versuche: {max_versuche - versuche}") 

    eingabe = input("Gib die Zeile und Spalte ein (z.B. 2 3): ")
    try:
        zeile, spalte = map(int, eingabe.split())
        if zeile < 0 or zeile > 9 or spalte < 0 or spalte > 9:
            print("Bitte gib gültige Koordinaten zwischen 0 und 9 ein.")
            continue
    except ValueError:
        print("Ungültige Eingabe. Bitte gib zwei Zahlen ein.")
        continue
    if Schiffe[zeile][spalte] == 'X':
        print("Treffer!")
        Raster[zeile][spalte] = 'O'
        treffer += 1
    elif Raster[zeile][spalte] == '.':
        print("Leider verfehlt.")
        Raster[zeile][spalte] = '-'  
    else:
        print("Diese Koordinate wurde bereits angegriffen. Versuch es erneut.")
    versuche += 1
if treffer == 7:
    print("Du hast alle Schiffe getroffen!")
else:
    print("Du hast alle Versuche aufgebraucht. Hier sind die Positionen der Schiffe:")
    for zeile in Schiffe:
        print(' '.join(zeile))