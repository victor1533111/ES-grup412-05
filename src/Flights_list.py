import Skyscanner
import User
import Flights

class Flights_list:
    # Se le pasa una lista de hoteles
    
    def calcular_precioTotal(self):
        precio_T = 0
        for vuelo in self.listVuelos:
            precio_T += vuelo.CalcularPrecio_vuelo()
        return precio_T
    
    def __init__(self, listVuelos: Flights, usuario: User):
        self.usuario = usuario
        
        if listVuelos == None:
            self.listVuelos = []
            return
        
        for vuelo in listVuelos:
            if vuelo.destinacio == None or vuelo.origen == None:
                self.listVuelos = []
                return
        
        self.listVuelos = listVuelos
        pass
    
    def getListaDestinos(self):
        l = []
        for vuelo in self.listVuelos:
            l.append(vuelo.destinacio)
        return l
    
    def AñadirDestino(self, codi_vol, origen, destinacio, num_passatgers, precio_vuelo, posicion_del_vuelo):
        vuelo = Flights.Flights(codi_vol,origen, destinacio, num_passatgers, precio_vuelo)
        self.listVuelos.insert(posicion_del_vuelo, vuelo)
        pass
    
    def BorrarDestino(self, posicion_del_vuelo):
        self.listVuelos.pop(posicion_del_vuelo)
        pass
    
    def confirmar_Todos(self, skyscanner: Skyscanner):
        # Retorna Falso reintenta el pago 3 veces y todas son False
        for vuelo in self.listVuelos:
            intento = 0; ApiReplies=[]; Api = False
            while(intento < 3):
                sky = skyscanner
                ret = sky.confirm_reserve(self.usuario, sky)
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
            print("No se ha podido realizar la reserva, se ha intentado " + str(intento) + " veces.")
            if Api == False:
                return False
        return True
    
    def Gestionar_Errores_Pago(self, usuario: User, sky: Skyscanner):
        
        reply = self.Confirmar_todos(sky)
        
        if reply == False:
            print("No se ha podido realizar el pago")
            return False
        else:
            print("El pago se ha realizado correctamente")
            return True