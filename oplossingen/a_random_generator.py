import random

voorvoegsels = ('Super', 'Mega', 'Ultra', 'Geweldige', 'Toffe', 'Snelle', 'Slimme', 'Magische')
achtervoegsels = ('Coder', 'Ninja', 'Expert', 'Gebruiker', 'Gamer', 'Ster')

def genereer_gebruikersnaam():
    voorvoegsel = random.choice(voorvoegsels)
    achtervoegsel = random.choice(achtervoegsels)

    gebruikersnaam = voorvoegsel + achtervoegsel
    return gebruikersnaam

print("10 willekeurige gebruikersnamen:")

for _ in range(10):
    print(genereer_gebruikersnaam())