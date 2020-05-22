from src.User import User
from src.Rentalcars import Rentalcars
from src.Flights import Flights

class Cars:

    def __init__(self,codigo,marca,lugar_recojida,duaracion_reserva):

        self.codigo=codigo
        self.marca = marca
        self.lugar_recojida=lugar_recojida
        self.duracion_reserva =duaracion_reserva

        pass

    def confirmar_reserva_vehiculos(self,usuario:User,rentalcars: Rentalcars):
        
        
        if rentalcars.confirm_reserve(usuario,self) == False:
            print("No se ha podido realizar la reserva de los vehiculos")
            return False
        else:
            print("Se ha realizado la reserva de los vehiculos correctamente")
            return True
        
        pass
        
    def añadir_vehiculo(self, flight:Flights, ciudad, precio_vehiculo):
        if ciudad is not flight.destinos:
            print("no existente en el viaje")

            
                
        