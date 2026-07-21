def visualizar_contatos(lista_contatos):
    for indice, contato in enumerate (lista_contatos, start=1):
        favorito = "★" if contato["Favorito"] else "X"
        print(f'{indice}.  {contato["Nome"]} - {contato["Telefone"]} - {contato["Email"]} - {favorito}')
    return

def adicionar_contatos(lista_contatos, nome, telefone, email):
    contato = {"Nome": nome, "Telefone": telefone, "Email": email, "Favorito": False}
    lista_contatos.append(contato)
    print(f"\nContato de {nome} adicionado com sucesso!")
    return

def editar_contato(lista_contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    print("1. Nome")
    print("2. Telefone")
    print("3. Email")
    
    campo = input("\nQual campo deseja alterar?")

    if campo == "1":
        campo = "Nome"
    elif campo == "2":
        campo = "Telefone"
    elif campo == "3":
        campo = "Email"
    
    novo_valor = input(f"\nDigite o novo valor para o campo {campo}: ")

    lista_contatos[indice_contato_ajustado][campo] = novo_valor
    
    print(f"\nCampo {campo} ajustado para {novo_valor} com sucesso")
    
    return

def marcar_favorito(lista_contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    print("\nO que deseja fazer?")
    print("\n1. Marcar contato como favorito")
    print("2. Desmarcar contato como favorito")

    opcao = input("\nSelecione uma opção: ")
    
    if opcao == "1":
        lista_contatos[indice_contato_ajustado]["Favorito"] = True
    elif opcao == "2":
        lista_contatos[indice_contato_ajustado]["Favorito"] = False

    return

def visualizar_favoritos(lista_contatos):
    for indice, contato in enumerate (lista_contatos, start=1):
        favorito = "★"
        if contato["Favorito"]:
            print(f'{indice}.  {contato["Nome"]} - {contato["Telefone"]} - {contato["Email"]} - {favorito}')
    return

def apagar_contato(lista_contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    lista_contatos.pop(indice_contato_ajustado)
    return

lista_contatos = []

while True :
    print("\n1. Visualizar lista de contatos")
    print("2. Adicionar contato")
    print("3. Editar contato")
    print("4. Deletar contato")
    print("5. Marcar/Desmarcar contato como favorito")
    print("6. Visualizar lista de contatos favoritos")
    print("7. Sair")

    escolha = input("\n Selecione a opção desejada: ")

    if escolha == "1":
        visualizar_contatos(lista_contatos)

    elif escolha == "2":
        nome = input("\nDigite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")
        adicionar_contatos(lista_contatos, nome, telefone, email)

    elif escolha == "3":
        indice_contato = input("Qual o índice do contato que deseja editar?")
        editar_contato(lista_contatos, indice_contato)

    elif escolha == "4":
        indice_contato = input("Qual o índice do contato que deseja apagar?")
        apagar_contato(lista_contatos, indice_contato)

    elif escolha == "5":
        indice_contato = input("Qual o índice do contato que deseja marcar/desmarcar como favorito?")
        marcar_favorito(lista_contatos, indice_contato)

    elif escolha == "6":
        visualizar_favoritos(lista_contatos)

    elif escolha == "7":
        print("\nPrograma encerrado!")
        break
