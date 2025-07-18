from abc import ABC, abstractmethod

class Criptografia(ABC):

    @abstractmethod
    def criptografar(self, palavra):
        pass

    @abstractmethod
    def descriptografar(self, palavra):
        pass
    
class AtBash(Criptografia):
    def __init__(self):
        self.__alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.__atbash =  self.__alfabeto[::-1] 
        
    def criptografar(self, palavra):
        cripto = ""
        for letra in palavra:
            # Retorna o indice numerico dentro do alfabeto
            i = self.__alfabeto.index(letra)
            #Letra equivalente na AtBash
            l = self.__atbash[i]
            cripto += l
        return cripto

    def descriptografar(self, palavra):
        descripto = ""
        for letra in palavra:
            i = self.__atbash.index(letra)
            l = self.__alfabeto[i]
            descripto += l
        return descripto
    
at = AtBash()
print(at.criptografar("ifrn"))
print(at.descriptografar("ruim"))