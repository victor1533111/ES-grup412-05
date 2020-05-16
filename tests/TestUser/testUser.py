from ../.. import Flights
from ../.. import Users



def test_gestiopassatgers(numero, user):
    if numero == Flights.viajeros:
        return True
    if Flights.usuario == user:
        return True