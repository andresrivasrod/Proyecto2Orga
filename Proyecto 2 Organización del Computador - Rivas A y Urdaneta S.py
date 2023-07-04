import os
from pathlib import Path

# Funcion que escribe "EN MANTENIMIENTO" o "EN EXHIBICION" en la base de datos
def cambiarEstado(line, index, mode):
    if mode == 0:
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        p = Path(__file__).with_name('db.txt')
        with open(p, 'r') as f:
            g = f.readlines()
            line = line.replace('EN EXHIBICION', 'EN MANTENIMIENTO')
            g[index] = line
        with open(p, 'w') as h:
            h.writelines(g)
    elif mode == 1:
        __location__ = os.path.realpath( os.path.join(os.getcwd(), os.path.dirname(__file__)))
        p = Path(__file__).with_name('db.txt')
        with open(p, 'r') as f:
            g = f.readlines()
            line = line.replace('EN MANTENIMIENTO', 'EN EXHIBICION')
            g[index] = line
        with open(p, 'w') as h:
            h.writelines(g)
  
# Funcion que cambia de exhibicion a mantenimiento
def puestaMant():
    selector = input("\nSeleccione como hacer su búsqueda:\n1. Buscar pintura por cota\n2. Buscar pintura por nombre\n>>>> ")
    if selector == '1':
       index = buscarCota()
    elif selector == '2':
       index = buscarNombre()
    if index == '-1':
        print("No se ha encontrado la cota o nombre buscado.")
        input("Presione enter para volver al menú principal...\n")
        menu()
    else:
        index = int(index.replace('\n', ""))
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        p = Path(__file__).with_name('db.txt')
        with open(p) as f:
            g = f.readlines()
            x = g[index].split('/')   
            if x[4] == 'EN EXHIBICION\n':
                    cambiarEstado(g[index], index, 0)
                    print("Cambio de estatus exitoso")
                    input("Presione enter para volver al menú principal...\n")
                    menu()
            else:
                print("La pintura ya se encuentra en mantenimiento")
                input("Presione enter para volver al menú principal...\n")
                menu()
           
# Funcion que cambia de mantenimiento a exhibicion
def puestaExh():
    selector = input("\nSeleccione como hacer su búsqueda:\n1. Buscar pintura por cota\n2. Buscar pintura por nombre\n>>>> ")
    if selector == '1':
       index = buscarCota()
    elif selector == '2':
       index = buscarNombre()
    if index == '-1':
        print("No se ha encontrado la cota o nombre buscado.")
        input("Presione enter para volver al menú principal...\n")
        menu()
    else:
        index = int(index.replace('\n', ""))
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        p = Path(__file__).with_name('db.txt')
        with open(p) as f:
            g = f.readlines()
            x = g[index].split('/')   
            if x[4] == 'EN MANTENIMIENTO\n':
                    cambiarEstado(g[index], index, 1)
                    print("Cambio de estatus exitoso")
                    input("Presione enter para volver al menú principal...\n")
                    menu()
            else:
                print("La pintura ya se encuentra en exhibiciÓn")
                input("Presione enter para volver al menú principal...\n")
                menu()

# Funcion encargada imprimir los resultados de la búsqueda 
def buscarBaseDeDatos(index):
    if index == '-1':
        print("La obra de arte ingresada no se encuentra en la galería.")
        input("Presione enter para volver al menú principal...\n")
        menu()
    else:
        index = int(index.replace('\n', ""))
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        p = Path(__file__).with_name('db.txt')
        with open(p) as f:
            g = f.readlines()
            x = g[index].split('/')
            f.close()
        if x[0][0:2] == "##":          
            print("\nEsta obra está marcada para ser eliminada.")
        print('\tCota: ' + x[0] + '\n\tNombre: ' + x[1] + '\n\tPrecio: $' + x[2] + '\n\tAño: ' + x[3] + '\n\tEstatus: ' + x[4])
    input("Presione enter para volver al menú principal...\n")
    menu()              

# Funcion encargada de buscar la cota mediante una búsqueda binaria
def buscarCota():
    objetivo = input("\nIntroduzca la cota de la obra que desea buscar: ").upper()

    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    p = Path(__file__).with_name('cotaIndice.txt')
    with open(p) as f:
        g = f.readlines()
        l = []
        for x in g:
            l.append(x.split('/'))
        # búsqueda binaria
        pasos = 0
        izq = 0
        der = len(l) - 1
        while izq <= der:
            pasos += 1
            medio = (izq + der) // 2

            if l[medio][0] == objetivo:
                return l[medio][1]
            elif l[medio][0] > objetivo:
                der = medio - 1
            else:
                izq = medio + 1
        return str(-1)

# Funcion encargada de buscar el nombre mediante una búsqueda binaria
def buscarNombre():
    objetivo = input("\nIntroduzca el nombre de la obra que desea buscar: ")

    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    p = Path(__file__).with_name('nombreIndice.txt')
    with open(p) as f:
        g = f.readlines()
        l = []
        for x in g:
            l.append(x.split('/'))
        # búsqueda binaria
        pasos = 0
        izq = 0
        der = len(l) - 1
        while izq <= der:
            pasos += 1
            medio = (izq + der) // 2

            if l[medio][0] == objetivo:
                return l[medio][1]
            elif l[medio][0] > objetivo:
                der = medio - 1
            else:
                izq = medio + 1
        return str(-1)        

# Funcion de registrar en archivo nombreIndice y cotaIndice
def regIndexes(name, cota, indice):
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    p = Path(__file__).with_name('nombreIndice.txt')
    with p.open('a') as k:
        k.write(name + '/' + str(indice) + '\n')
        k.close()
    organizarNombre()

    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    p = Path(__file__).with_name('cotaIndice.txt')
    with p.open('a') as k:
        k.write(cota + '/' + str(indice) + '\n')
        k.close()
    organizarCota()

# Funcion reorganizar archivo cotaIndice
def organizarCota():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    p = Path(__file__).with_name('cotaIndice.txt')
    with p.open('r+') as f:
        g = sorted(f)
        f.seek(0)
        for h in g:
            f.write(h)
    f.close()

# Funcion reorganizar archivo nombreIndice
def organizarNombre():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    p = Path(__file__).with_name('nombreIndice.txt')
    with p.open('r+') as f:
        g = sorted(f)
        f.seek(0)
        for h in g:
            f.write(h)
        f.close()

# Archivo que devuelve el indice donde se agregará la pintura
def indexDB():
    y = 0
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    p = Path(__file__).with_name('db.txt')
    with p.open('r') as f:
        for x in f:
            y += 1
        f.close()
    return str(y)

# Funcion que almacena los datos de la pintura en la base de datos
def regPintura(cota, nombre, precio, ano, status):
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    p = Path(__file__).with_name('db.txt')
    with p.open('a') as f:
        f.write(cota + '/' + nombre + '/' + precio + '/' + ano + '/' + status + '\n')
        f.close()    
    
# Funcion de validacion de nombre
def validacion_nombre():
    nombre = input("\nIntroduzca el nombre de su pintura (no exceda de 10 caracteres): \n>>>> ")
    if len(nombre) <= 10:
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        p = Path(__file__).with_name('nombreIndice.txt')
        with open(p) as f:
            info = f.readlines()
            f.close()

        lista_nombres = []

        for linea in info:
            #lineas.append(linea.strip().split('/'))
            lineas = linea.strip().split('/')
            lista_nombres.append(lineas[0])

        if nombre in lista_nombres:
            print(f"Ya existe una obra guardada con el nombre '{nombre}'.")
            input("Presione enter para volver al menú principal...\n")
            menu()   
        else:
            return nombre
    else:
        print("Asegúrese de que la cantidad de caracteres no exceda de 10")
        validacion_nombre()

# Funcion de validacion de cota
def validacion_cota():
    cota = input("Introduzca la cota de la obra, debe tener 4 letras y 4 dígitos (Ejemplo: ABCD1234): \n>>>> ")
    digitos = sum(c.isdigit() for c in cota)
    letras = sum(c.isalpha() for c in cota)
    if (digitos == 4) and (letras == 4):
        cota = cota.upper()
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        p = Path(__file__).with_name('cotaIndice.txt')
        with open(p) as f:
            info = f.readlines()
            f.close()
        lista_cotas = []
        for linea in info:
            lineas = linea.strip().split('/')
            lista_cotas.append(lineas[0])
        if cota in lista_cotas:
            print(f"Ya existe una obra guardada con la cota '{cota}'.")
            input("Presione enter para volver al menú principal...\n")
            menu()
        else:  
            return cota
    else:
        print("\nAsegúrese de que la cota contenga 4 letras y 4 dígitos.")
        validacion_cota()

# Funcion de validacion de precio
def validacion_precio():
    try:
        precio = float(input("\nIntroduzca el precio de la pintura: \n>>>> "))
        if precio > 0:
            return precio
        else:
            print("Introduzca un número valido.")
            validacion_precio()
    except:
        print("Introduzca un número valido.")
        validacion_precio()

# Funcion de validacion del año
def validacion_ano():
    try:
        ano = int(input("\nIntroduzca el año de creación de la pintura: \n>>>> "))
        if ano >= 0 and ano <= 2023:
            return ano
        else:
            print("Introduzca un año valido.")
            validacion_ano()
    except:
        print("Introduzca un año valido.")
        validacion_ano()

# Funcion input y registro de Pintura
def nuevaPintura():
    print("A continuación te pediremos los datos de la pintura a registrar:\n")
    cota = validacion_cota()
    nombre = validacion_nombre()
    precio = str(validacion_precio())
    ano = str(validacion_ano())
    while True:
        selectStatus = input(
            "\nSeleccione el estado de la obra:\n1. EN EXHIBICIÓN.\n2. EN MANTENIMIENTO.\n>>>> ")
        if selectStatus == '1':
            status = 'EN EXHIBICION'
            break
        elif selectStatus == '2':
            status = 'EN MANTENIMIENTO'
            break
        else:
            print(
            "\nValor ingresado fuera de rango. Solo puede ingresar '1' o '2'")  
    regIndexes(nombre, cota, indexDB())
    regPintura(cota, nombre, precio, ano, status)
    input("\nLa pintura ha sido agregada exitosamente.\nPresione enter para volver al menú...\n")
    menu()

# Funcion encargada de compactar la base de datos  
def eliminar():
    selector = input("\nSeleccione como hacer su búsqueda:\n1. Buscar pintura por cota\n2. Buscar pintura por nombre\n>>>> ")
    if selector == '1':
       index = buscarCota()
    elif selector == '2':
       index = buscarNombre()
    if index == '-1':
        print("No se ha encontrado la cota o nombre buscado.")
        input("Presione enter para volver al menú principal...\n")
        menu()
    else:
        index = int(index.replace('\n', ""))
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        p = Path(__file__).with_name('db.txt')
        with open(p) as f:
            g = f.readlines()
            x = g[index].split('/')  
            f.close()
        aux = x[0]
        if aux[0:2] == "##":
            print("La pintura seleccionada ya estaba marcada para como eliminada.")
            input("Presione enter para volver al menú principal...\n")
            menu()  
        x[0] = '##' + x[0]
        cadena = ""
        i = 0
        for elemento in x:
            i = i + 1
            if i == 5:
                cadena = cadena + elemento
            else:
                cadena = cadena + elemento + '/'
        g[index] = cadena
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        p = Path(__file__).with_name('db.txt')
        with open(p, 'w') as f:
            for elemento in g:
                f.write(elemento)
            f.close()
        print("La pintura fue marcada como eliminada exitosamente. Recuerde compactar la base de datos para confirmar su eliminación.")
        input("Presione enter para volver al menú principal...\n")
        menu()   

# Funcion encargada de compactar la base de datos  
def compactar():
    while True:
        opcion = input("\nEsta seguro que quiere proceder con la compactación de la base de datos (S/N):\n>>>> ")
        if opcion == 'S' or opcion == 'N':
            break      
        else:
            print("Ingreso inválido, intente nuevamente.")
    if opcion == 'N':  
        print("\nLa compactación ha sido cancelada con éxito.")
        input("Presione enter para volver al menú principal...\n")
        menu()
    
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    p = Path(__file__).with_name('db.txt')
    with open(p, 'r') as f:
        info = f.readlines()
        f.close()
    cadena = ""
    lista_compactacion = []
    for linea in info:
        if linea[0:2] == "##":
           lista_compactacion.append(linea)
    i = 0
    compactacion = []
    for elemento in lista_compactacion:
        elemento = elemento[2::]
        compactacion.append(elemento)
        i =+ 1
    compactarCotaIndice(compactacion)
    compactarNombreIndice(compactacion)
    compactarBaseDeDatos(compactacion)
    organizarCotaIndices()
    organizarNombreIndices()

    print("\nLa compactación ha sido realizada con éxito.")
    input("Presione enter para volver al menú principal...\n")
    menu()

def organizarCotaIndices():
    return

def organizarNombreIndices():
    return

# Funcion encargada de eliminar las pinturas indicadas en el archivos "cotaIndice.txt"      
def compactarCotaIndice(compactacion):
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    p = Path(__file__).with_name('cotaIndice.txt')
    with open(p, 'r') as f:
        info = f.readlines()
        f.close() 
    for obra in compactacion:
        obra = obra.split('/')
        for i, x in enumerate(info):
            if obra[0] in x[:-3]:
                info.remove(info[i])
    with open(p, 'w') as f:
        f.writelines(info)
        f.close()

# Funcion encargada de eliminar las pinturas indicadas en el archivos "nombreIndice.txt"
def compactarNombreIndice(compactacion):
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    p = Path(__file__).with_name('nombreIndice.txt')
    with open(p, 'r') as f:
        info = f.readlines()
        f.close() 
    for obra in compactacion:
        obra = obra.split('/')
        for i, x in enumerate(info):
            if obra[1] in x[:-3]:
                info.remove(info[i])
    with open(p, 'w') as f:
        f.writelines(info)
        f.close()

# Funcion encargada de eliminar las pinturas indicadas en el archivos "db.txt"
def compactarBaseDeDatos(compactacion):
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    p = Path(__file__).with_name('db.txt')
    with open(p, 'r') as f:
        info = f.readlines()
        f.close()
    for obra in compactacion:
        obra = obra.split('/')
        for i, x in enumerate(info):
            if obra[0] in x[2:10]:
                info.remove(info[i])      
    with open(p, 'w') as f:
        f.writelines(info)
        f.close()

# Funcion que despliega el menú
def menu():
    print("==============================================================\nBienvenido al Sistema Manejador de la Galería de Arte Nacional\n==============================================================")
    selector = input("Seleccione una de las siguientes opciones:\n1. Registrar una nueva pintura\n2. Buscar pintura por cota\n3. Buscar pintura por nombre\n4. Poner pintura en mantenimiento\n5. Poner pintura en exhibición\n6. Eliminar una pintura\n7. Compactar base de datos\n8. Salir del programa\n>>>> ")
    if selector == '1':
        nuevaPintura()
    elif selector == '2':
        buscarBaseDeDatos(buscarCota())
    elif selector == '3':
        buscarBaseDeDatos(buscarNombre())
    elif selector == '4':
        puestaMant()
    elif selector == '5':
        puestaExh()
    elif selector == '6':
        eliminar()
    elif selector == '7':
        compactar()
    elif selector == '8':
        exit()             
    else:
        input("Ha introducido un valor errado, por favor vuelva a intentarlo.\nPresione enter para reiniciar el programa...")
        menu()

# Funcion inicial del programa
menu()