phrase = str(input('Enter a phrase: '))
vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
print('The phrase has the next vowels: ')

for x in phrase:
    if x in vowels:
        print(x)
