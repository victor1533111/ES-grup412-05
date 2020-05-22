import Skyscanner
import User
import Flights

class Flights_list:
    # Se le pasa una lista de hoteles
    
    def calcular_precioTotal(self):
        precio_T = 0
        for vuelo in self.listVuelos:
            precio_T += vuelo.CalcularPrecio()
        return precio_T
    
    def __init__(self, listVuelos: Flights, usuario: User):
        self.usuario = usuario
        self.listVuelos = listVuelos
        pass

    def AñadirDestino(self, codi_vol, destinacio, num_passatgers, precio_vuelo, posicion_del_vuelo):
        vuelo = Flights.Flights(codi_vol, destinacio, num_passatgers, precio_vuelo)
        self.listVuelos.insert(posicion_del_vuelo, vuelo)
        pass
    
    def BorrarDestino(self,posicion_del_vuelo):
        self.listVuelos.erase(posicion_del_vuelo)
        pass