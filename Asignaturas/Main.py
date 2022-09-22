#python permite meter mas de una clase en un archivo, en otros lenguajes se deben separar.
#programa que permita crear asignaturas Asignatura debe consumir a Profesor

from Asignatura import *

lista_asignaturas = []
asig = Asignatura(0,0,0,0)

asig.ingresarAsignatura(lista_asignaturas)
asig.mostrarAsignaturas(lista_asignaturas)

