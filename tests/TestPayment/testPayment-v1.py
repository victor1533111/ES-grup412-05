import unittest
import PaymentData
from unittest import mock

class TestMockPayment(unittest.TestCase):
    
    def test_valid_data(self)
        payment = PaymentData("Pepe", "4323 1234 5478 9123", "123", "VISA", "321")
        valid = PaymentData.validar_datos(payment)
        assert valid == True

    def test_invalid_method(self)
        payment = PaymentData("Pepe", "4323 1234 5478 9123", "123", "visa", "321")
        valid = PaymentData.validar_datos(payment)
        assert valid == False

    def test_invalid_import(self)
        payment = PaymentData("Pepe", "4323 1234 5478 9123", "123", "VISA", "-321")
        valid = PaymentData.validar_datos(payment)
        assert valid == False

    def test_invalid_types(self)
        payment = PaymentData("Pepe", "4323 1234 5478 9123", "123", "VISA", 321)
        valid = PaymentData.validar_datos(payment)
        assert valid == False

    def test_empty_data(self)
        payment = PaymentData("", "", "", "", "")
        valid = PaymentData.validar_datos(payment)
        assert valid == False
    
    pass

