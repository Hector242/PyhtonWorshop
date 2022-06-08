#definimos la funcion main del proyecto
from operator import truediv

def palindromo(word):
    word = word.replace(' ','')
    word= word.lower()
    word_on_reverse = word[::-1]
    print("Asi es la palabra al reves: " + word_on_reverse)
    if word == word_on_reverse:
        return True
    else:
        return False


def main():
    word = input("Escriba una palabra: ")
    is_palindromo = palindromo(word)
    if is_palindromo == True:
        print("Es palindromo")
    else:
        print("No es palindromo")

#Definimos el entry point como buena practica, siempre tiene que estar
if __name__ == '__main__':
    main()