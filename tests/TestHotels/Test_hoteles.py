import unittest
from unittest import mock
import sys
sys.path.append('../../src/')
import Hotels
import Hotels_list
import Flights
import Flights_list
import User
import Booking

class testHotels(unittest.TestCase):
    '''Dado un viaje con más de un viajero, cuando se añaden alojamientos, el precio
        del viaje es el esperado'''
    def test_AñadirAlojamiento_precio(self):
        usuario = User.User("Ruben", "4712458T", "Calle Vic","645548572", "rubenjibo@gmail.com")
        numviajeros = 2
        numhabitaciones = 1
        numdias = 3
        
        precioVuelo = 50
        precioHabitacion = 15
        
        lista_vuelos = Flights_list.Flights_list(None, usuario)
        lista_vuelos.AñadirDestino("3214", "Valencia", "Madrid", numviajeros, precioVuelo, 0)    
        lista_vuelos.AñadirDestino("2323", "Madrid", "Sevilla", numviajeros, precioVuelo, 1)
        
        lista_hoteles = Hotels_list.Hotels_list(None)
        lista_hoteles.AñadirHotel("1000", "Cristian", numviajeros, numhabitaciones, numdias, precioHabitacion, 0)    
        lista_hoteles.AñadirHotel("2000", "Cristian", numviajeros, numhabitaciones, numdias, precioHabitacion, 1)
        
        precio_Vuelos = (precioVuelo * numviajeros) * len(lista_vuelos.listVuelos)
        precio_Hoteles = (precioHabitacion * numhabitaciones * numdias) * len(lista_hoteles.listHotels)
        
        assert (lista_vuelos.calcular_precioTotal() + lista_hoteles.calcular_precioTotal()) == (precio_Vuelos + precio_Hoteles)
    
    def test_BorrarAlojamiento_precio(self):
        usuario = User.User("Ruben", "4712458T", "Calle Vic","645548572", "rubenjibo@gmail.com")
        numviajeros = 2
        numhabitaciones = 1
        numdias = 3
        
        precioVuelo = 50
        precioHabitacion = 15
        
        lista_vuelos = Flights_list.Flights_list(None, usuario)
        lista_vuelos.AñadirDestino("3214", "Valencia", "Madrid", numviajeros, precioVuelo, 0)    
        lista_vuelos.AñadirDestino("2323", "Madrid", "Sevilla", numviajeros, precioVuelo, 1)
        
        lista_hoteles = Hotels_list.Hotels_list(None)
        lista_hoteles.AñadirHotel("1000", "Cristian", numviajeros, numhabitaciones, numdias, precioHabitacion, 0)    
        lista_hoteles.AñadirHotel("2000", "Cristian", numviajeros, numhabitaciones, numdias, precioHabitacion, 1)
        
        lista_hoteles.BorrarHotel(1)
        
        precio_Vuelos = (precioVuelo * numviajeros) * len(lista_vuelos.listVuelos)
        precio_Hoteles = (precioHabitacion * numhabitaciones * numdias) * len(lista_hoteles.listHotels)
        
        assert (lista_vuelos.calcular_precioTotal() + lista_hoteles.calcular_precioTotal()) == (precio_Vuelos + precio_Hoteles)
    

if __name__ == "__main__":
    unittest.main()
