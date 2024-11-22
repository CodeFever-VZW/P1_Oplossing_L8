import random

beschrijvingen = ('Super', 'Mega', 'Ultra', 'Geweldige', 'Toffe', 'Snelle', 'Slimme', 'Magische')
rollen = ('Coder', 'Ninja', 'Expert', 'Gebruiker', 'Gamer', 'Ster')

def genereer_gebruikersnaam():
    beschrijving = random.choice(beschrijvingen)
    rol = random.choice(rollen)

    gebruikersnaam = beschrijving + rol
    return gebruikersnaam

print("10 willekeurige gebruikersnamen:")

for _ in range(10):
    print(genereer_gebruikersnaam())
