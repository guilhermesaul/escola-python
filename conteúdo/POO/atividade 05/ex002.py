class MetodoPagamento:
    def __init__(self, valor:float):
        self.__valor = valor
        
    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, novo):
        self.__valor = novo
        
    def processar_pagamento(self):
        return "Pagamento processado"
    
class CartaoCredito(MetodoPagamento):
    def __init__(self, valor: float, numero_cartao):
        super().__init__(valor)
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
    def __init__(self, valor: float, codigo_barras):
        super().__init__(valor)
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
    def __init__(self, valor: float, chave_pix):
        super().__init__(valor)
        self.__chave_pix = chave_pix
        
    @property
    def chave_pix(self):
        return self.__chave_pix
    
    @chave_pix.setter
    def chave_pix(self, novo):
        self.__chave_pix = novo
        
    def processar_pagamento(self):
        return "Pagamento via Pix efetuado com sucesso!"
    
m1 = CartaoCredito(100.50, 12345678)
m2 = BoletoBancario(105, 87654321)
m3 = Pix(50, "exemplo@gmail.com")
transacoes_pendentes = [m1, m2, m3]
for transacao in transacoes_pendentes:
    print(transacao.processar_pagamento())