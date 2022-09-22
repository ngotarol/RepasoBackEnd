class Jugador:
    nombre = ""
    numero = 0

    def __init__(self, numero, nombre) :
        self.numero = numero
        self.nombre = nombre
    
    def ingresarJugadores(self, lst_jugadores):
        rpt = "si"        
        while rpt == "si":
            while True:
                try:
                    numero = int(input("Ingrese número del jugador: \n"))
                    break
                except ValueError: 
                    print("Debe ingresar un número entero\n")
            nombre = input("Ingrese nombre del jugador\n")
            p = Jugador(numero,nombre)
            lst_jugadores.append(p)
            rpt = input("Ingresar otro jugador: si/no \n")
        while not(rpt=="si" or rpt=="no"):
            print("Debe indicar si o no")
            rpt = input("Ingresar otro jugador: si/no \n")


    def buscarNroJugador(self,lst_jugadores):
        esta = False
        while True:
            try:
                numero = int(input("Ingrese número del jugador a buscar: \n"))
                break
            except ValueError: 
                print("Debe ingresar un número entero\n")
        for i in lst_jugadores:
            if numero == i.numero:
                print("El nombre del jugador es ", i.nombre)
                esta = True
        if not esta:
            print("No se encontró un jugador con ese número")      
