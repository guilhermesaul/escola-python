import tkinter as tk
from tkinter import messagebox
from models import Tarefa

class TelaPrincipal():

    def __init__(self, tela):
        self.lista_tarefas = []
        
        self.lb_descricao = tk.Label(tela, text="Descrição")
        self.lb_descricao.pack(pady = (0, 10))
        
        self.descricao = tk.Entry(tela, width=50)
        self.descricao.pack(pady = 10)
        
        self.lb_prioridade = tk.Label(tela, text="Prioridade")
        self.lb_prioridade.pack(pady = (0, 10))
        
        self.prioridade = tk.Entry(tela, width=50)
        self.prioridade.pack(pady = 10)
        
        self.adicionar = tk.Button(tela, text="Adicionar", command=self.inserir_list)
        self.adicionar.pack()
        
        self.lista = tk.Listbox(tela, width=50, height=20)
        self.lista.pack(pady = (0, 10))
        
        self.concluir = tk.Button(tela, text="Concluir", command=self.concluir)
        self.concluir.pack()
        
    def inserir_list(self):
        desc = self.descricao.get()
        prioridade = self.prioridade.get()
        tarefa = Tarefa(desc, prioridade)
        self.lista_tarefas.append(tarefa)
        self.lista.insert(tk.END, tarefa)
        
    def concluir(self):
        selecao = self.lista.curselection()
        if selecao:
            indice = selecao[0]
            self.lista_tarefas[indice].concluir()
            self.lista.delete(0, tk.END)
            for t in self.lista_tarefas:
                self.lista.insert(tk.END, t)
        else:
            messagebox.showwarning("Atenção", "Selecione")