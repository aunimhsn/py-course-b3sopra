

fruit = 'mandarin'

match fruit:
    case 'apple':
        print('Apple price : 0.60')
    case 'banana':
        print('Banana price : 0.70')
    case 'orange' | 'mandarin':
        print('Orange and Madarin price : 0.90')
    case _:
        print('Ce fruit n\'existe pas')

