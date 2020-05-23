import sys
sys.path.append('../../src/')
import Flights_list
import Hotels_list
import Cars_List

class User:

    def __init__(self, name, DNI, direccion, telf, email):
        self.name = name
        self.DNI = DNI
        self.direccion = direccion
        self.telf = telf
        self.email = email
        pass

    def Trip(self, lista_vuelos: Flights_list, hotel_list: Hotels_list, car_list: Cars_List, fecha_in, fecha_f):
        self.lista_vuelos = lista_vuelos
        self.hotel_list = hotel_list
        self.car_list = car_list
        self.fecha_inicio = fecha_in
        self.fecha_final = fecha_f
    
    def calcularPrecioT(self):
        precioVuelos = self.lista_vuelos.calcular_precioTotal()
        precioHoteles = self.hotel_list.calcular_precioTotal()
        precioCars = self.car_list.calcular_precioTotal()
        return(precioVuelos + precioHoteles + precioCars)
    
    def comprobar_datos(self):
        
        if type(self.name) !=str:
            return False
        if type(self.DNI) !=str:
            return False
        if type(self.direccion) !=str:
            return False
        if type(self.telf) !=str:
            return False
        if type(self.email) !=str:
            return False

        return True
      