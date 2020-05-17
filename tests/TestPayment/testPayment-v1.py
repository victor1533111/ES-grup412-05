import unittest
from src.PaymentData import PaymentData

class TestPaymentV1(unittest.TestCase):
    
    def test_valid_data(self):
        payment = PaymentData("Pepe", "4323 1234 5478 9123", "123", "VISA", "321")
        valid = PaymentData.validar_datos(payment)
        assert valid == True, "Invalid Data"

    def test_invalid_method(self):
        payment = PaymentData("Pepe", "4323 1234 5478 9123", "123", "visa", "321")
        valid = PaymentData.validar_datos(payment)
        assert valid == False, "Invalid Method"

    def test_invalid_import(self):
        payment = PaymentData("Pepe", "4323 1234 5478 9123", "123", "VISA", "-321")
        valid = PaymentData.validar_datos(payment)
        assert valid == False, "Invalid Negative Import"

    def test_empty_data(self):
        payment = PaymentData("", "", "", "", "")
        valid = PaymentData.validar_datos(payment)
        assert valid == False, "Invalid data, data is empty"

if __name__ == "__main__":
    unittest.main()

