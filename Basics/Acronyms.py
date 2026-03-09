#Capture string input with space as sep 
Phrase = map(str, input("Enter the Phrase Please ").split())

Acronym = []
#Iterating and appending the First Alphabet of every word in the Phrase
for Alph in Phrase:
    Acronym.append(Alph[0].upper())
#joining Alphabets together with dot.
print('.'.join(Acronym))