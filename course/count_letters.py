from string import ascii_lowercase

poem = "Two roads diverged in a yellow wood, \
And sorry I could not travel both \
And be one traveler, long I stood \
And looked down one as far as I could \
To where it bent in the undergrowth."
poem = poem.lower()

result = {}
for letter in ascii_lowercase:
    result[letter] = poem.count(letter)

print(result)

