import User 
import PaymentData
import Hotels
import Bank
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
            usuario = User(Nombre,DNI,direccion,telefono,email)

        print("Deseas continuar ? S/N")
        continuar = "S"
        if continuar == 'S':
            datoscorrectos= usuario.comprobar_datos()
            if datoscorrectos == False:
                print("Los datos de facturacion introducidos son incorrectos o incompletos.")
    
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
            datos_pago = PaymentData(titular,num_tarjeta,codigo_seguridad,metodo_pago,0)
            validar_datos_tarjeta = datos_pago.validar_datos()
            if validar_datos_tarjeta == False:
                print("Los datos para realiazar el pago introducidos son incorrectos o incompletos.")
            banco = Bank()
            errores_pago=datos_pago.Gestionar_Errores_Pago(usuario,banco)
            if errores_pago == False:
                print("No se ha podido realizar el pago.")
    
    


     

if __name__== "__main__":
    main()

