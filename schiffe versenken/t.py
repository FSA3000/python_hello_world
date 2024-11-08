import random

# Erstelle ein 7x7 Raster
Raster = [['.' for _ in range(7)] for _ in range(7)]

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
            start_zeile = random.randint(0, 6)
            start_spalte = random.randint(0, 7 - anzahl)
        else:
            start_zeile = random.randint(0, 7 - anzahl)
            start_spalte = random.randint(0, 6)
        
        # Überprüfen, ob das Schiff platziert werden kann
        if alle_felder_frei(Raster, start_zeile, start_spalte, richtung, anzahl):
            markiere_punkte(Raster, start_zeile, start_spalte, richtung, anzahl)
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

# Platziere zwei Schiffe
platziere_schiff(4)  # Erstes Schiff mit 4 Feldern
platziere_schiff(3)  # Zweites Schiff mit 3 Feldern

# Spiel Schleife
treffer = 0
versuche = 0

while treffer < 7:  # Insgesamt 7 Felder zu treffen (4 + 3)
    print("Aktuelles Raster:")
    for zeile in Raster:
        print(' '.join(zeile))
    
    eingabe = input("Gib die Zeile und Spalte ein (z.B. 2 3): ")
    
    # Eingabe validieren
    try:
        zeile, spalte = map(int, eingabe.split())
        if zeile < 0 or zeile > 6 or spalte < 0 or spalte > 6:
            print("Bitte gib gültige Koordinaten zwischen 0 und 6 ein.")
            continue
    except ValueError:
        print("Ungültige Eingabe. Bitte gib zwei Zahlen ein.")
        continue
    
    if Raster[zeile][spalte] == 'X':
        print("Treffer!")
        Raster[zeile][spalte] = 'O'  # Markiere Treffer
        treffer += 1
    elif Raster[zeile][spalte] == '.':
        print("Leider verfehlt.")
        Raster[zeile][spalte] = '-'  # Markiere Fehlschuss
    else:
        print("Diese Koordinate wurde bereits angegriffen. Versuch es erneut.")
    
    versuche += 1

print(f"Herzlichen Glückwunsch! Du hast alle Schiffe getroffen in {versuche} Versuchen.")
