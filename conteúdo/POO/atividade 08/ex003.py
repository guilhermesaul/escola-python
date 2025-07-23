class ContaCorrente:
    def __init__(self, nome, numero, agencia, saldo, data):
        self.__nome = nome
        self.__numero = numero
        self.__agencia = agencia
        self.__saldo = saldo
        self.__data = data
        
    @property
    def nome(self):
        return self.__nome
        
    @property
    def numero(self):
        return self.__numero
        
    @property
    def agencia(self):
        return self.__agencia
        
    @property
    def saldo(self):
        return self.__saldo
        
    @property
    def data(self):
        return self.__data
    
    @nome.setter
    def nome(self, novo):
        self.__nome = novo
    
    @numero.setter
    def numero(self, novo):
        self.__numero = novo
    
    @agencia.setter
    def agencia(self, novo):
        self.__agencia = novo
    
    @saldo.setter
    def saldo(self, novo):
        self.__saldo = novo
    
    @data.setter
    def data(self, novo):
        self.__data = novo
        
    def saca(self, valor_saque):
        self.__saldo -= valor_saque
        
    def deposita(self, valor_deposito):
        self.__saldo += valor_deposito
        
class Nubank(ContaCorrente):
    def __init__(self, nome, numero, agencia, saldo, data):
        super().__init__(nome, numero, agencia, saldo, data)
        self.__taxa_cdi_anual = 6,4/100
        
    @property
    def taxa_cdi_anual(self):
        return self.__taxa_cdi_anual
    
    @taxa_cdi_anual.setter
    def nome(self, novo):
        self.__taxa_cdi_anual = novo
        
    def render(self, dias = 1):
        self.__taxa_cdi_anual = self.__taxa_cdi_anual/252 # 252 dias uteis
        for i in range(dias+1):
            self.__saldo *= self.__taxa_cdi_anual
            