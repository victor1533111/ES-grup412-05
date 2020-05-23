import unittest
from unittest import mock
import sys
sys.path.append('../../src/')
import PaymentData
import User
import Bank
import Hotels_list
import Flights_list


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
    
    def test_gestionar_metodo_valido(self):
        usuario = User.User("Pepe", "2051923A", "C/ Bolets", "93333333", "jibo@gmail.com")
        banco = Bank.Bank()
        payment = PaymentData.PaymentData("Pepe", "4323 1234 5478 9123", "123", "VISA", "321")
        bank_reply = payment.confirmar_Pago(usuario, banco)
        assert bank_reply == True, "The payment is denied when it should be accepted"
    
    def test_gestionar_metodo_invalido(self):
        with mock.patch('Bank.Bank') as MockBank:
            MockBank.do_payment.return_value = False
            usuario = User.User("Pepe", "2051923A", "C/ Bolets", "93333333", "jibo@gmail.com")
            payment = PaymentData.PaymentData("Pepe", "4323 1234 5478 9123", "123", "VISA", "321")
            bank_reply = payment.confirmar_Pago(usuario, MockBank)
            assert bank_reply == False, "The payment is accepted when it should be denied"
    
    '''Dado un viaje con múltiples destinos y más de un viajero, cuando se produce un
    error al realizar el pago, se reintenta realizar el pago'''
    def test_pagofallido_reintento(self):
        with mock.patch('Bank.Bank') as MockBank:
            MockBank.do_payment.return_value = [True, True, True]
            usuario = User.User("Ruben", "4712458T", "Calle Vic","645548572", "rubenjibo@gmail.com")
            precioT = 350
            payment = PaymentData.PaymentData("Pepe", "4323 1234 5478 9123", "123", "VISA", str(precioT))
            bank_reply, intentos = payment.confirmar_Pago_con_Reintento(usuario, MockBank)
            assert intentos == 1, "The payment is accepted when it should be denied"
    
    '''Dado un viaje con múltiples destinos y más de un viajero, cuando se produce un
    error al realizar el pago, se reintenta realizar el pago'''
    def test_pagofallido_reintentoCorrectos(self):
        with mock.patch('Bank.Bank') as MockBank:
            MockBank.do_payment.return_value = [False, True, True]
            usuario = User.User("Ruben", "4712458T", "Calle Vic","645548572", "rubenjibo@gmail.com")
            precioT = 350
            payment = PaymentData.PaymentData("Pepe", "4323 1234 5478 9123", "123", "VISA", str(precioT))
            bank_reply, intentos = payment.confirmar_Pago_con_Reintento(usuario, MockBank)
            
            assert intentos == 2, "The payment is accepted when it should be denied"
            
    '''Dado un viaje con múltiples destinos y más de un viajero, cuando se produce un
    error al realizar el pago, se reintenta realizar el pago'''
    def test_pagofallido_reintentoIncorrectos(self):
        with mock.patch('Bank.Bank') as MockBank:
            MockBank.do_payment.return_value = [False, False, False]
            usuario = User.User("Ruben", "4712458T", "Calle Vic","645548572", "rubenjibo@gmail.com")
            precioT = 350
            payment = PaymentData.PaymentData("Pepe", "4323 1234 5478 9123", "123", "VISA", str(precioT))
            bank_reply, intentos = payment.confirmar_Pago_con_Reintento(usuario, MockBank)
            
            assert intentos == 3, "The payment is accepted when it should be denied"
            

if __name__ == "__main__":
    unittest.main()


