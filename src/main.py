import User 
import PaymentData
import Hotels
import Bank
import Cars
import Flights
import Flights_list
import Cars_List
import Hotels_list
def main():

    
    
    datoscorrectos = False
    print("Deseas realizar el pago de la reserva ? S/N")
    respuesta = "S"
    while datoscorrectos == False:
        if respuesta == "S":
            print("Proporcioname los siguientes datos:")
            print("Nombre Completo:")
            Nombre = "Daniel Gutierrez Batista"
            print("DNI:")
            DNI = "47124321W"
            print("Direccion:")
            direccion = "Calle Querol "
            print("Telefono:")
            telefono = "628548332"
            print("Email:")
            email = "dani.guiterrez@uab.cat"
            usuario = User.User(Nombre,DNI,direccion,telefono,email)

        print("Deseas continuar ? S/N")
        continuar = "S"
        if continuar == 'S':
            datoscorrectos= usuario.comprobar_datos()
            if datoscorrectos == False:
                print("Los datos de facturacion introducidos son incorrectos o incompletos.")
    
    numviajeros = 5
        
    # Añadir Vuelos
    
    lista_vuelos = Flights_list.Flights_list(None, usuario)
    lista_vuelos.AñadirDestino("1234", "Barcelona", "Valencia", numviajeros, 20, 0)
    lista_vuelos.AñadirDestino("3214", "Valencia", "Madrid", numviajeros, 50, 1)
    
    # Añadir Hoteles
    
    numhabitaciones = 3
    numdias = 3
    precioHabitacion = 15
    
    lista_hoteles = Hotels_list.Hotels_list(None)
    lista_hoteles.AñadirHotel("1000", "Cristian", numviajeros, numhabitaciones, numdias, precioHabitacion, 0)    
    lista_hoteles.AñadirHotel("2000", "Cristian", numviajeros, numhabitaciones, numdias, precioHabitacion, 1)
    
    # Añadir Coches
    
    lista_cars = Cars_List.Cars_List(None)
    lista_cars.añadir_vehiculo(lista_vuelos, "Valencia", 15, "Seat Ibiza", "2321", "Valencia", 3)    
    
    fecha_in = "03/2/2019"
    fecha_f = "09/2/2019"
    usuario.Trip(lista_vuelos, lista_hoteles, lista_cars, fecha_in, fecha_f)
    precio = usuario.calcularPrecioT()
    validar_datos_tarjeta=False
    
    while validar_datos_tarjeta ==False:
        print("Selecciona el metodo de pago de entre los siguiente:")
        print("VISA")
        print("MasterCard")
        metodo_pago = "VISA"
        print("Deseas continuar ? S/N")
        continuar = "S"
        if continuar == 'S':
            print("Proporcioname los siguientes datos:")
            print("Titular de la tarjeta:")
            titular = "Daniel Gutierrez Batista"
            print("Numero de la tarjeta de credito:")
            num_tarjeta = "4332 2555 6777 8989"
            print("Codigo de seguridad de la tarjeta de credit:.")
            codigo_seguridad = "323"
            datos_pago = PaymentData.PaymentData(titular,num_tarjeta,codigo_seguridad,metodo_pago,precio)
            validar_datos_tarjeta = datos_pago.validar_datos()
            if validar_datos_tarjeta == False:
                print("Los datos para realiazar el pago introducidos son incorrectos o incompletos.")
            else:
                banco = Bank.Bank()
                errores_pago=datos_pago.confirmar_Pago(usuario,banco)
                if errores_pago == False:
                    validar_datos_tarjeta = False
            
    
        
    
    


     

if __name__== "__main__":
    main()

