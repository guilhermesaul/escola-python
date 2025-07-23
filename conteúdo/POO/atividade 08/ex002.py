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
        
p1 = ContaCorrente("gui", 12345678, 1, 1000, "23/07/2025")
print(p1.saldo)
p1.saca(100)
print(p1.saldo)
p1.deposita(200)
print(p1.saldo)
