import random
import string


def passaword_generation(len_pass = 8):
    ascii_options = string.ascii_letters
    number_options = string.digits
    punt_options = string.punctuation
    options = ascii_options + number_options + punt_options
    
    
    passaword_user = ""
    
    
    for digit in range (0, len_pass):
       digit = random.choice(options)
       passaword_user = passaword_user + digit
       
    return passaword_user
choice_user = input("Quantos digitos na senha? ")

if choice_user.isdigit():
    choice_user = int(choice_user)
else:
    print("Entrada invalida")
    quit()
    
response = passaword_generation(len_pass = choice_user)
print(f"Sua senha foi gerada: \n{response}")