#Prueba numero 3: 
import os,time,msvcrt
from Funciones import *
while True:
    os.system('cls')
    print('\tMenú de Gaxplosive')
    print('1. Registrar pedido.')
    print('2. Listar pedido.')
    print('3. Buscar pedido por rut.')
    print('4. Imprimir hoja de ruta(archivo.csv).')
    print('5. Salir.')
    opc=validar_opc()
    os.system('cls')
    if opc==1:
        registrar_pedido()
    elif opc ==2:
        listar_pedido()
    elif opc ==3:
        buscar_rut()
    elif opc ==4:
        imprimir_csv()
    else:
        salir()