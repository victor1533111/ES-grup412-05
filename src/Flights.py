from src.User import User
from src.Skyscanner import Skyscanner
class Flights:

    def CalcularPrecio(self):
        return self.precio_vuelos*self.viajeros*len(self.vuelos)

    def __init__(self, viajeros,user,origen='',destinos=[],precio_vuelos=0):
        
        if(viajeros<1):
            print("El numero de viajeros es incorrecto, debe ser superior a uno.")
        else:
            self.usuario = user
            self.viajeros=viajeros
            if(len(destinos)==0):
                self.destinos=[]
                self.vuelos=[]
                self.precio_total=0
                self.precio_vuelos=precio_vuelos
            else:
                self.destinos=destinos
                list(self.destinos)
                self.vuelos=[]
                self.vuelos.append([origen,self.destinos[0]])
                if len(destinos)!=1:                
                    i=0
                    for dest in self.destinos:
                        if dest != self.destinos[-1]:
                            self.vuelos.append([dest,self.destinos[i+1]])

                        i=i+1
                self.vuelos.append([self.destinos[-1],origen])
                self.precio_total=self.CalcularPrecio()
                


        pass
   


    def AñadirDestino(self,Ndestino,posicion):
        NuevosDestinos=[]
        i=1
        for dest in self.destinos:
            if i==posicion:
                NuevosDestinos.append(Ndestino)
            NuevosDestinos.append(dest)
            i=i+1
        self.destinos=NuevosDestinos
        
        
        NuevosVuelos=[]
        origen=self.vuelos[0][0]
        
        NuevosVuelos.append([origen,self.destinos[0]])
        
        if len(self.destinos)!=1:                
            i=0
            for dest in self.destinos:
                if dest != self.destinos[-1]:
                    NuevosVuelos.append([dest,self.destinos[i+1]])

                i=i+1
        
        NuevosVuelos.append([self.destinos[-1],origen])
        self.vuelos=NuevosVuelos
        
        self.precio_total=self.CalcularPrecio()


        pass


    def BorrarDestino(self,destinoB):
        

        NuevosDestinos=[]
        for dest in self.destinos:
            if dest!=destinoB:
                 NuevosDestinos.append(dest)          
            
        self.destinos=NuevosDestinos

        NuevosVuelos=[]

        origen=self.vuelos[0][0]
        
        NuevosVuelos.append([origen,self.destinos[0]])
        
        if len(self.destinos)!=1:                
            i=0
            for dest in self.destinos:
                if dest != self.destinos[-1]:
                    NuevosVuelos.append([dest,self.destinos[i+1]])

                i=i+1
        
        NuevosVuelos.append([self.destinos[-1],origen])
        self.vuelos=NuevosVuelos
        self.precio_total=self.CalcularPrecio()        


        pass

    def ConfirmarVuelos(self):
        confirmar =sky.Skyscanner.confirm_reserve(self,self.usuario,self)        
        return confirmar
        
        
        
