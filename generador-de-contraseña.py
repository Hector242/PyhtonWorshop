from random import choice
from string import ascii_lowercase
from string import ascii_uppercase

def password_generator():
    #llenar listas de mayusculas
    uppercase = []
    for letter in ascii_uppercase:
        uppercase.append(letter)
    #cambiamos el tipo de dato de una lista de int a str con .join
    uppercase_list = "".join(uppercase)
    #print(uppercase_list)
    
    #llenar listas de minusculas
    lowercase = []
    for letter in ascii_lowercase:
        lowercase.append(letter)
    #cambiamos el tipo de dato de una lista de int a str con .join
    lowercase_list = "".join(lowercase)
    #print(lowercase_list)

    
    #llenar listas de numeros
    numbers = []
    for i in range(10):
        numbers.append(i)
    #cambiamos el tipo de dato de una lista de int a str con .join
    numbers_list= "".join(map(str, numbers))
    #print(numbers_list)
    
    #llenar listas de simbolos
    sign = ['!', '$', '#']
    sign_list = "".join(sign)
    #print(sign_list)

    #Crear contraseña random
    chars = uppercase + lowercase + sign + numbers
    password = []
    for i in range(8):
        char_random = choice(chars)
        password.append(char_random)
    password_generated = "".join(map(str,password))
    return password_generated



def main():
    password = password_generator()
    print('Su password es ' + password)

if __name__ == '__main__':
    main()