def converter(pesos_value, type_of_pesos):
    pesos = input ("Cuantos pesos " + type_of_pesos + " tienes?: ")
    pesos = float(pesos)
    dolars = pesos / pesos_value
    dolars = round(dolars, 2)
    dolars = str(dolars)
    print ("Tienes $" + dolars + " dolares") 
menu ="""
 Bienvenidos al conversor de monedas

Para comenzar tome una opcion:
1.- Convertir de pesos Argentinos a dolar
2.- Convertir de pesos Colombianos a dolar
3.- Convertir de pesos Mexicanos a dolar

:  """
option = int(input(menu))

if option == 1:
    converter(220, "Argentinos")
elif option == 2:
   converter(3334, "Colombianos")
elif option == 3:
    converter(20, "Mexicanos")
else:
    print("La opcion tomada es incorrecta")