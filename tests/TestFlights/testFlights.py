from src.Flights import Flights
from src.User import User



class testUser():

    def test_gestiopassatgers(self):
        self.usuario= User("Ruben","4712458T","Calle Vic","645548572","rubenjibo@gmail.com")
        numviajeros=5
        self.vuelo = Flights(numviajeros,self.usuario,"Valencia","Barcelona",200)

        assert numviajeros == self.vuelo.viajeros
        assert self.usuario == self.vuelo.usuario
        