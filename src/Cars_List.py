import Cars

class Cars_List:

    def __init__(self, listcars: Cars):
        self.listcars = listcars
        pass

    def calcular_precioTotal(self):
        precio_T = 0
        for car in self.listcars:
            precio_T += car.precio_Total
        return precio_T