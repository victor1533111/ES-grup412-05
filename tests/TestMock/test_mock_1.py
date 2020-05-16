import unittest
from src.Flights import Flights
from src.User import User
from unittest import mock
from requests.exceptions import Timeout

class TestMock1(unittest.TestCase):
    
    @mock.patch('src.Flights.vuelos')
    def test_gestiopassatgers(self,mock_vuelos):
        usuario = User("Ruben","4712458T","Calle Vic","645548572","rubenjibo@gmail.com")
        destinos = ["Madrid","Valencia","Lisboa"]
        vuelo = Flights(5,usuario,"Barcelona",destinos,200)
