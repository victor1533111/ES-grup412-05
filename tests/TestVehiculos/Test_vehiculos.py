import unittest
from unittest import mock
import sys
sys.path.append('../../src/')
import Flights
import User
import Flights_list
import Cars_List
import Cars
import Rentalcars

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

    def test_eliminar_vehiculo(self):
      usuario = User.User("Ruben", "4712458T", "Calle Vic", "645548572", "rubenjibo@gmail.com")
      num_p=2
      vuelo = []
      vuelo.append(Flights.Flights("1234", "Barcelona", "Valencia", num_p, 20))
      lista_vuelos = Flights_list.Flights_list(vuelo, usuario)
      precio_por_dia = 20
      dias=5
      codigo=123
      ciudad="Valencia"
      modelo="Seat"
      lugar_recogida="calle Valencia"
      cars = []
      cars.append(Cars.Cars(codigo,modelo,precio_por_dia,lugar_recogida,dias))
      lista_Cars=Cars_List.Cars_List(cars)    
      lista_Cars.eliminar_vehiculo(lista_vuelos,ciudad,precio_por_dia,modelo , codigo, lugar_recogida,dias)
      assert lista_Cars.precio_coches == 0

    ''' V4 - Dado un viaje con múltiples destinos y más de un viajero, cuando se produce un
    error al confirmar los alojamientos, se reintenta realizar la confirmación'''
    def test_confirmarfallido_reintento(self):
        with mock.patch('Rentalcars.Rentalcars') as MockRental:
            MockRental.confirm_reserve.return_value = [True, True, True]
            usuario = User.User("Ruben", "4712458T", "Calle Vic","645548572", "rubenjibo@gmail.com")
            lista_vuelos = Flights_list.Flights_list(None, usuario)
            lista_vuelos.AñadirDestino("3214", "Valencia", "Madrid", 5, 50, 0) 
            lista_vuelos.AñadirDestino("2323", "Madrid", "Amsterdam", 5, 50, 1)
            lista_cars = Cars_List.Cars_List(None)
            lista_cars.añadir_vehiculo(lista_vuelos, "Valencia", 15, "Seat Ibiza", "2321", "Valencia", 3)    
            rental_reply = lista_cars.confirmar_reserva(usuario, MockRental)
            assert rental_reply == True, "The payment is accepted when it should be denied"
            

if __name__ == "__main__":
    unittest.main()

        
