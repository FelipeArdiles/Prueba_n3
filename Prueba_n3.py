import os, msvcrt, time
from funciones import *

print("""¡Bienvenido a Gaxploxive!
      1) Registrar pedido.
      2) Listar todos los pedidos.
      3) Buscar pedido por RUT.
      4) Imprimir hoja de ruta.
      5) Salir del programa""")

opc=int(input("Ingrese una opción del menú: "))
if opc==1:
    registrar_pedido()
elif opc==2:
    pass
elif opc==3:
    pass
elif opc==4:
    pass
else:
    pass