import unittest
from unittest import mock
import sys
sys.path.append('../../src/')
import Flights
import User
import Flights_list
import Cars_List
import Cars

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
          precio_por_dia=20
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
          
      '''Dado un viaje con múltiples destinos y más de un viajero, cuando se confirma
      correctamente la reserva de los vehículos, se reporta que la acción se ha
      realizado correctamente'''

      def test_reserva_vehiculos(self):
             with mock.patch('Rentalcars.Rentalcars') as MockRental:
            MockRental.confirm_reserve.return_value = True
            usuario = User.User("Ruben", "4712458T", "Calle Vic","645548572", "rubenjibo@gmail.com")
            rentalcars = Cars.Cars(123, "Seat", 20, "Calle Vic", "calle Valencia", 3)
            rental_reply = rentalcars.confirmar_reserva_vehiculos_conerrores(usuario,rentalcars)
            
            assert rental_reply == True
                
          
if __name__ == "__main__":
    unittest.main()

        
