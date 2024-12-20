from random import randint


difficulty = input('1. Facile - 2. Moyen - 3. Difficile : ')
while difficulty not in ['1', '2', '3']:
    print('Veuillez entrer 1, 2 ou 3')
    difficulty = input('1. Facile - 2. Moyen - 3. Difficile : ')

maximum = 100
if difficulty == '1':
    maximum = 10
elif difficulty == '2':
    maximum = 100
elif difficulty == '3':
    maximum = 1000

secret = randint(0, maximum)
user_input = int(input(f'Veuillez saisir un nombre entre 0 et {maximum} : '))
attempts = 1

while secret != user_input:
    if secret > user_input:
        print('C\'est plus !')
    else:
        print('C\'est moins')
    
    user_input = int(input(f'Veuillez saisir un nombre entre 0 et {maximum} : '))
    # attempts = attempts + 1
    attempts += 1

print(f'Bravo, vous avez trouvé le nombre secret {secret} en {attempts} essai.s')