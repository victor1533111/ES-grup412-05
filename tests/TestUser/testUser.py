from ../.. import Flights
from ../.. import Users


class testUser:
    def test_gestiopassatgers(self):
        usuario = User("Ruben","4712458T","Calle Vic","645548572","rubenjibo@gmail.com")
        numero = 7
        assert numero == Flights.viajeros
        assert user == Flights.usuario