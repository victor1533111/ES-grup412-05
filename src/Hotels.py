import Booking
import User

class Hotels:
    
    def __init__(self, codigo, nombre, num_huespedes, num_habitacions, duracion_reserva, precio):
        self.codigo=codigo
        self.nombre=nombre
        self.num_huespedes=num_huespedes
        self.num_habitacions=num_habitacions
        self.duracion_reserva=duracion_reserva
        self.precio
        self.precio_Total = self.precio * self.num_habitacions * self.duracion_reserva
        pass
