

# 1. Acquisition des notes
marks = []

while True:
    mark = input('Veuillez saisir une note (si nombre négatif = quitte le programme) : ')

    try:
        mark_float = float(mark)
    except ValueError:
        print('Ceci n\'est pas un nombre...')
    else:
        if mark_float < 0:
            break
        else:
            marks.append(mark_float)

print(f'Il y a {len(marks)} de note.s')

# 2. Calcul de la moyenne des notes (marks)
try:
    marks_average = sum(marks) / len(marks)
except ZeroDivisionError:
    print('Il n\'y a pas de note...')
else:
    print(f'La moyenne des notes est {marks_average}')    