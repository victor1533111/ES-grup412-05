class Flights:

    def __init__(self, viajeros):
        if(viajeros>0):
            self.viajeros=viajeros
        else:
            print("El numero de viajeros es incorrecto, debe ser superior a uno.")
        pass