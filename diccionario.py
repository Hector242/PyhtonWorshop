def main():
#Los diccionarios son otras estructuras de datos que empiezan {} y 
#funcionan con un estilo key:value
    diccionary = {
        'Argentina': 44938712,
        'Brasil': 210147125,
        'Colombia': 50372424,
    }
    # print(diccionary['key1'])
    # print(diccionary['key2'])
    # print(diccionary['key3'])
    #Para recorrer el diccionario y ver el resultado de key y valor
    #usar un ciclo for y usar el metodo items
    for country, population in diccionary.items():
        print(country + ' tiene la poblacion de ' + str(population))

if __name__ == '__main__':
    main()