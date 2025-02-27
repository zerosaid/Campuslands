import os
import collections.abc 
inventario_autos = {
    "Toyota Corolla":{"Disponibles":3,"precio_por_dia":160000},
    "Toyota Civic": {"Disponibles":2,"precio_por_dia":160000},
    "Chevrolet Spark":{"Disponibles":4,"precio_por_dia":160000}, 
    "Hyundai Accent":{"Disponibles":4,"precio_por_dia":160000}, 
    "Nissan Svrsa":{"Disponibles":5,"precio_por_dia":160000},
    "Toyota Yaris":{"Disponibles":6,"precio_por_dia":160000},
    "Ford Focus":{"Disponibles":3,"precio_por_dia":160000},
    "Nissan Sentra":{"Disponibles":7,"precio_por_dia":160000}, 
    "Dodge Avenger":{"Disponibles":4,"precio_por_dia":160000},
    "Ford Fusion":{"Disponibles":5,"precio_por_dia":160000},
    "Nissan Altima":{"Disponibles":2,"precio_por_dia":160000}
}

def mostrar_auto():
    print()
    for llave, valor in inventario_autos.items():
        print(valor, " - ", llave)
        

def alquilar_auto():
    os.system("cls" if os.name =="nt" else"clear")
    print("****Alquilar Auto***")
    while True:            
        print("Los autos disponibles son: ")
        for i in inventario_autos:
            print("- ",i)
        produc = str(input("ingrese el modelo de auto que desea alquilar o si ya escogio dele 0 para volver: "))
        auto = produc.title()
        if auto in inventario_autos:
            cantidad = int(input("Ingrese la cantidad de dias que los desee alquilar, luego de 0 para volver al menu: "))
            lista[auto] = cantidad
        elif auto == "0":
            break
        else:
            print("El Auto que desea ya no esta o no se encuentra en nuestro sistema") 

def pagar_alquiler ():
    os.system("cls" if os.name =="nt" else"clear")
    print("El auto alquilado es: ")
    total = 0
    for llave, valor in lista.items():
        print(llave, " - cantidad: ", valor, " - precio: ", 160000)
        total  += valor * 160000
    print("El total a pagar es: ", total)

opciones = {"1": mostrar_auto, "2": alquilar_auto, "3": pagar_alquiler}
lista = {}

while True:
    os.system("cls" if os.name =="nt" else"clear")
    print("*****Bienvenido a el alquiles de Mario*****")
    print("Ingrese\n1. Para ver los autos disponibles\n2. Para alquilar un auto\n3. Para ver cuanto debe pagar\n4. Para salir")
    opc = input("Ingrese la opción requerida: \n")
    if opc in opciones:
        os.system("cls" if os.name =="nt" else"clear")
        opciones[opc]()
        input("\n Presione enter para continuar")
    elif opc == "3":
        print("Saliendo...")
        break
    else:
        print("Lea bien...")