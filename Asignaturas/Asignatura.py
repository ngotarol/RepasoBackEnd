from Profesor import *

class Asignatura:
    codigo = ""
    nombre = ""
    horas = 0
    lista_profesores = []

    def __init__(self,codigo,nombre,horas,lista_profesores):
        self.codigo = codigo
        self.nombre = nombre
        self.horas = horas
        self.lista_profesores = lista_profesores
        pass

    def ingresarAsignatura(self, lst_asignaturas):
        rpt = "si"        
        while rpt == "si":
            codigo = input("Ingrese codigo de la asignatura\n")
            nombre = input("Ingrese nombre de la asignatura\n")
            while True:
                try:
                    horas = int(input("Ingrese horas de la asignatura: \n"))
                    break
                except ValueError: 
                    print("Debe ingresar un número entero\n")
            lst_profesores = []
            rp="si"
            while rp == "si":
                rut = input("Ingrese rut\n")
                nombre_prof = input("Ingrese Nombre del profesor\n")
                profesion = input("ingrese profesion\n")
                p = Profesor(rut,nombre_prof,profesion)
                lst_profesores.append(p)
                rp = input("Ingresar otro profesor: si/no \n")
            while not(rp=="si" or rp=="no"):
                print("Debe indicar si o no")
                rp = input("Ingresar otro profesor: si/no \n")
            a = Asignatura(codigo,nombre,horas,lst_profesores)
            lst_asignaturas.append(a)
            rpt = input("Ingresar otra asignatura: si/no \n")
        while not(rpt=="si" or rpt=="no"):
            print("Debe indicar si o no")
            rpt = input("Ingresar otra asignatura: si/no \n")
        pass

    def mostrarAsignaturas(self, lst_asignaturas):
        for i in lst_asignaturas:
            print("_________________________________________________________________________")
            print(f"Código: {i.codigo} Nombre: {i.nombre} Horas: {i.horas}")
            for x in i.lista_profesores:
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
                print(f"Rut: {x.rut} Nombre: {x.nombre} Profesion: {x.profesion}")
