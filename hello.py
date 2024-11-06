import random
def hangman():
    wörter = ["python", "programmieren", "hangman", "spiel", "computer","schulen","schwimmen","schlafen","praktikum","ferien","urlaub","mathematik","informatik","haus",  "winter","sommer", "herbst","frühling","jahr","monat","tag","stunde","minute","flender","Artzt","Kunst","Musik","Deutsch","Englisch",]
    wörter = random.choice(wörter) 
    guessed_letters = []
    attempts = 6
    wörter_completion = '_' * len(wörter) 
    print("Willkommen zu Hangman!")
    print(display_hangman(attempts))
    print(wörter_completion)
    print("\n")
    while attempts > 0 and '_' in wörter_completion:
        guess = input("Rate einen Buchstaben: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Bitte gib einen einzelnen Buchstaben ein.")
            continue
        if guess in guessed_letters:
            print("Du hast diesen Buchstaben bereits geraten.")
            continue
        guessed_letters.append(guess)
        if guess in wörter:
            print(f"Gut gemacht! Der Buchstabe '{guess}' ist im Wort.")
            wörter_completion = ''.join([letter if letter in guessed_letters else '_' for letter in wörter])
        else:
            attempts -= 1
            print(f"Leider, der Buchstabe '{guess}' ist nicht im Wort. Du hast noch {attempts} Versuche.")
        print(display_hangman(attempts))
        print(wörter_completion)
        print("\n")
    if '_' not in wörter_completion:
        print("Du hast das Wort erraten")
    else:
        print("Du hast es leider nicht geschafft das Wort war:",wörter)
def display_hangman(attempts):
    stages = [
        """
      -----
      |   |
      |   O
      |  /|\\
      |  / \\
      |
   """,
   """
      -----
      |   |
      |   O
      |  /|\\
      |  /
      |
   """,
   """
      -----
      |   |
      |   O
      |  /|
      |
      |
   """,
   """
      -----
      |   |
      |   O
      |
      |
      |
   """,
   """
      -----
      |   |
      |
      |
      |
      |
   """,
   """
      -----
      |
      |
      |
      |
      |
   """,
   """
      -----
      |
      |
      |
      |
      |
        """
    ]
    return stages[attempts]
if __name__ == "__main__":
    hangman()