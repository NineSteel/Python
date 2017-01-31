import pprint
message = "Mr. Swanson is the computer science teacher at ACS."
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] +1

pprint.pprint(count)
