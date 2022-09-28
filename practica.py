from array import array
from time import sleep
import numpy
import matplotlib
datos=[]

def agregar():
    print("Ingrese dato a leer")
    Dato = input("ingrese dato\n")
    datos.append(Dato)
    sleep(3)
    main()
        

def eliminar():
    print("Ingrese dato a eliminar")
    DatoElim= input("ingrese dato a eliminar\n")
    if datos>0:
        try:
            datos.remove(DatoElim)
            sleep(3)
        except:
            print("No existe el dato\n")
            sleep(3)
        
    else: print("no hay datos en el arreglo\n")
    sleep(3)
    main()

def listar():
    print(datos)
    sleep(3)
    main()

def main():
    print("Bienvenido, eliga un numero para elegir funcion \n")
    print("---------------------------------------------------")
    print("1. Agregar \n")
    print("2. Eliminar \n")
    print("3. Vizualizar \n")
    print("---------------------------------------------------")

    select = input("inserte valor deseado\n")
    if select =="1":
        agregar()
    elif select =="2":
        eliminar()
    elif select =="3":
        listar()
    else: print("valor no encontrado")
    


if __name__ == '__main__':
    main()



        


