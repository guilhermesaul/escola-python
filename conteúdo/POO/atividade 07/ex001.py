from abc import ABC, abstractmethod

class Criptografia(ABC):
    def __init__(self, chave):
        super().__init__()
        self.chave = chave
        
    @abstractmethod
    def criptografar(self, palavra):
        pass

    @abstractmethod
    def descriptografar(self, palavra):
        pass
    
class Cesar(Criptografia):
    def __init__(self, chave):
        super().__init__(chave)
        self.__alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        
    def criptografar(self, palavra):
        palavras = []
        for letra in palavra:
            indice = self.__alfabeto.index(letra)
            indice = (indice+self.chave)%26
            palavras.append(self.__alfabeto[indice])
        return palavras
    
    def descriptografar(self, palavra):
        palavrass = []
        for letra in palavra:
            indice = self.__alfabeto.index(letra)
            indice = (indice-self.chave)%26
            palavrass.append(self.__alfabeto[indice])
        return palavrass
            
    
cu = Cesar(5)
mensagem = cu.criptografar("oibb")
invertida = cu.descriptografar(mensagem)
print(''.join(mensagem))
print(''.join(invertida))