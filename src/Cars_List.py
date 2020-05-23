import sys
sys.path.append('../../src/')
import Flights_list
import Cars
import Rentalcars

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
    
    def confirmar_reserva(self,usuario,api_Rentalcars: Rentalcars):
        # Retorna Falso reintenta el pago 3 veces y todas son False
        for car in self.listcars:
            intento = 0; ApiReplies=[]; Api = False
            while(intento < 3):
                rental = api_Rentalcars
                ret = rental.confirm_reserve(usuario, rental)
                if type(ret) != list:
                    ApiReplies = ret
                else:
                    ApiReplies = ret[intento]
                if ApiReplies == True:
                    intento += 1
                    Api = True
                    break;
                    print("la reserva se ha realizado correctamente en el intento " + str(intento))
                intento += 1
            if Api == False:
                return False
        print("La reserva de Cars se ha realizado correctamente para los " + str(len(self.listcars)) + " coches.")
        return True