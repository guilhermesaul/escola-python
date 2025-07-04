from abc import ABC, abstractmethod

class MetodoPagamento(ABC):
    def __init__(self, valor:float, status):
        super().__init__()
        self.__valor = valor
        self.status = status
        
    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, novo):
        self.__valor = novo
        
    @abstractmethod
    def processar_pagamento(self):
        pass
    
class CartaoCredito(MetodoPagamento):
    def __init__(self, valor: float, status, numero_cartao):
        super().__init__(valor, status)
        self.__numero_cartao = numero_cartao
        
    @property
    def numero_cartao(self):
        return self.__numero_cartao
    
    @numero_cartao.setter
    def numero_cartao(self, novo):
        self.__numero_cartao = novo
        
    def processar_pagamento(self):
        return "Pagamento com Cartão de Crédito processado com sucesso!"
        
    
class BoletoBancario(MetodoPagamento):
    def __init__(self, valor: float, status, codigo_barras):
        super().__init__(valor, status)
        self.__codigo_barras = codigo_barras
        
    @property
    def codigo_barras(self):
        return self.__codigo_barras
    
    @codigo_barras.setter
    def codigo_barras(self, novo):
        self.__codigo_barras = novo
        
    def processar_pagamento(self):
        return "Boleto bancário gerado. Aguardando pagamento."
    
class Pix(MetodoPagamento):
    def __init__(self, valor: float, status, chave_pix):
        super().__init__(valor, status)
        self.__chave_pix = chave_pix
        
    @property
    def chave_pix(self):
        return self.__chave_pix
    
    @chave_pix.setter
    def chave_pix(self, novo):
        self.__chave_pix = novo
        
    def processar_pagamento(self):
        return "Pagamento via Pix efetuado com sucesso!"
    
m1 = CartaoCredito(100.50, "Pendente", 12345678)
m2 = BoletoBancario(105, "Pendente", 87654321)
m3 = Pix(50, "Pendente", "exemplo@gmail.com")
transacoes_pendentes = [m1, m2, m3]
for transacao in transacoes_pendentes:
    transacao.status = "Processado"
    print(f"Valor: {transacao.valor}. \nStatus: {transacao.status}. \nProcessamento: {transacao.processar_pagamento()}. \n")