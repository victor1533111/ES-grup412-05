import User
import Skyscanner

class Flights:

    def CalcularPrecio_vuelo(self):
        return self.precio_vuelo * self.num_passatgers

    def __init__(self, codi_vol, origen, destinacio, num_passatgers, precio_vuelo):
        
        if(num_passatgers<1):
            print("El numero de viajeros es incorrecto, debe ser superior a uno.")
        else:
            self.codi_vol = codi_vol
            self.origen = origen
            self.destinacio = destinacio
            self.num_passatgers = num_passatgers
            self.precio_vuelo = precio_vuelo
        pass
    
