class Livro:
    def __init__(self, titulo:str, autor:str, ano:int):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True

    def emprestar(self):       
        self.disponivel = False

    def devolver(self):
        self.disponivel = True
        
class Usuario:
    def __init__(self, nome:str, id_usuario:int, livros_emprestados):
        self.nome = nome
        self.id_usuario = id_usuario
        self.livros_emprestados = []
        
    def emprestar_livro(self):
        if Livro.disponivel:
            Livro.disponivel = False
            self.livros_emprestados.append(Livro)
    
    def devolver_livro(self):
        self.livros_emprestados.remove(Livro)
        Livro.disponivel = True
        
class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.acervo = []
        self.usuarios = []
        
    def adicionar_livro(self, livro):
        self.acervo.append(livro)

    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)
    
    def buscar_livro_por_titulo(self, titulo):
        for livro in self.acervo:
            if livro.titulo.lower() == titulo.lower():
                return livro