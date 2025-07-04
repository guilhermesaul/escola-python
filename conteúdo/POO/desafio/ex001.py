class Pedido:
    def __init__(
        self,
        id_pedido: int,
        protocolo_pedido: str,
        esfera: str,
        uf: str,
        municipio: str,
        orgao_destinatario: str,
        situacao: str,
        data_registro: str,
        prazo_atendimento: str,
        foi_prorrogado: str,
        foi_reencaminhado: str,
        forma_resposta: str,
        origem_solicitacao: str,
        id_solicitante: int,
        assunto_pedido: str,
        subassunto_pedido: str,
        tag: str,
        data_resposta: str,
        decisao: str,
        especificacao_decisao: str
    ):
        self.__id_pedido = id_pedido
        self.__protocolo_pedido = protocolo_pedido
        self.__esfera = esfera
        self.__uf = uf
        self.__municipio = municipio
        self.__orgao_destinatario = orgao_destinatario
        self.__situacao = situacao
        self.__data_registro = data_registro
        self.__prazo_atendimento = prazo_atendimento
        self.__foi_prorrogado = foi_prorrogado
        self.__foi_reencaminhado = foi_reencaminhado
        self.__forma_resposta = forma_resposta
        self.__origem_solicitacao = origem_solicitacao
        self.__id_solicitante = id_solicitante
        self.__assunto_pedido = assunto_pedido
        self.__subassunto_pedido = subassunto_pedido
        self.__tag = tag
        self.__data_resposta = data_resposta
        self.__decisao = decisao
        self.__especificacao_decisao = especificacao_decisao

    @property
    def id_pedido(self):
        return self.__id_pedido

    @id_pedido.setter
    def id_pedido(self, valor):
        self.__id_pedido = valor

    @property
    def protocolo_pedido(self):
        return self.__protocolo_pedido

    @protocolo_pedido.setter
    def protocolo_pedido(self, valor):
        self.__protocolo_pedido = valor

    @property
    def esfera(self):
        return self.__esfera

    @esfera.setter
    def esfera(self, valor):
        self.__esfera = valor

    @property
    def uf(self):
        return self.__uf

    @uf.setter
    def uf(self, valor):
        self.__uf = valor

    @property
    def municipio(self):
        return self.__municipio

    @municipio.setter
    def municipio(self, valor):
        self.__municipio = valor

    @property
    def orgao_destinatario(self):
        return self.__orgao_destinatario

    @orgao_destinatario.setter
    def orgao_destinatario(self, valor):
        self.__orgao_destinatario = valor

    @property
    def situacao(self):
        return self.__situacao

    @situacao.setter
    def situacao(self, valor):
        self.__situacao = valor

    @property
    def data_registro(self):
        return self.__data_registro

    @data_registro.setter
    def data_registro(self, valor):
        self.__data_registro = valor

    @property
    def prazo_atendimento(self):
        return self.__prazo_atendimento

    @prazo_atendimento.setter
    def prazo_atendimento(self, valor):
        self.__prazo_atendimento = valor

    @property
    def foi_prorrogado(self):
        return self.__foi_prorrogado

    @foi_prorrogado.setter
    def foi_prorrogado(self, valor):
        self.__foi_prorrogado = valor

    @property
    def foi_reencaminhado(self):
        return self.__foi_reencaminhado

    @foi_reencaminhado.setter
    def foi_reencaminhado(self, valor):
        self.__foi_reencaminhado = valor

    @property
    def forma_resposta(self):
        return self.__forma_resposta

    @forma_resposta.setter
    def forma_resposta(self, valor):
        self.__forma_resposta = valor

    @property
    def origem_solicitacao(self):
        return self.__origem_solicitacao

    @origem_solicitacao.setter
    def origem_solicitacao(self, valor):
        self.__origem_solicitacao = valor

    @property
    def id_solicitante(self):
        return self.__id_solicitante

    @id_solicitante.setter
    def id_solicitante(self, valor):
        self.__id_solicitante = valor

    @property
    def assunto_pedido(self):
        return self.__assunto_pedido

    @assunto_pedido.setter
    def assunto_pedido(self, valor):
        self.__assunto_pedido = valor

    @property
    def subassunto_pedido(self):
        return self.__subassunto_pedido

    @subassunto_pedido.setter
    def subassunto_pedido(self, valor):
        self.__subassunto_pedido = valor

    @property
    def tag(self):
        return self.__tag

    @tag.setter
    def tag(self, valor):
        self.__tag = valor

    @property
    def data_resposta(self):
        return self.__data_resposta

    @data_resposta.setter
    def data_resposta(self, valor):
        self.__data_resposta = valor

    @property
    def decisao(self):
        return self.__decisao

    @decisao.setter
    def decisao(self, valor):
        self.__decisao = valor

    @property
    def especificacao_decisao(self):
        return self.__especificacao_decisao

    @especificacao_decisao.setter
    def especificacao_decisao(self, valor):
        self.__especificacao_decisao = valor
