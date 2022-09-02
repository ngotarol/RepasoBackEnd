#crear un programa que permita ingresar 100 numeros enteros. Calcule e imprima lo siguiente:
# 1. Cantidad de numeros pares ingresados.
# 2. Valor del número mayor ingresado indicando cuantas veces se ingreso.


def ingresar(lst_n):
    for i in range(100):
        while True:
            try:
                numero = int(input("Ingrese un número\n"))
                break
            except ValueError:
                print("Debe ingresar un número entero, vuelva a intentar")
        lst_n.append(numero)
    pass

def contar_pares(lst_1):
    cont_par = 0
    for i in lst_1:
        if i%2==0:
            cont_par+=1
    return cont_par
    
def buscar_mayor(lst_2):
    #max(lst_2)
    mayor = lst_2[0]
    for i in lst_2:
        if i>mayor: mayor=i
    return i

def contar_mayor(lst_3,num_may):
    cont = 0
    for i in lst_3:
        if i == num_may: cont+=1
    return cont
    
def imprimir(pares,num_may,cant):
    print(f"Se ingresaron {pares} número(s) par(es), y el número mayor es {num_may} y se repitió {cant} veces")

lista_numeros = []

ingresar(lista_numeros)
cantidad_pares = contar_pares(lista_numeros)
nro_mayor = buscar_mayor(lista_numeros)
cantidad = contar_mayor(lista_numeros,nro_mayor)
imprimir(cantidad_pares,nro_mayor,cantidad)