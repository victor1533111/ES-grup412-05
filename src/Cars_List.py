from src.Cars import Cars
from src.Flights import Flights

class Cars_List:

    def __init__(self, listcars: Cars):
        self.listcars = listcars
        pass

    def calcular_precioTotal(self):
        precio_T = 0
        for car in self.listcars:
            precio_T += car.precio_Total
        self.precio_coches=precio_T
        pass
    
    def añadir_vehiculo(self, flight:Flights, ciudad="", precio_por_dia=0, modelo="", codigo="", lugar_recogida="", dias=0):
        if ciudad is not flight.destinos:
            print("no existente en el viaje")
        else:
            for i,x in enumerate(flight.destinos):
                if(ciudad==x):
                    coche = Cars.Cars(codigo,modelo,precio_por_dia,lugar_recogida,dias)
                    self.listcars.insert(i,coche)
                    self.calcular_precioTotal()
        
        pass