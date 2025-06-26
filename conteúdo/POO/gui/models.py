class Tarefa():
    
    def __init__(self, descricao, prioridade):
        self.descricao = descricao
        self.prioridade = prioridade
        self.concluida = False
        
    def concluir(self):
        if self.concluida == False:
            self.concluida = True

    def __str__(self):
        return f"{self.descricao} / {self.prioridade} / {self.concluida}"