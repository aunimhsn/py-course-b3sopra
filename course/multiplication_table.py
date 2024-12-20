table = int(input('Veuillez saisir la table à afficher : '))

result = []

for i in range(1, 11):
    if (i * table) % 3 == 0:
        result.append(f'{i * table}*')
    else:
        result.append(i * table)

print(result)