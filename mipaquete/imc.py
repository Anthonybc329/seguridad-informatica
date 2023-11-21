# Funcion que determina el IMC, y que diga el nivel del peso
#Peso, altura y nombre

def funcion():
    nombre = input("Cual es tu nombre? ")
    peso = float(input("Cual es tu peso? "))
    altura = float(input("Cual es tu altura? "))
    
    imc = peso / altura*altura
    
    if imc > 30:
        print("Tienes obesidad")
    elif imc > 25:
        print("Tienes sobre peso")
    elif  imc > 18:
        print ("Tienes un peso normal")
    else:
        print("Te falta alimentarte")