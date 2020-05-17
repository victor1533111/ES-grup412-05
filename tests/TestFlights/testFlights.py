
from src.Flights import Flights
from src.User import User
import unittest

class testFlights(unittest.TestCase):

    def test_gestiopassatgers(self):
        self.usuario = User("Ruben", "4712458T", "Calle Vic",
                            "645548572", "rubenjibo@gmail.com")
        numviajeros = 5
        self.vuelo = Flights(numviajeros, self.usuario,
                             "Valencia", ["Barcelona"], 200)

        assert numviajeros == self.vuelo.viajeros
        assert self.usuario == self.vuelo.usuario

    def test_listavacia(self):
        self.usuario = User("Ruben", "4712458T", "Calle Vic",
                            "645548572", "rubenjibo@gmail.com")
        numviajeros = 1
        self.viaje = Flights(numviajeros,self.usuario)
        assert self.viaje.vuelos==[]

    def test_precio0(self):
        self.usuario = User("Ruben", "4712458T", "Calle Vic",
                            "645548572", "rubenjibo@gmail.com")
        numviajeros = 1
        self.viaje = Flights(numviajeros,self.usuario)
        assert self.viaje.vuelos==0

    def test_precio_actualizado(self):
        self.usuario = User("Ruben", "4712458T", "Calle Vic",
                            "645548572", "rubenjibo@gmail.com")
        numviajeros = 2
        self.viaje = Flights(numviajeros,self.usuario,origen='BCN',destinos=['BER','VEN','ENG'],precio_vuelos=2000)
        self.viaje.AñadirDestino('AZJ',4)
        assert self.viaje.precio_total == numviajeros*2000*4

    def test_confirmarvuelos(self):
        self.usuario = User("Ruben", "4712458T", "Calle Vic","645548572", "rubenjibo@gmail.com")
        numviajeros = 5
        vuelo = Flights(numviajeros, self.usuario,"Valencia", "Barcelona", 200)
        
        self.assertTrue(vuelo.ConfirmarVuelos(), "Reserva hecha")


    ''' Dado un viaje con múltiples destinos y más de un viajero, cuando se quitan
        destinos, la lista de vuelos/destinos es la esperada  '''
    def test_viajeMultiple_Vuelos_y_Vuelos(self):
        usuario= User("Ruben","4712458T","Calle Vic","645548572","rubenjibo@gmail.com")
        numviajeros=5
        vuelo = Flights(numviajeros,usuario,"Valencia","Barcelona",200)
        vuelo.AñadirDestino("Pamplona", 1)
        vuelo.BorrarDestino("Pamplona")
        expected = ["Valencia", "Barcelona"]
        self.assertListEqual(vuelo.vuelos, expected)
        self.assertListEqual(vuelo.destinos, expected)

    
    def test_AnadirDestino(self):
            usuario= User("Ruben","4712458T","Calle Vic","645548572","rubenjibo@gmail.com")
            destinos=["Valencia","Madrid"]
            vuelos = Flights(5,usuario,"Barcelona",destinos,200)
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
            vuelos = Flights(5,usuario,"Barcelona",destinos,200)
            vuelos.BorrarDestino("Amsterdam")
            DestinosEsperados=["Valencia","Madrid"]
            VuelosEsperados=[["Barcelona","Valencia"],["Valencia","Madrid"],["Madrid","Barcelona"]]
            precioEsperado=3000
            assert precioEsperado == vuelos.precio_total
            assert DestinosEsperados == vuelos.destinos
            assert VuelosEsperados == vuelos.vuelos
    

if __name__ == "__main__":
    unittest.main()

        
