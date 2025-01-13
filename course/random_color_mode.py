from random import randint
from sty import fg

def generate_rgb() -> tuple[int]:
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)

    return red, green, blue

print(fg(*generate_rgb()), 'Hello', fg.rs)