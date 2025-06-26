class Motorista:
    def __init__(self, CPF, veiculo1, veiculo2, parentes):
        self.CPF = CPF
        self.veiculo1 = veiculo1
        self.veiculo2 = veiculo2
        self.parentes = []
class Supervisores:
    def __init__(self, CPF, parentes):
        self.CPF = CPF
        self.parentes = []
class Mecanicos: 
    def __init__(self, CPF, parentes):
        self.CPF = CPF
        self.parentes = []
class Moto:
    def __init__(self, registros):
        self.registros = []
class Van:
    def __init__(self, registros):
        self.registros = []
class Manutencao:
    def __init__(self, mecanico, supervisor, aprovado = False):
        self.mecanico = mecanico
        self.supervisor = supervisor
        self.aprovado = aprovado
        
    def aprovar_manutencao(self):
        if self.mecanico.cpf == self.supervisor.cpf:
            self.aprovado = False
        else:
            self.aprovado = True