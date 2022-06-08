def is_primo(number):
    count = 0
    for i in range(1, number + 1):
        primo = number % i
        if primo == 0:
            count = count + 1
        
    if count > 2:
        return False
    else:
        return True



def main():
    number = int(input("Escriba un numero: "))
    # for i in range(2,number + 1):
    #     is_primo = number % i
    #     division_by_one = number % 1 
    # if (is_primo == 0 and division_by_one == 0 and number % 2 != 0) or number == 2:
    #     print ("Es un numero primo :) ")
    # else:
    #     print("No es un numero primo :(")
    primo_verdarero = is_primo(number)
    if primo_verdarero == True:
        print("Es primo")
    else:
        print("no es primo")

if __name__ == "__main__":
    main()