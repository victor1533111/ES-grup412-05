from src.Flights import Flights
from src.User import User



class testUser():

    def test_gestiopassatgers(self):
        self.usuario= User("Ruben","4712458T","Calle Vic","645548572","rubenjibo@gmail.com")
        numeroviajeros=5
        self.vuelo = Flights(numeroviajeros,self.usuario,"Valencia","Barcelona",200)

        assert numeroviajeros == self.vuelo.viajeros
        assert self.usuario == self.vuelo.usuario
        