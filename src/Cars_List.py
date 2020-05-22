import sys
sys.path.append('../../src/')
import Flights_list
import Cars_List
import Cars

class Cars_List:

    def __init__(self, listcars: Cars):
        self.listcars = listcars
        pass

    def calcular_precioTotal(self):
        precio_T = 0
        for car in self.listcars:
            precio_T += car.precio_total
        self.precio_coches=precio_T
        pass
    
    def añadir_vehiculo(self, flight_l:Flights_list, ciudad, precio_por_dia, modelo, codigo, lugar_recogida, dias):    
        for i,x in enumerate(flight_l.listVuelos):
            if(ciudad==x.destinacio):
                coche = Cars.Cars(codigo,modelo,precio_por_dia,lugar_recogida,dias)
                self.listcars.insert(i,coche)
                self.calcular_precioTotal()
        
        pass