from src.Flights import Flights
from src.User import User

class testFlights():

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
        self.vuelo = Flights(numviajeros, self.usuario,"Valencia", "Barcelona", 200)
        
        assertTrue(ConfirmarVuelos(), "Reserva hecha")