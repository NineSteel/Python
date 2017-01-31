import pprint

count = {}
c = 0

while c<5:
    print('Enter a message')
    message = input()

    for character in message:
        count.setdefault(character, 0)
        count[character] = count[character] +1
        pprint.pprint(count)
        count = {}

    print('Do you want to run the program again?')

    answer = input()
    if answer == 'yes':
        c-=1
    elif answer == 'no':
        c=5
        print('Bye bye!')
    else:
        c=5
        print('You have force quit the application')
