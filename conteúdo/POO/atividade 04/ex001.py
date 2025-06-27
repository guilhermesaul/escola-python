class Personagem:
    def __init__(self, nome, idade, sexo, ataque, defesa, vida):
        self.__nome = nome
        self.__idade = idade
        self.__sexo = sexo
        self.__ataque = ataque
        self.__defesa = defesa
        self.__vida = vida

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @property
    def sexo(self):
        return self.__sexo
    
    @property
    def ataque(self):
        return self.__ataque

    @property
    def defesa(self):
        return self.__defesa

    @property
    def vida(self):
        return self.__vida

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @idade.setter
    def idade(self, nova_idade):
        self.__idade = nova_idade
        
    @sexo.setter
    def sexo(self, novo_sexo):
        self.__sexo = novo_sexo
        
    @ataque.setter
    def ataque(self, novo_ataque):
        self.__ataque = novo_ataque
        
    @defesa.setter
    def defesa(self, nova_defesa):
        self.__defesa = nova_defesa
        
    @vida.setter
    def vida(self, nova_vida):
        self.__vida = nova_vida
        
    def bloquear_golpe(self):
        self.__defesa *= 2
        
    def golpe_especial(self):
        self.__ataque *= 3
        
class KazuyaMishima(Personagem):
    def __init__(self, nome, idade, sexo, ataque, defesa, vida):
        super().__init__(nome, idade, sexo, ataque, defesa, vida)
        
    def bloquear_golpe(self):
        super().bloquear_golpe()
        self.ataque *= 2
        return self.ataque
    
    def golpe_especial(self):
        super().golpe_especial()
        
class King(Personagem):
    def __init__(self, nome, idade, sexo, ataque, defesa, vida):
        super().__init__(nome, idade, sexo, ataque, defesa, vida)
        
    def bloquear_golpe(self):
        self.defesa *= 3
    
    def golpe_especial(self):
        self.ataque *= 2
        
class NinaWilliams(Personagem):
    def __init__(self, nome, idade, sexo, ataque, defesa, vida):
        super().__init__(nome, idade, sexo, ataque, defesa, vida)
        
    def bloquear_golpe(self):
        super().bloquear_golpe()
        self.ataque *= 2
        return self.ataque
    
    def golpe_especial(self):
        self.ataque *= 2
        
class PaulPhoenix(Personagem):
    def __init__(self, nome, idade, sexo, ataque, defesa, vida):
        super().__init__(nome, idade, sexo, ataque, defesa, vida)
        
    def bloquear_golpe(self):
        super().bloquear_golpe()
    
    def golpe_especial(self):
        self.ataque *= 2
          
class MichelleChang(Personagem):
    def __init__(self, nome, idade, sexo, ataque, defesa, vida):
        super().__init__(nome, idade, sexo, ataque, defesa, vida)
        
    def bloquear_golpe(self):
        self.defesa *= 3
        self.vida += 10
    
    def golpe_especial(self):
        self.ataque *= 5
        self.vida -= 5
          
class Law(Personagem):
    def __init__(self, nome, idade, sexo, ataque, defesa, vida):
        super().__init__(nome, idade, sexo, ataque, defesa, vida)
        
    def bloquear_golpe(self):
        self.vida += 20
    
    def golpe_especial(self):
        self.ataque *= 2
          
class Yoshimitsu(Personagem):
    def __init__(self, nome, idade, sexo, ataque, defesa, vida):
        super().__init__(nome, idade, sexo, ataque, defesa, vida)
        
    def bloquear_golpe(self):
        self.defesa *= 3
    
    def golpe_especial(self):
        self.ataque *= 2
          
class Jack(Personagem):
    def __init__(self, nome, idade, sexo, ataque, defesa, vida):
        super().__init__(nome, idade, sexo, ataque, defesa, vida)
        
    def bloquear_golpe(self):
        super().bloquear_golpe()
        return self.ataque
    
    def golpe_especial(self):
        self.ataque *= 4