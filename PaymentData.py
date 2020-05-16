class PaymentData:

    def __init__(self, titular, num_tarjeta, cvc, method, import_):
        self.titular = titular
        self.num_tarjeta = num_tarjeta
        self.cvc = cvc
        self.method = method
        self.import_ = import_
        pass
    
    def validar_datos(self):
        return True