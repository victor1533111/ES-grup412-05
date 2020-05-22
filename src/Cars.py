from src.User import User
from src.Rentalcars import Rentalcars
class Cars:

    def __init__(self,codigo,marca,precio,lugar_recojida,duaracion_reserva):

        self.codigo=codigo
        self.marca = marca
        self.lugar_recojida=lugar_recojida
        self.duracion_reserva =duaracion_reserva
        self.precio_total = precio * duaracion_reserva

        pass

    def confirmar_reserva_vehiculos(self,usuario:User,rentalcars: Rentalcars):
        
        
        if rentalcars.confirm_reserve(usuario,self) == False:
            print("No se ha podido realizar la reserva de los vehiculos")
            return False
        else:
            print("Se ha realizado la reserva de los vehiculos correctamente")
            return True