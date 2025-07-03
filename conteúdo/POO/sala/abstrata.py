from abc import ABC, abstractmethod

class Lutador(ABC):
    def __init__(self, nome, vida):
        super().__init__()
        self.__nome = nome
        self.__vida = vida
        
    @abstractmethod
    def atacar(self):
        pass
    
    @abstractmethod
    def defender(self):
        pass
    
    @abstractmethod
    def especial(self):
        pass
    
class Kyo(Lutador):
    def atacar(self):
        return "Kyo Atacando"
    
    def defender(self):
        return "Kyo defendendo"
    
    def especial(self):
        return "Kyo ataque especial"
    
class Iori(Lutador):
    def atacar(self):
        return "Iori Atacando"
    
    def defender(self):
        return "Iori defendendo"
    
    def especial(self):
        return "Iori ataque especial"
    
kyo = Kyo("Kyo", 100)
iori = Iori("Iori", 100)
print(kyo.atacar())
print(kyo.especial())
print(iori.atacar())
print(iori.especial())