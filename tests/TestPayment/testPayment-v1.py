import Bank
import User

class PaymentData:

    def __init__(self, titular, num_tarjeta, cvc, method, import_):
        self.titular = titular
        self.num_tarjeta = num_tarjeta
        self.cvc = cvc
        self.method = method
        self.import_ = import_
        pass
    
    def validar_datos(self):

        if self.method != "VISA" and self.method != "MASTERCARD":
            return False
        
        # Negative Imports
        if int(self.import_) < 0:
            return False
        
        # Empty elements
        if not self.titular or not self.num_tarjeta or not self.cvc or not self.method or not self.import_:
            return False
        
        # Non-string elements
        if not all(isinstance(element, str) for element in [self.titular, self.num_tarjeta, self.cvc, self.method, self.import_]):
            return False
    
        return True
    
    def confirmar_Pago(self, usuario: User, banco: Bank):
        reply = banco.do_payment(usuario,self)
        if reply == False:
            print("No se ha podido realizar el pago")
            return False
        else:
            print("El pago se ha realizado correctamente")
            return True
    
    def confirmar_Pago_con_Reintento(self, usuario: User, banco: Bank):
        # Si retorna Falso reintenta el pago 3 veces
        intento = 0; bankReplies=[]
        while(intento < 3):
            reply = banco.do_payment(usuario,self)
            bankReplies.append(reply[intento])
            if bankReplies[intento] == False:
                print("No se ha podido realizar el pago en el intento " + str(intento))
            else:
                print("El pago se ha realizado correctamente en el intento " + str(intento))
                intento += 1
                return True, intento
            intento += 1
        print("No se ha podido realizar el pago, se ha intentado " + str(intento) + " veces.")
        return False, intento
        
   