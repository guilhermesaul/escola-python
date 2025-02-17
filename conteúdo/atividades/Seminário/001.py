quantidade_alunos = int(input("Digite a quantidade de alunos: "))
alunos = []
while True:
    print("*"*45)
    print("CADASTRO DE ALUNOS")
    print("*"*45)
    print("0. Sair")
    print("1. Adicionar aluno (nome, idade, gênero e média)")
    print("2. Remover aluno")
    print("3. Listar alunos")
    print("4. Ver média dos alunos")
    print("5. Buscar aluno")
    print("6. Quantidade de alunos reprovados (média 60)")
    print("*"*45)
    opcao = int(input("Digite o número correspondente à uma opção: "))
    if opcao == 0:
        print("Encerrando programa...")
        break
    elif opcao == 1:
        for l in range(quantidade_alunos):
            nome = str(input("Digite o nome do aluno: "))
            idade = str(input("Digite a idade do aluno: "))
            genero = str(input("Digite o gênero do aluno: "))
            media = str(input("Digite a média do aluno: "))
            alunos.append([nome, idade, genero, media])
    elif opcao == 2:
        remove