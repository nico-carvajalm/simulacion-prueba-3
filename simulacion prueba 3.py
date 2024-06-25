def mostrar_menu():
    print("1. Registrar pedido")
    print("2. Listar todos los pedidos")
    print("3. Imprimir hoja de ruta")
    print("4. Salir del programa")

def registrar_pedido():
    
    nom=input("Ingrese nombre y Apellido: ")
    com=input("Ingrese comuna: ")
    c5=int(input("Ingrese cantidad de cilindros de 5kg: "))
    c15=int(input("Ingrese cantidad de cilindros de 15kg: "))
    c45=int(input("Ingrese cantidad de cilindros de 45kg: "))
    L1=[nom,com,c5,c15,c45]
    L.append(L1)


    

##MAIN

L=[]
while True:
    mostrar_menu()

    op=input("Elegir opción: ")
    if op=="1":
        registrar_pedido()
        print(L)
    elif op=="4":
        print("Saliendo del programa")
        break

   

