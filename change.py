#31/3/2025
#TP2 - Rozas Miguel Agustin - Introduccion a la programacion 1
#Ejercicio 3
def change():
    expense = 23.75
    money = 100
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print("")
    print("Vuelto")
    print("")
    print("Pesos:")
    print(int(money - expense))
    print("Centavos:")
    print(int((money - expense) * 100 % 100))
