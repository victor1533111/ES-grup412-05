import User
import PaymentData
def main():

    viaje= User.Trip(num_pass=2, origen='BCN', flight_list=[('BCN','BER'),('BER','VEN'),('VEN','BCN')],car_list=['Buggati Veyron','Lamborghini Aventador'],fecha_in='10/06/2021',fecha_f='30/06/2021',precio=3500)


    #flujo principal
    print('El usuario pulsa el boton de "Realizar pago"')
    corr==False
    while(corr==False):
        print("El usuario introduce sus datos para el pago")
        user = User.user(nom="pepe",DNI="39887788V", direccion="calle juan carlos I", tel="673666888",email="pepeilosglobos@gmail.com")
        payment = PaymentData.payment(titular="Pepe", num_tarjeta="2313353", cvc="321", method="VISA")
        
        
        if(corr):
            corr=True
        else:
            print("datos incorrectos vuelve a rellenar")


    print("validamos datos")
    if(PaymentData.payment.validar_datos(payment) != True):
        print("datos incorrectos vuelve a rellenar")

if __name__== "__main__":
    main()
