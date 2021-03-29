import random

print('Welcome to Password Generator\n')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*()_.,?0123456789'

number = input('Amounts of passowords to generate: ')
number = int(number)

length = input('Input password length: ')
length = int(length)

print('\nHere are the passwords: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)