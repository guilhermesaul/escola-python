class Lutador:
    def __init__(self, nome, vida):
        self.__nome = nome
        self.__vida = vida
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        
    @property
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self, vida):
        self.__vida = vida
        
    def golpe(self):
        return "Sem golpe"
        
    def atacar(self):
        return 10
    
    def golpe_especial(self):
        return 0
    
class Ryu(Lutador):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.__golpe = "Hadouken"
        
    @property
    def golpe(self):
        return self.__golpe
    
    def golpe_especial(self):
        return 30
    
class ChunLi(Lutador):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.__golpe = "Lt Kick"
        
    @property
    def golpe(self):
        return self.__golpe
    
    def golpe_especial(self):
        return 35
    
lutadores = [Ryu("Ryu", 100), ChunLi("Chun Li", 95)]
for lutador in lutadores:
    nome = lutador.nome
    golpe = lutador.golpe
    dano = lutador.golpe_especial
r = Ryu("Ryu", 100)
print(r.golpe, r.golpe_especial())  # Hadouken 30
