import unittest
from unittest import mock
import sys
sys.path.append('../../src/')
import Flights
import Flights_list
import User
import Skyscanner

class testFlights(unittest.TestCase):

    def test_gestiopassatgers(self):
        usuario = User.User("Ruben", "4712458T", "Calle Vic", "645548572", "rubenjibo@gmail.com")
        numviajeros = 5
        vuelo = []
        vuelo.append(Flights.Flights("1234", "Barcelona", "Valencia", numviajeros, 20))
        lista_vuelos = Flights_list.Flights_list(vuelo, usuario)
        assert numviajeros == vuelo[0].num_passatgers
        assert usuario == lista_vuelos.usuario

    def test_lista_destinos_vacia(self):
        usuario = User.User("Ruben", "4712458T", "Calle Vic", "645548572", "rubenjibo@gmail.com")
        numviajeros = 1
        vuelo = []
        vuelo.append(Flights.Flights("1234", "Barcelona", None, numviajeros, 20))
        lista_vuelos = Flights_list.Flights_list(vuelo, usuario)
        assert vuelo[0].destinacio == None
    
    def test_lista_vuelos_vacia(self):
        usuario = User.User("Ruben", "4712458T", "Calle Vic", "645548572", "rubenjibo@gmail.com")
        numviajeros = 1
        vuelo = []
        vuelo.append(Flights.Flights("1234", "Barcelona", None, numviajeros, 20))
        lista_vuelos = Flights_list.Flights_list(vuelo, usuario)
        assert lista_vuelos.listVuelos == []

    def test_precio0(self):
        usuario = User.User("Ruben", "4712458T", "Calle Vic", "645548572", "rubenjibo@gmail.com")
        numviajeros = 1
        lista_vuelos = Flights_list.Flights_list(None, usuario)
        lista_vuelos.AñadirDestino("1234", "Barcelona", "Valencia", numviajeros, 0, 1)
        assert lista_vuelos.listVuelos[0].precio_vuelo == 0

    def test_precio_actualizado(self):
        usuario = User.User("Ruben", "4712458T", "Calle Vic", "645548572", "rubenjibo@gmail.com")
        numviajeros = 1
        lista_vuelos = Flights_list.Flights_list(None, usuario)
        lista_vuelos.AñadirDestino("1234", "Barcelona", "Valencia", numviajeros, 20, 0)
        lista_vuelos.AñadirDestino("3214", "Valencia", "Madrid", numviajeros, 50, 1)
        assert lista_vuelos.calcular_precioTotal() == 70

    def test_confirmarvuelos(self):
        usuario = User.User("Ruben", "4712458T", "Calle Vic","645548572", "rubenjibo@gmail.com")
        numviajeros = 5
        lista_vuelos = Flights_list.Flights_list(None, usuario)
        lista_vuelos.AñadirDestino("1234", "Barcelona", "Valencia", numviajeros, 20, 0)
        lista_vuelos.AñadirDestino("3214", "Valencia", "Madrid", numviajeros, 50, 1)
        sky = Skyscanner.Skyscanner()
        self.assertTrue(lista_vuelos.Confirmar_todos(sky), "Reserva hecha")


    ''' Dado un viaje con múltiples destinos y más de un viajero, cuando se quitan
        destinos, la lista de vuelos/destinos es la esperada  '''
    def test_viajeMultiple_Vuelos_y_Destinos(self):
        usuario = User.User("Ruben", "4712458T", "Calle Vic","645548572", "rubenjibo@gmail.com")
        numviajeros = 5
        lista_vuelos = Flights_list.Flights_list(None, usuario)
        lista_vuelos.AñadirDestino("3214", "Valencia", "Madrid", numviajeros, 50, 0)    
        lista_vuelos.AñadirDestino("2323", "Madrid", "Sevilla", numviajeros, 50, 1) 
        lista_vuelos.AñadirDestino("4522", "Sevilla", "Bilbao", numviajeros, 50, 2) 
        lista_vuelos.BorrarDestino(0)
        assert len(lista_vuelos.listVuelos) == 2
        self.assertListEqual(lista_vuelos.getListaDestinos(), ["Sevilla", "Bilbao"])
    
    ''' Dado un viaje con múltiples destinos y más de un viajero, cuando se quitan
        destinos, la lista de vuelos/destinos es la esperada  '''
    def test_viajeMultiple_Precio(self):
        usuario = User.User("Ruben", "4712458T", "Calle Vic","645548572", "rubenjibo@gmail.com")
        numviajeros = 5
        lista_vuelos = Flights_list.Flights_list(None, usuario)
        lista_vuelos.AñadirDestino("3214", "Valencia", "Madrid", numviajeros, 50, 0)    
        lista_vuelos.AñadirDestino("2323", "Madrid", "Sevilla", numviajeros, 50, 1) 
        lista_vuelos.AñadirDestino("4522", "Sevilla", "Bilbao", numviajeros, 50, 2) 
        lista_vuelos.BorrarDestino(0)
        assert lista_vuelos.calcular_precioTotal() == 500 
    
    def test_AnadirDestino(self):
        usuario = User.User("Ruben", "4712458T", "Calle Vic","645548572", "rubenjibo@gmail.com")
        numviajeros = 5
        lista_vuelos = Flights_list.Flights_list(None, usuario)
        lista_vuelos.AñadirDestino("3214", "Valencia", "Madrid", numviajeros, 50, 0)    
        lista_vuelos.AñadirDestino("2323", "Madrid", "Amsterdam", numviajeros, 50, 1) 
        lista_vuelos.AñadirDestino("4522", "Amsterdam", "Valencia", numviajeros, 50, 2) 
        assert len(lista_vuelos.listVuelos) == 3
        assert lista_vuelos.getListaDestinos() == ["Madrid", "Amsterdam", "Valencia"]
        assert lista_vuelos.calcular_precioTotal() == 750 

    def test_BorrarDestino(self):
        usuario = User.User("Ruben", "4712458T", "Calle Vic","645548572", "rubenjibo@gmail.com")
        numviajeros = 5
        lista_vuelos = Flights_list.Flights_list(None, usuario)
        lista_vuelos.AñadirDestino("3214", "Valencia", "Madrid", numviajeros, 50, 0)    
        lista_vuelos.AñadirDestino("2323", "Madrid", "Amsterdam", numviajeros, 50, 1) 
        lista_vuelos.AñadirDestino("4522", "Amsterdam", "Valencia", numviajeros, 50, 2) 
        lista_vuelos.BorrarDestino(1)
        lista_vuelos.BorrarDestino(1)
        assert len(lista_vuelos.listVuelos) == 1
        assert lista_vuelos.getListaDestinos() == ["Madrid"]
        assert lista_vuelos.calcular_precioTotal() == 250 

    def test_gestionar_reserva(self):
        with mock.patch('Skyscanner.Skyscanner') as MockSky:
            MockSky.confirm_reserve.return_value = False
            usuario = User.User("Pepe", "2051923A", "C/ Bolets", "93333333", "jibo@gmail.com")
            lista_vuelos = Flights_list.Flights_list(None, usuario)
            lista_vuelos.AñadirDestino("3214", "Valencia", "Madrid", 5, 50, 0)  
            reply = lista_vuelos.Confirmar_todos(MockSky)
            assert reply == False, "The payment is accepted when it should be denied"

if __name__ == "__main__":
    unittest.main()

        
