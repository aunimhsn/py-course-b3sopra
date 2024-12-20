actors = ['Isabelle Adjani', 'Cilian Murphy']

actors_initials = []

for actor in actors:
    actor_initials = f'{actor.split(' ')[0][0]}. {actor.split(' ')[1][0]}.'
    actors_initials.append(actor_initials)


print(actors_initials)
