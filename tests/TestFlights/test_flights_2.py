class testUser():

    def test_gestiopassatgers(self):
        self.usuario= User("Ruben","4712458T","Calle Vic","645548572","rubenjibo@gmail.com")
        numeroviajeros=5
        destinos=["Valencia","Madrid"]
        self.vuelo = Flights(numeroviajeros,self.usuario,destinos,"Barcelona",200)

        assert numeroviajeros == self.vuelo.viajeros
        assert self.usuario == self.vuelo.usuario
    
    def test_AñadirDestino(self):
            usuario= User("Ruben","4712458T","Calle Vic","645548572","rubenjibo@gmail.com")
            destinos=["Valencia","Madrid"]
            Flights(5,usuario,"Barcelona",destinos,200)
            Flights.AñadirDestino("Amsterdam",2,10)
            DestinosEsperados=["Valencia","Amsterdam","Madrid"]
            VuelosEsperados=[["Barcelona","Valencia"],["Valencia","Amsterdam"],["Amsterdam","Madrid"],["Madrid","Barcelona"]]
            precioEsperado=3000
            assert precioEsperado == Flights.precio_total
            assert DestinosEsperados == Flights.destinos
            assert VuelosEsperados == Flights.vuelos