from src.Flights import Flights
from src.User import User
import unittest

class testFlights(unittest.TestCase):

    def test_gestiopassatgers(self):
        self.usuario = User("Ruben", "4712458T", "Calle Vic",
                            "645548572", "rubenjibo@gmail.com")
        numviajeros = 5
        self.vuelo = Flights(numviajeros, self.usuario,
                             "Valencia", "Barcelona", 200)

        assert numviajeros == self.vuelo.viajeros
        assert self.usuario == self.vuelo.usuario

    def test_listavacia(self):
        self.usuario = User("Ruben", "4712458T", "Calle Vic",
                            "645548572", "rubenjibo@gmail.com")
        numviajeros = 1
        self.viaje = Flights(numviajeros,self.usuario)
        assert self.viaje.vuelos==[]

    def test_confirmarvuelos(self):
        self.usuario = User("Ruben", "4712458T", "Calle Vic","645548572", "rubenjibo@gmail.com")
        numviajeros = 5
        vuelo = Flights(numviajeros, self.usuario,"Valencia", "Barcelona", 200)
        
        self.assertTrue(vuelo.ConfirmarVuelos(), "Reserva hecha")

    ''' Dado un viaje con múltiples destinos y más de un viajero, cuando se quitan
        destinos, la lista de destinos es la esperada '''
    def test_viajeMultiple_Destinos(self):
        usuario= User("Ruben","4712458T","Calle Vic","645548572","rubenjibo@gmail.com")
        numviajeros=5
        vuelo = Flights(numviajeros,usuario,"Valencia","Barcelona",200)
        vuelo.AñadirDestino("Pamplona", 1)
        vuelo.BorrarDestino("Pamplona")
        expected = ["Valencia", "Barcelona"]
        self.assertListEqual(vuelo.destinos, expected)

    ''' Dado un viaje con múltiples destinos y más de un viajero, cuando se quitan
        destinos, la lista de vuelos/destinos es la esperada  '''
    def test_viajeMultiple_Vuelos(self):
        usuario= User("Ruben","4712458T","Calle Vic","645548572","rubenjibo@gmail.com")
        numviajeros=5
        vuelo = Flights(numviajeros,usuario,"Valencia","Barcelona",200)
        vuelo.AñadirDestino("Pamplona", 1)
        vuelo.BorrarDestino("Pamplona")
        expected = ["Valencia", "Barcelona"]
        self.assertListEqual(vuelo.vuelos, expected)
        self.assertListEqual(vuelo.destinos, expected)

    

if __name__ == "__main__":
    unittest.main()

        
