class User:

    def __init__(self, name, DNI, direccion, telf, email):
        self.name = name
        self.DNI = DNI
        self.direccion = direccion
        self.telf = telf
        self.email = email
        pass

    def Trip(self, numpass, origen, listavuelos, hotel_list, car_list, fecha_in, fecha_f, precio_tot):
        self.viajeros=numpass
        self.origen=origen
        self.lista_vuelos=listavuelos
        self.hotel_list=hotel_list
        self.car_list=car_list
        self.fecha_inicio=fecha_in
        self.fecha_final=fecha_f
        self.precio_total=precio_tot

        pass