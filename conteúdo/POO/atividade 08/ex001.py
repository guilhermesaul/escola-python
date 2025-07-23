class Carro:
    def __init__(self, modelo, cor, fabricante, potencia, torque, cambio):
        self.__modelo = modelo
        self.__cor = cor
        self.__fabricante = fabricante
        self.__potencia = potencia
        self.__torque = torque
        self.__cambio = cambio
        
    @property 
    def modelo(self):
        return self.__modelo
    
    @property 
    def cor(self):
        return self.__cor
    
    @property 
    def fabricante(self):
        return self.__fabricante
    
    @property 
    def potencia(self):
        return self.__potencia
    
    @property 
    def torque(self):
        return self.__torque
    
    @property 
    def cambio(self):
        return self.__cambio
    
    @modelo.setter
    def modelo(self, novo):
        self.__modelo = novo
    
    @cor.setter
    def cor(self, novo):
        self.__cor = novo
    
    @fabricante.setter
    def fabricante(self, novo):
        self.__fabricante = novo
    
    @potencia.setter
    def potencia(self, novo):
        self.__potencia = novo
    
    @torque.setter
    def torque(self, novo):
        self.__torque = novo
    
    @cambio.setter
    def cambio(self, novo):
        self.__cambio = novo