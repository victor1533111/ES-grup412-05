import User
class Flights:

    def __init__(self, viajeros,user,origen,destinos,precio_vuelos):
        
        if(viajeros<1):
            print("El numero de viajeros es incorrecto, debe ser superior a uno.")
        else:
            self.usuario = user
            self.viajeros=viajeros
            if(len(destinos)==0):
                self.destinos=[]
                self.vuelos=[]
                self.precio_total=0
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
                self.precio_vuelos=[]
                self.precio_vuelos.append(precio_vuelo)
                for pre in precio_vuelos:
                    self.precio_total+=pre
                self.precio_total=self.precio_total*viajeros


        pass


    def AñadirDestino(self,Ndestino,posicion, precio_destino):
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
        
        new_precio=precio_destino
        old_precios=self.precio_vuelos
        old_precios.append(new_precio)
        for i in old_precios:
            self.precio_total+=i
        self.precio_vuelos=old_precios
        self.precio_total=self.precio_total*self.viajeros


        pass


    def BorrarDestino(self,destinoB):
        #lo hago al inicio pa poder usar self.destinos original
        old_precios=self.precios_vuelos
        new_precios=[]
        for l,x in enumerate(self.destinos):
            if x != destinoB:
                new_precios.append(old_precios[l])
            else:
                self.precio_vuelos=self.precio_vuelos-(old_precios[l]*self.viajeros)
        self.precios_vuelos=new_precios


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
        
        


        pass