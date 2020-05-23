import sys
sys.path.append('../../src/')
import Flights_list
import Cars

class Cars_List:

    def __init__(self, listcars: Cars):
        if listcars == None:
            self.listcars = []
            return
        self.listcars = listcars
        pass
    
    def calcular_precioTotal(self):
        precio_T = 0
        for car in self.listcars:
            precio_T += car.precio_total
        self.precio_coches=precio_T
        return precio_T
        pass
    
    def añadir_vehiculo(self, flight_l:Flights_list, ciudad, precio_por_dia, modelo, codigo, lugar_recogida, dias):    
        for i,x in enumerate(flight_l.listVuelos):
            if(ciudad==x.destinacio):
                coche = Cars.Cars(codigo,modelo,precio_por_dia,lugar_recogida,dias)
                self.listcars.insert(i,coche)
                self.calcular_precioTotal()
        
        pass
    
    def eliminar_vehiculo(self, flight_l:Flights_list, ciudad, precio_por_dia, modelo, codigo, lugar_recogida, dias):
        for i,x in enumerate(flight_l.listVuelos):
            if(ciudad==x.destinacio):
                self.listcars.pop(i)
                self.calcular_precioTotal()
        pass
    
    def confirmar_reserva(self,usuario,api_Rentalcars):
        reserva_coches = api_Rentalcars.confirm_reserve(usuario,self.listcars)
        if reserva_coches == True:
            print("La reserva de los coches se ha realizado correctamente")
        intentos_reserva_coches=1
        while reserva_coches == False:
            reserva_coches = api_Rentalcars.confirm_reserve(usuario,self.listcars)
            intentos_reserva_coches =+ 1 
            if intentos_reserva_coches == 3:
                print("Ha habido un problema durante el proceso de confirmación de la reserva y no se le ha efectuado ningún cargo.")
                print("Intentelo mas tarde.")
                return 0
        return True