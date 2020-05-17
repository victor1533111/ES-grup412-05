class User:

    def __init__(self, name, DNI, direccion, telf, email):
        self.name = name
        self.DNI = DNI
        self.direccion = direccion
        self.telf = telf
        self.email = email
            
        pass

    def comprobar_datos(self):
        
        if type(self.name) != str:
            return False
            break
        if type(self.DNI) != str:
            return False
            break
        if type(direccion) != str:
            return False
            break
        if type(telf) != int:
            return False
            break
        if type(email) != str:
            return False
            break
        return True