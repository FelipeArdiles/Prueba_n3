import os, msvcrt, csv,time

pedidos=[]
total_5kg=0
total_15kg=0

def registrar_pedido():
    print("\tRegistrar Pedido")
    while True:
            rut=input("Ingrese su RUT (SIN PUNTOS Y SIN GUIÓN): ")
            if len(rut)<=10 and len(rut)>7:
                break
            else:
               print("ERROR! la longitud del rut no puede ser menor a 7 dígitos o mayor a 10")

    while True:
            nombre=input("Ingrese Nombre: ")
            if len(nombre)<3:
                print("ERROR! La longitud del nombre no puede ser menor a 3")
            else:
                break

    direccion = input("ingrese su dirección: ")
    comuna = input("Ingrese su comuna: ")

    while True: 
        os.system("cls")
        print("\tCilindros")
        print("1) 5Kg   12.500$")
        print("2) 15Kg  25.000$")
        print("3) Salir ")
        while True:
            try:
                opc_cilindros=int(input("Elija la opción que desea comprar: "))
                if opc_cilindros in (1,2,3):
                    break
                else:
                    print("ERROR! DEBE INGRESAR UNA OPCÍON VÁLIDA")
            except:
                print("ERROR, DEBE INGRESAR UN NÚMERO ENTERO")

            if opc_cilindros==1:
                print("Cilindros de 5Kg")
                while True:
                    try:
                        cil_5kg=int(input("Ingrese la cantidad que desea de este producto: "))
                        if cil_5kg>=0 and cil_5kg<=10:
                            total_5kg=total_5kg+cil_5kg
                            print("Se ha agregado con éxito!")
                            print("Su subtotal es de:",total_5kg*12500,"$")
                            time.sleep(3)
                            break
                        else:
                            ("ERROR! No puede ingresar valores negativos o mayores a 10")

                    except:
                        print("ERROR DEBE INGRESAR UN NÚMERO ENTERO")

            elif opc_cilindros==2:
                print("Cilindros de 15Kg")
                while True:
                    try:
                        cil_15kg=int(input("Ingrese la cantidad que desea de este producto: "))
                        if cil_15kg>=0 and cil_15kg<=10:
                            total_15kg=total_15kg+cil_15kg
                            print("Se ha agregado con éxito!")
                            print("Su subtotal es de:",total_15kg*25500,"$")
                            time.sleep(3)
                            break
                        else:
                            ("ERROR! No puede ingresar valores negativos o mayores a 10")

                    except:
                        print("ERROR DEBE INGRESAR UN NÚMERO ENTERO")

            else:
                break
        precio_total=(total_5kg*12500)+(total_15kg*25500)
        pedido=[rut,nombre,direccion,comuna,total_5kg,total_15kg,precio_total]
        pedidos.append(pedido)
        print("El pedido se añadio con éxito!")
        time.sleep(2)
        break

def rut():
    while True:
            rut=input("Ingrese su RUT (SIN PUNTOS Y SIN GUIÓN): ")
            if len(rut)<=10 and len(rut)>7:
                break
            else:
               print("ERROR! la longitud del rut no puede ser menor a 7 dígitos o mayor a 10")

def documento():
    nom_documento=input("Ingrese nombre del documento: ")
    with open(nom_documento+".csv","w",newline="") as archivo:
        escritor=csv.writer(nom_documento+".csv")
        escritor.writerows(archivo)



