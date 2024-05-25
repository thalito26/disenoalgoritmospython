import os 
from .Variables import save, getAll,student
from tabulate import tabulate
def create():
    os.system('clear')
    print("""             
              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
              ~~~ Formulario registro ~~~
              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
          """)
    save({
        "Nombre": input("ingresa tu nombre: "),
        "Apellido": input("Ingresa tu apellido: "),
        "Edad": int(input("Ingresa tu edad: "))
    })
    os.system('pause')

def read(codigo=None):#declarar una variable
    os.system("clear")
    print("""             
              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
              ~~~ Formulario registro ~~~
              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
          """)
    if(codigo==None)#se busca el codigo
        for i,val in enumerate(getAll()):
            print(f"""
            ________________
            Codigo: {i+1}
            Nombre: {val.get('Nombre')}
            Apellido: {val.get('Apellido')}
            Edad: {val.get('Edad')}
            _________________
            """)
    else: 
        val = getAll()[codigo-1]
          print(f"""
            ________________
            Codigo: {i+1}
            Nombre: {val.get('Nombre')}
            Apellido: {val.get('Apellido')}
            Edad: {val.get('Edad')}
            _________________
            """)
    os.system("pause")

    # from tabulate import tabulate
    # getAll= ["Nombre"],
    # ["Apellido"],
    # ["Edad"]
    # headers = ["Nombre", "Apellido", "Edad"]
    # print(tabulate(getAll,headers()))
os.system('pause')
def update():
    bandera=True
    while(bandera)
    os.system
    read ()
    print("""
                  ~~~~~~~~~~~~~~~~~~~~~~~~~
                  ~~~ Actualizar camper ~~~
                  ~~~~~~~~~~~~~~~~~~~~~~~~~
          """)
    codigo=int(input("¿Codigo del camper que desea eliminar"))
    read (codigo)
    print("""
        ¿Seguro que desea actualizar el camper?
            1. Si
            2. No
            3. Cancelar
        """)
        opc = int(input())
        match (opc)
            case 1:
                val= {
                    "Nombre": input("ingresa tu nombre: "),
                    "Apellido": input("Ingresa tu apellido: "),
                    "Edad": int(input("Ingresa tu edad: "))
                }
                camper[codigo-1]-val# camper[codigo-1].update(val)
                os.system("clear")
                print(f"""
                El camper fue actualizado
                ________________
                Codigo: {i+1}
                Nombre: {val.get('Nombre')}
                Apellido: {val.get('Apellido')}
                Edad: {val.get('Edad')}
                _________________
                """)
                os.system("pause")
                bandera = false
            case 3:
                bandera = false
def delete():
    bandera=True
    while(bandera)
    os.system("clear")
    read()
    print("""
                  ~~~~~~~~~~~~~~~~~~~~
                  ~~~ Eliminar camper ~~~
                  ~~~~~~~~~~~~~~~~~~~~
          """)
    codigo=int(input("¿Codigo del camper que desea eliminar"))
    read(codigo)
        print("""
        ¿Seguro que desea eliminar el camper?
            1. Si
            2. No
            3. Cancelar
        """)
        opc = int(input())
        match (opc)
            case 1:
                 val = camper.pop(codigo-1)
                 os.system("clear")
                    print(f"""
                EL CAMPER ELIMINADO FUE    
                ________________
                Codigo: {i+1}
                Nombre: {val.get('Nombre')}
                Apellido: {val.get('Apellido')}
                Edad: {val.get('Edad')}
                _________________
                """)
                os.system("pause")
                bandera = false
            case 3:
                bandera = false
    # student=input("ingresa el nombre del camper a eliminar")
    # for i,item in save:
    #     if (student in save):
    #      save.pop(i)
    # print("el camper se borro")

def menu():
    menu=["Guardar", "Buscar", "Actualizar", "Eliminar","Salir"]
    while(True):
        os.system('cls')
        print("""
                  ~~~~~~~~~~~~~~~~~~~~
                  ~~~ Menu camper ~~~
                  ~~~~~~~~~~~~~~~~~~~~
          """)
        print("".join([f"{i+1}. {val}\n" for i, val in enumerate(menu)]))
        try:
            opc=int(input())
            if(opc<=len(menu)and opc>0):
                match(opc):
                    case 1: create()
                    case 2: read()
                    case 3: update()
                    case 4: delete()
                    case 5: break
        except ValueError:
                    print(f"La opcion no esta disponible")

