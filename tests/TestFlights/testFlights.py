import unittest
from unittest import mock
import sys
sys.path.append('../../src/')
import Flights
import User

class testFlights(unittest.TestCase):

    def test_gestiopassatgers(self):
        self.usuario = User.User("Ruben", "4712458T", "Calle Vic",
                            "645548572", "rubenjibo@gmail.com")
        numviajeros = 5
        self.vuelo = Flights.Flights(numviajeros, self.usuario,
                             "Valencia", ["Barcelona"], 200)

        assert numviajeros == self.vuelo.viajeros
        assert self.usuario == self.vuelo.usuario

    def test_listavacia(self):
        self.usuario = User.User("Ruben", "4712458T", "Calle Vic",
                            "645548572", "rubenjibo@gmail.com")
        numviajeros = 1
        self.viaje = Flights.Flights(numviajeros,self.usuario)
        assert self.viaje.vuelos==[]

    def test_precio0(self):
        self.usuario = User.User("Ruben", "4712458T", "Calle Vic",
                            "645548572", "rubenjibo@gmail.com")
        numviajeros = 1
        self.viaje = Flights.Flights(numviajeros,self.usuario)
        assert self.viaje.vuelos==0

    def test_precio_actualizado(self):
        self.usuario = User.User("Ruben", "4712458T", "Calle Vic",
                            "645548572", "rubenjibo@gmail.com")
        numviajeros = 2
        self.viaje = Flights.Flights(numviajeros,self.usuario,origen='BCN',destinos=['BER','VEN','ENG'],precio_vuelos=2000)
        self.viaje.AñadirDestino('AZJ',4)
        assert self.viaje.precio_total == numviajeros*2000*4

    def test_confirmarvuelos(self):
        self.usuario = User.User("Ruben", "4712458T", "Calle Vic","645548572", "rubenjibo@gmail.com")
        numviajeros = 5
        vuelo = Flights.Flights(numviajeros, self.usuario,"Valencia", "Barcelona", 200)
        
        self.assertTrue(vuelo.ConfirmarVuelos(), "Reserva hecha")


    ''' Dado un viaje con múltiples destinos y más de un viajero, cuando se quitan
        destinos, la lista de vuelos/destinos es la esperada  '''
    def test_viajeMultiple_Vuelos_y_Vuelos(self):
        usuario = User.User("Ruben","4712458T","Calle Vic","645548572","rubenjibo@gmail.com")
        numviajeros=5
        vuelo = Flights.Flights(numviajeros,usuario,"Valencia","Barcelona")
        vuelo.AñadirDestino("Pamplona", 1)
        vuelo.BorrarDestino("Pamplona")
        expected = ["Valencia", "Barcelona"]
        self.assertListEqual(vuelo.vuelos, expected)
        self.assertListEqual(vuelo.destinos, expected)

        
    ''' Dado un viaje con múltiples destinos y más de un viajero, cuando se quitan
        destinos, la lista de vuelos/destinos es la esperada  '''
    def test_viajeMultiple_Precio(self):
        usuario= User.User("Ruben","4712458T","Calle Vic","645548572","rubenjibo@gmail.com")
        numviajeros=5
        vuelo = Flights.Flights(numviajeros,usuario,"Valencia","Barcelona",200)
        vuelo.AñadirDestino("Pamplona", 1)
        vuelo.BorrarDestino("Pamplona")
        expected = ["Valencia", "Barcelona"]
        self.precio_Esperado = 400
        assert self.precioEsperado == vuelo.precio_total
    
    def test_AnadirDestino(self):
        usuario = User.User("Ruben","4712458T","Calle Vic","645548572","rubenjibo@gmail.com")
        destinos = ["Valencia","Madrid"]
        vuelos = Flights.Flights(5,usuario,"Barcelona",destinos,200)
        vuelos.AñadirDestino("Amsterdam",2)
        DestinosEsperados=["Valencia","Amsterdam","Madrid"]
        VuelosEsperados=[["Barcelona","Valencia"],["Valencia","Amsterdam"],["Amsterdam","Madrid"],["Madrid","Barcelona"]]
        precioEsperado=4000
        assert precioEsperado == vuelos.precio_total
        assert DestinosEsperados == vuelos.destinos
        assert VuelosEsperados == vuelos.vuelos

    def test_BorrarDestino(self):
        usuario= User("Ruben","4712458T","Calle Vic","645548572","rubenjibo@gmail.com")
        destinos=["Valencia","Amsterdam","Madrid"]
        vuelos = Flights.Flights(5,usuario,"Barcelona",destinos,200)
        vuelos.BorrarDestino("Amsterdam")
        DestinosEsperados=["Valencia","Madrid"]
        VuelosEsperados=[["Barcelona","Valencia"],["Valencia","Madrid"],["Madrid","Barcelona"]]
        precioEsperado=3000
        assert precioEsperado == vuelos.precio_total
        assert DestinosEsperados == vuelos.destinos
        assert VuelosEsperados == vuelos.vuelos


if __name__ == "__main__":
    unittest.main()

        
