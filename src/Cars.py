import sys
sys.path.append('../../src/')
import User
import Rentalcars

class Cars:

    def __init__(self,codigo,marca,precio,lugar_recojida,duracion_reserva):

        self.codigo=codigo
        self.marca = marca
        self.lugar_recojida=lugar_recojida

        self.duracion_reserva =duracion_reserva
        self.precio_total = precio * duracion_reserva


        pass

    def confirmar_reserva_vehiculos(self,usuario:User,rentalcars: Rentalcars):
        
        
        print("Se ha realizado la reserva de los vehiculos correctamente")
        return rentalcars.confirm_reserve(usuario,self)
        
        
    def confirmar_reserva_vehiculos_conerrores(self,usuario:User,rentalcars: Rentalcars):  
        intento = 0; rentalReplies=[]
        while(intento < 3):
            reply = rentalcars.confirm_reserve(usuario,self)
            if type(reply) != list:
                rentalReplies = reply
            else:
                rentalReplies = reply[intento]
            if rentalReplies == True:
                intento += 1
                print("La reserva se ha realizado correctamente en el intento " + str(intento))
                return True
            intento += 1
        print("No se ha podido realizar la reserva , se ha intentado " + str(intento) + " veces.")
        return False
  
            
                
        