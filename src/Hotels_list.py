import Booking
import User
import Hotels

class Hotels_list:
    # Se le pasa una lista de hoteles
    
    def __init__(self, listHotels: Hotels):
        self.listHotels = listHotels
        pass
    
    def confirmar_reserva_Booking(self, usuario: User):
        for hotel in self.listHotels:
            ret = Booking.Booking.confirm_reserve(usuario, hotel) 
            if ret == False:
                return False
        return True
    
    def calcular_precioTotal(self):
        precio_T = 0
        for hotel in self.listHotels:
            precio_T += hotel.precio_Total
        return precio_T
    
    def cancelar_cargo(self):
        print("Se cancela el cargo debido a que no se ha podido realizar la reserva.")