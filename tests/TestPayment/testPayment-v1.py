import PaymentData
import unittest

class TestPaymentV1(unittest.TestCase):
    
    def test_valid_data(self):
        payment = PaymentData.PaymentData("Pepe", "4323 1234 5478 9123", "123", "VISA", "321")
        valid = PaymentData.PaymentData.validar_datos(payment)
        assert valid == True, "Invalid Data"

    def test_invalid_method(self):
        payment = PaymentData.PaymentData("Pepe", "4323 1234 5478 9123", "123", "visa", "321")
        valid = PaymentData.PaymentData.validar_datos(payment)
        assert valid == False, "Invalid Method, check uppercase (VISA or MASTERCARD are the only valid options"

    def test_invalid_import(self):
        payment = PaymentData.PaymentData("Pepe", "4323 1234 5478 9123", "123", "VISA", "-321")
        valid = PaymentData.PaymentData.validar_datos(payment)
        assert valid == False, "Invalid Negative Import"

    def test_empty_data(self):
        payment = PaymentData.PaymentData("", "", "", "", "")
        valid = PaymentData.PaymentData.validar_datos(payment)
        assert valid == False, "Invalid data, data is empty"
        
    def test_empty_types(self):
        payment = PaymentData.PaymentData("Pepe", "4323 1234 5478 9123", 123, "VISA", 321)
        valid = PaymentData.PaymentData.validar_datos(payment)
        assert valid == False, "Invalid data types"

if __name__ == "__main__":
    unittest.main()


