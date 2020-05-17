from src.User import User 
from src.PaymentData import PaymentData
from src.Hotels import Hotels
def main():

    respuesta = input("Deseas realizar el pago de la reserva ? S/N")
    if respuesta == "S":
        print("Proporcioname los siguientes datos:")
        Nombre = input("Nombre Completo")
        DNI = input("DNI")
        direccion = input("Direccion")
        telefono = input("Telefono")
        email = input("Email")
        usuario = User(Nombre,DNI,direccion,telefono,email)

        datoscorrectos= usuario.comprobar_datos()

        if datoscorrectos == False:
            print("Los datos introducidos son incorrectos")
            print("Proporcioname los siguientes datos:")
            titular = input("Titular de la tarjeta")
            tarjeta = input("Numero de la tarjeta de credito")
            codigo_seguridad = input("Codigo de seguridad de la tarjeta de credito")
            



if __name__== "__main__":
    main()
