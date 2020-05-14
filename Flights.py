class Flights:

    def __init__(self, viajeros,origen,destinos):
        if(viajeros>0):
            self.viajeros=viajeros
        else:
            print("El numero de viajeros es incorrecto, debe ser superior a uno.")
        if(len(destinos)==0):
            self.destinos=[]
            self.vuelos=[]
            self.precio=0
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

            print("Falta actualizar precio")

        pass


    def AñadirDestino(self,Ndestino,posicion):
        NuevosDestinos=[]
        i=0
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
        print("Falta actualizar precio")

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
        print("Falta actualizar precio")

        pass