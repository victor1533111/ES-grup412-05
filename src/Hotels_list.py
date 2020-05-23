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
    
    def confirmar_Todos(self, usuario: User, booking: Booking):
        # Retorna Falso reintenta el pago 3 veces y todas son False
        for hotel in self.listHotels:
            intento = 0; ApiReplies=[]; Api = False
            while(intento < 3):
                bookAPI = booking
                ret = bookAPI.confirm_reserve(usuario, bookAPI)
                if type(ret) != list:
                    ApiReplies = ret
                else:
                    ApiReplies = ret[intento]
                if ApiReplies == True:
                    intento += 1
                    Api = True
                    break;
                    print("La reserva se ha realizado correctamente en el intento " + str(intento))
                intento += 1
            if Api == False:
                return False
        print("La reserva de Hoteles se ha realizado correctamente para los " + str(len(self.listHotels)) + " hoteles.")
        return True