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

