class PaymentData:

    def __init__(self, titular, num_tarjeta, cvc, method, import_):
        self.titular = titular
        self.num_tarjeta = num_tarjeta
        self.cvc = cvc
        self.method = method
        self.import_ = import_
        pass
    
    def validar_datos(self):
        if self.method != "VISA" or self.method != "MASTERCARD":
            return False
        if self.import_ < 0:
            return False
        return True