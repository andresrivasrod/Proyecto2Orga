import os
from pathlib import Path

# Funcion Wipe todos los index

paintings = []
def bDB(index):
    if index == '-1':
        print("No se ha encontrado la cota o nombre buscado.")
        input("Presione enter para volver al menu principal... ")
        menu()
    else:
        index = int(index.replace('\n', ""))
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
        p = Path(__file__).with_name('db.txt')
        with open(p) as f:
            g = f.readlines()
            x = g[index].split(';')
            print('\nCota: ' + x[0] + '\nNombre: ' + x[1] +
                  '\nPrecio: $' + x[2] + '\nEstatus: ' + x[3])
    input("Presione enter para volver al menu principal... ")
    menu()              

def bCota():
    imp = input("Introduzca la cota que desea buscar: ").upper()
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    p = Path(__file__).with_name('cotaIndex.txt')
    with open(p) as f:
        g = f.readlines()
        l = []
        for x in g:
            l.append(x.split(';'))
        # Comienzo busqueda binaria
        pasos = 0
        izq = 0
        der = len(l) - 1
        while izq <= der:
            pasos += 1
            medio = (izq + der) // 2

            if l[medio][0] == imp:
                return l[medio][1]
            elif l[medio][0] > imp:
                der = medio - 1
            else:
                izq = medio + 1
        return str(-1)

# Funcion de busqueda en archivo nameIndex
def bNombre():
    imp = input("Introduzca el nombre que desea buscar: ").upper()
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    p = Path(__file__).with_name('nameIndex.txt')
    with open(p) as f:
        g = f.readlines()
        l = []
        for x in g:
            l.append(x.split(';'))
        # Comienzo busqueda binaria
        pasos = 0
        izq = 0
        der = len(l) - 1
        while izq <= der:
            pasos += 1
            medio = (izq + der) // 2

            if l[medio][0].upper() == imp:
                return l[medio][1]
            elif l[medio][0].upper() > imp:
                der = medio - 1
            else:
                izq = medio + 1
        return str(-1)        

# Funcion de registrar en archivo nameIndex y cotaIndex
def regIndexes(name, cota, indice):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    p = Path(__file__).with_name('nameIndex.txt')
    with p.open('a') as k:
        k.write(name + ';' + indice + '\n')
    k.close()
    organizrName()

    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    p = Path(__file__).with_name('cotaIndex.txt')
    with p.open('a') as k:
        k.write(cota + ';' + indice + '\n')
    k.close()
    organizrCota()

# Funcion reorganizar archivo cotaIndex
def organizrCota():

    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    p = Path(__file__).with_name('cotaIndex.txt')
    with p.open('r+') as f:
        g = sorted(f)
        f.seek(0)
        for h in g:
            f.write(h)
    f.close()

# Funcion reorganizar archivo nameIndex
def organizrName():

    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    p = Path(__file__).with_name('nameIndex.txt')
    with p.open('r+') as f:
        g = sorted(f)
        f.seek(0)
        for h in g:
            f.write(h)
        f.close()

# Funcion reorganizar archivo cotaIndex
def organizrCota():

    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    p = Path(__file__).with_name('cotaIndex.txt')
    with p.open('r+') as f:
        g = sorted(f)
        f.seek(0)
        for h in g:
            f.write(h)
    f.close()
# Archivo que devuelve el index donde se agregará la pintura
def indexDB():
    y = 0
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    p = Path(__file__).with_name('db.txt')
    with p.open('r') as f:
        for x in f:
            y += 1
        f.close()
    return str(y)

def regPintura(cota, nombre, precio, status):

    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    p = Path(__file__).with_name('db.txt')
    with p.open('a') as f:
        f.write(cota + ';' + nombre + ';' +
                precio + ';' + status + '\n')
        f.close()    
    
# Funcion de validacion de nombre
def validacion_nombre():
  nombre = input("Introduzca el nombre de su pintura (no exceda de 10 caracteres): \n")
  if len(nombre) <= 10:
    return nombre
  else:
    print("Asegúrese de que la cantidad de caracteres no exceda de 10")
    validacion_nombre()

# Funcion de validacion de cota
def validacion_cota():
  cota = input("Introduzca la Cota debe tener 4 letras y 4 dígitos (Ejemplo: ABCD1234): \n")
  digitos = sum(c.isdigit() for c in cota)
  letras = sum(c.isalpha() for c in cota)
  if (digitos == 4) and (letras == 4):
    cota = cota.upper()
    return cota
  else:
    print("Asegúrese de que la cota contenga 4 letras y 4 dígitos.")
    validacion_cota()

# Funcion de validacion de precio
def validacion_precio():
  try:
    precio = float(input("Introduzca el precio de la pintura: \n"))
    assert precio > 0
    return precio

  except (ValueError, AssertionError):
    print("Introduzca un número valido.")
    validacion_precio()

# Funcion input y registro de Pintura
def nuevaPintura():
    print("A continuación te pediremos los datos de la pintura a registrar:\n")
    cota = validacion_cota()
    nombre = validacion_nombre()
    precio = str(validacion_precio())
    selectStatus = input(
            "Seleccione un status:\n1. EN EXHIBICIÓN.\n2. EN MANTENIMIENTO.\n")
    if selectStatus == '1':
        status = 'EN EXHIBICIÓN'
    elif selectStatus == '2':
      status = 'EN MANTENIMIENTO'
    else:
        print(
        "Ha cometido un error escribiendo algún dato, reiniciando el programa de adición...")
        input("Presione enter para continuar.")
        nuevaPintura()
        
    regIndexes(nombre, cota, indexDB())
    regPintura(cota, nombre, precio, status)
    input("La pintura ha sido agregada exitosamente.\nPresione enter para volver al menu...")
    menu()

def menu():
    print("==============================================================\nBienvenido al Sistema Manejador de la Galería de Arte Nacional\n==============================================================")
    selector = input("Seleccione una de las siguientes opciones:\n1. Registrar una nueva pintura.\n2. Buscar pintura por cota.\n3. Buscar pintura por nombre.\n4. Poner pintura en Mantenimiento\n5. Poner pintura en Exhibicion\n6. Eliminar pintura\n7. Compactar\n8. Salir del programa.\n")
    if selector == '1':
        nuevaPintura()
    elif selector == '2':
        bDB(bCota())
    elif selector == '3':
        bDB(bNombre())
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


# Funcion inicial main
menu()