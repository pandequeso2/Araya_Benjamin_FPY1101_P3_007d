#Funciones principales: 
import os,msvcrt,time
ventas=[]
pago=0
def registrar_pedido():
    print('REGISTRAR PEDIDO.')
    rut=validar_rut()
    nombre=validar_nom()
    direccion=validar_direccion()
    comuna=validar_comuna()
    while True:
        os.system('cls')
        print('1. Cilindro 5 kilos')
        print('2. Cilindro 15 kilos ')
        print('3. Salir y ver total.')
        opc=validar_opc_2()
        os.system('cls')
        if opc==1:
            print('El valor de 5 kilos es de $12.500.')
            cant=validar_can()
            if cant==0:
                compra_5=0
            else:
                compra_5=cant*12500
                time.sleep(2)
        elif opc==2:
            print('Valor de cilindro de 15 kilos es $25.500')
            canti=validar_cant()
            if canti ==0:
                compra_15=0
            else:
                compra_15=canti*12500
                time.sleep(2)
        else:
            if compra_5==0 or compra_15==0:
                print('Debes comprar algo... ')
                time.sleep(1)
            else:    
                pago=compra_5+compra_15
                print(f'El total de la compra es: {pago}')
                print('Ingrese una tecla para continuar...')
                msvcrt.getch()
                break
    venta=[rut,nombre,direccion,comuna,cant,canti,pago]
    ventas.append(venta)
    time.sleep(1)
    print('Pedido realizado...')    
def listar_pedido():
    if not ventas:
        print('La lista de ventas esta vacia, ve a la opción 1 primero.')
        time.sleep(2)
    else:
        for v in ventas:
            print(f'Rut: {v[0]}')
            print(f'Nombre: {v[1]}')
            print(f'Dirección: {v[2]}')
            print(f'Comuna: {v[3]}')
            print(f'Cantidad 5 kilos: {v[4]}')
            print(f'Cantidad 15 kilos: {v[5]}')
            print(f'Pago total: ${v[6]}')
            print('Ingrese una tecla para continuar....')
            msvcrt.getch()
def buscar_rut():
    if not ventas:
        print('La lista de ventas esta vacia, ve a la opcion 1 primero.')
    else:
        rut_buscar=validar_rut_buscar()
        for v in ventas:
            if rut_buscar==v[0]:
                print(f'Rut: {v[0]}')
                print(f'Nombre: {v[1]}')
                print(f'Dirección: {v[2]}')
                print(f'Comuna: {v[3]}')
                print(f'Cantidad 5 kilos: {v[4]}')
                print(f'Cantidad 15 kilos: {v[5]}')
                print(f'Pago total: ${v[6]}')
                print('Ingrese una tecla para continuar....')
                msvcrt.getch()
            else:
                print('ERROR, EL RUT NO EXISTE...')
def imprimir_csv():
    pass
def salir():
    print('ADIOOOS...')
    exit()


#Funciones secundarias:
def validar_opc():
    while True:
        try:
            opc=int(input('Ingrese un numero: '))
            if opc in(1,2,3,4,5):
                return opc
            else:
                print('ERROR, no esta dentro de las opciónes...')
        except:
            print('ERROR, DEBE SER UN NÚMERO ENTERO...')        
def validar_rut():
    while True:
        try:
            rut=int(input('Ingrese su rut(sin puntos ni digito verificador): '))
            if len(str(rut))==9 and rut>0:
                return rut
            else:
                print('ERROR, el rut debe tener 9 digitos y debe ser mayor a 0...')
        except:
            print('ERROR, debe ser un número entero...')    
def validar_nom():
    while True:
        nom=input('Ingrese su nombre: ')
        if len(nom.strip())>=3 and nom.isalpha():
            return nom
        else:
            print('ERROR, el nombre debe tener almenos 3 caracteres...')
def validar_direccion():
    while True:
        di=input('Ingrese su dirección: ')
        if len(di.strip()) >=2:
            return di
        else:
            print('ERROR, DEBE TENER ALMENOS 2 CARACTERES')
def validar_comuna():
    while True:
        com=input('Ingrese su comuna: ')
        if len(com.strip()) >=2:
            return com
        else:
            print('ERROR, DEBE TENER ALMENOS 2 CARACTERES')                      
def validar_opc_2():
    while True:
        try:
            opc=int(input('Ingrese un numero: '))
            if opc in(1,2,3):
                return opc
            else:
                print('ERROR, no esta dentro de las opciónes...')
        except:
            print('ERROR, DEBE SER UN NÚMERO ENTERO...') 
def validar_can():
    while True:
        try:
            can=int(input('Ingrese la cantidad de cilindros: '))
            if can >=0:
                return can
            else:
                print('ERROR, ingrese un numero mayor o igual que 0...')
        except:
            print('ERROR, DEBE SER UN NÚMERO ENTERO.')    
def validar_cant():
    while True:
        try:
            can=int(input('Ingrese la cantidad de cilindros: '))
            if can >=0:
                return can
            else:
                print('ERROR, ingrese un numero mayor o igual que 0...')
        except:
            print('ERROR, DEBE SER UN NÚMERO ENTERO.')
def validar_rut_buscar():
    while True:
        try:
            rut=int(input('Ingrese su rut a buscar(sin puntos ni digito verificador): '))
            if len(str(rut))==9 and rut>0:
                return rut
            else:
                print('ERROR, el rut debe tener 9 digitos y debe ser mayor a 0...')
        except:
            print('ERROR, debe ser un número entero...') 

