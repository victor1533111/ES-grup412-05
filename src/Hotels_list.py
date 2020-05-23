import Booking
import User
import Hotels

class Hotels_list:
    # Se le pasa una lista de hoteles
    
    def __init__(self, listHotels: Hotels):
        if listHotels == None:
            self.listHotels = []
            return
        self.listHotels = listHotels
        pass
    
    def confirmar_reserva_Booking(self, usuario: User, booking: Booking):
        for hotel in self.listHotels:
            book = booking
            ret = book.confirm_reserve(usuario, hotel) 
            if ret == False:
                return False
        return True
    
    def calcular_precioTotal(self):
        precio_T = 0
        for hotel in self.listHotels:
            precio_T += hotel.precio_Total
        return precio_T
    
    
    def AñadirHotel(self, codigo, nombre, num_huespedes, num_habitacions, duracion_reserva, precio, posicion_hotel):
        hotel = Hotels.Hotels(codigo, nombre, num_huespedes, num_habitacions, duracion_reserva, precio)
        self.listHotels.insert(posicion_hotel, hotel)
        pass
    
    def BorrarHotel(self, posicion_hotel):
        self.listHotels.pop(posicion_hotel)
        pass