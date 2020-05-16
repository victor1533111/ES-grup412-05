import unittest
from src.Flights import Flights
from src.User import User
from unittest import mock
from requests.exceptions import Timeout

class TestMock1(unittest.TestCase):
     
    @mock.patch('src.Flights')
    def test_confirmarvuelos(self,mock_vuelos):
        self.assertTrue(mock.Flights.confirmarvuelos()
        mock_vuelos.confirmarvuelos().return_value = FALSE
        self.assertFalse(mock.Flights.confirmarvuelos( usuario, vuelos))
        