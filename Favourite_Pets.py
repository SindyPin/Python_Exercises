favourite_pet = str(input('Enter your favourite pet: '))
list_pet = ['fish', 'cat', 'dog']

if favourite_pet in list_pet:
    print('This is the available list of pets and your favourite pet is in the list')
    for favourite_pet in list_pet:
        print(favourite_pet)
else:
    print('This is the available list of pets and your favourite pet is NOT in the list')
    for favourite_pet in list_pet:
        print(favourite_pet)
