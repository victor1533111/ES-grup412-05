import unittest
from unittest import mock
import sys
sys.path.append('../../src/')
import Flights
import User
import Flights_list
import Cars_List

class testCars(unittest.TestCase):
    def test_añadir_vehiculo(self):
          usuario = User.User("Ruben", "4712458T", "Calle Vic", "645548572", "rubenjibo@gmail.com")
          num_p=2
          vuelo = []
          vuelo.append(Flights.Flights("1234", "Barcelona", "Valencia", num_p, 20))
          lista_vuelos = Flights_list.Flights_list(vuelo, usuario)
          precio_por_dia=20
          dias=5
          codigo=123
          ciudad="Valencia"
          modelo="Seat"
          lugar_recogida="calle Valencia"
          cars = []
          lista_Cars=Cars_List.Cars_List(cars)
          lista_Cars.añadir_vehiculo(lista_vuelos,ciudad,precio_por_dia,modelo , codigo, lugar_recogida,dias)
          assert lista_Cars.precio_coches == precio_por_dia*dias
          
         
            
if __name__ == "__main__":
    unittest.main()

        
