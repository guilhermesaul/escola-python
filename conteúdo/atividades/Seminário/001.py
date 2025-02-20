faxinas = []
#Menu para faxineiras
while True:
    print("*"*50)
    print("0. Encerrar programa")
    print("1. Adicionar valor da faxina")
    print("2. Remover valor da faxina")
    print("3. Ver valores das faxinas")
    print("4. Total obtido (em R$)")
    print("5. Excluir todas as faxinas")
    print("6. Maior preço obtido na faxina")
    print("7. Menor preço obtido na faxina")
    print("8. Média (em R$) das faxinas")
    print("9. Quantidade total de faxinas")
    print("*"*50)
    opcao = int(input("Digite uma opção correspondente acima: "))

    #Encerrar programa
    if opcao == 0:
        print("Encerrando programa...")
        break

    #Adicionar valor na lista
    elif opcao == 1:
        faxinas.append(float(input("Digite o valor obtido na faxina (em R$): ")))

    #Remover valor na lista
    elif opcao == 2:
        remover = float(input("Digite o valor que deseja remover (em R$): "))
        
        #Verificar se valor está na lista
        if remover in faxinas:
            faxinas.remove(remover)
            print("Valor removido com sucesso")
        else:
            print("Não existe esse valor na lista")

    #Listar lista
    elif opcao == 3:
        y = 1
        for x in faxinas:
            print(f"Na {y}° faxina você obteve: {x:.2f} R$")
            y += 1
            #Lista a lista, armazena um valor por vez na var x, e na var y vê o total de itens na lista e remove 1 numero a cada repetição

    #Exibe a soma de todas as faxinas
    elif opcao == 4:
        print(f"O total obtido foi: {sum(faxinas):.2f} R$")

    #Remove todos os valores da lista
    elif opcao == 5:
        faxinas.clear()
        print("Valores excluídos com sucesso")

    #Maior preço de todos nas faxinas
    elif opcao == 6:
        print(f"O maior preço obtido em uma faxina foi: {max(faxinas)} R$")

    #Menor preço de todos nas faxinas
    elif opcao == 7:
        print(f"O menor preço obtido em uma faxina foi: {min(faxinas)} R$")

    #Média em reais obtido nas faxinas
    elif opcao == 8:
        soma = sum(faxinas)
        quantidade = len(faxinas)
        media = soma/quantidade
        print(f"A média de R$ obtida nas faxinas foi de: {media:.2f} R$")

    #Total de faxinas
    elif opcao == 9:
        total = len(faxinas)
        print(f"O total de faxinas foi de: {total}")