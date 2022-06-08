from random import randint


def random_number():
    value = randint(0,10)
    return value


def is_it_true(number_created, number_from_user):
    if number_from_user == number_created:
        print ("Geni@! Has adivinado mi numero :)")
        return True
    elif number_from_user > number_created:
        print("Acaso lees mentes? pues la mia no, tu numero es mayor")
        return False
    else:
        print("Acaso lees mentes? pues la mia no, tu numero es menor")
        return False   
    
def entrada():
    screen_menu ="""

 Bienvenidos a adivina un numero. 

 El proposito de este juego es que adivines el numero
 que pienso... Si eres capaz de susperar este desafio,
 Demostraras sin duda tu poder mental!!!

"""
    print(screen_menu)

def main():
    entrada()
    number_created = random_number()
    verification = False
    while verification != True:
        number_from_user = int(input("Ingrese un numero del 1 al 10: "))
        verification = is_it_true(number_created, number_from_user)
    

if __name__ == '__main__':
    main()