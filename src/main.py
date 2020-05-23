import User 
import PaymentData
import Hotels
import Bank
def main():

    datoscorrectos = False
    print("Deseas realizar el pago de la reserva ? S/N")
    respuesta = input()
    while datoscorrectos == False:
        if respuesta == "S":
            print("Proporcioname los siguientes datos:")
            print("Nombre Completo:")
            Nombre = input()
            DNI = input("DNI:")
            direccion = input("Direccion")
            telefono = input("Telefono")
            email = input("Email")
            usuario = User(Nombre,DNI,direccion,telefono,email)

        print("Deseas continuar ? S/N")
        continuar = input()
        if continuar == 'S':
            datoscorrectos= usuario.comprobar_datos()
            if datoscorrectos == False:
                print("Los datos de facturacion introducidos son incorrectos o incompletos.")
    
    validar_datos_tarjeta=True
    while validar_datos_tarjeta ==False:
        print("Selecciona el metodo de pago de entre los siguiente:")
        print("VISA")
        print("MasterCard")
        metodo_pago = input()
        print("Deseas continuar ? S/N")
        continuar = input()
        if continuar == 'S':
            print("Proporcioname los siguientes datos:")
            titular = input("Titular de la tarjeta.")
            num_tarjeta = input("Numero de la tarjeta de credito.")
            codigo_seguridad = input("Codigo de seguridad de la tarjeta de credito.")
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

