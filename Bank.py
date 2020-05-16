import User
import PaymentData


class Bank:

    def __init__(self):
        pass

    def do_payment(self, user: User, payment_data: PaymentData):
        while PaymentData.validar_datos(payment_data) == False:
            PaymentData.pedir_datos()
        else:
            
        return True