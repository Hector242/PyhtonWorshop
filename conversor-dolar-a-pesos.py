dolars = input ("Cuantos dolares tienes?: ")
dolars = float(dolars)
pesos_value = 200
pesos = dolars*pesos_value
pesos = round(pesos, 2)
pesos = str(pesos)
print ("Tienes $" + pesos + " pesos")