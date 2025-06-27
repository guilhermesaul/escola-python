class Animal:
    def __init__(self, nome:str, idade:int):
        self.__nome = nome
        self.__idade = idade
        
    @property
    def nome(self):
        return self.__nome
        
    @property
    def idade(self):
        return self.__idade
    
    @nome.setter
    def nome(self, novo):
        self.__nome = novo
    
    @idade.setter
    def idade(self, nova):
        self.__idade = nova
        
    def fazer_som(self):
        return "Som genérico de animal"
    
class Cachorro(Animal):
    def __init__(self, nome: str, idade: int, raca:str):
        super().__init__(nome, idade)
        self._raca = raca
        
    def fazer_som(self):
        return "Au Au!"
    
class Gato(Animal):
    def __init__(self, nome: str, idade: int, cor_pelo):
        super().__init__(nome, idade)
        self._cor_pelo = cor_pelo
        
    def fazer_som(self):
        return "Miau!"
    
a1 = Cachorro("Gui", 9, "Pastor alemão")
a2 = Gato("Bob", 4, "Branco com cinza")
animais_do_zoologico = [a1, a2]
for animal in animais_do_zoologico:
    nome = animal.nome
    idade = animal.idade
    som = animal.fazer_som()
    print(f"o nome dele é {nome}, ele tem {idade} anos e o som dele é {som}")