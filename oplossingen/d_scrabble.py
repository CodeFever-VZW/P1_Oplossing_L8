punten = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2,
          'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
          'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1,
          'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}


def scrabble_punten(woord):
    score = 0
    for letter in woord:
        score += punten[letter]
    return score


while True:
    woord = input("Voer een woord in (of druk op Enter om te stoppen): ")

    if len(woord) == 0:
        break

    score = scrabble_punten(woord.lower())
    print(f"Scrabble-punten voor '{woord}': {score}")