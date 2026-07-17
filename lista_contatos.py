def adicionar_contatos(nome, telefone, email, lista_contatos):
    lista = {"Nome": nome, "Telefone": telefone, "Email": email, "Favorito": False}
    lista_contatos.append(lista)
    print("\nContato adicionado com sucesso")
    return

def visualizar_contatos(lista_contatos):
    for indice, lista in enumerate (lista_contatos, start=1):
        favorito = "Favorito" if lista["Favorito"] else " "
        print(f'{indice}. {lista["Nome"]} - {lista["Telefone"]} - {favorito}')
    return

def editar_contato(lista_contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(lista_contatos):        
        print("\n Qual campo deseja alterar?")
        print("1. Nome")
        print("2. Telefone")
        print("3. Email")
        print("4. Favorito")

        campo = input("Qual campo deseja alterar?")
        if campo == "1":
            campo = "Nome"
        elif campo == "2":
            campo = "Telefone"
        elif campo == "3":
            campo = "Email"
        elif campo == "4":
            campo = "Favorito"

        novo_valor = input(f"Digite o novo valor para o {campo}")

        if campo == "Favorito":
            novo_valor = False

        lista_contatos[indice_contato_ajustado][campo] = novo_valor

        print("Contato atualizado com sucesso")

    else:
        print("Indice nao existe")

    return

def excluir_contato(lista_contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    lista_contatos.pop(indice_contato_ajustado)
    return

def marcar_favorito(indice_contato, lista_contatos):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(lista_contatos):  
        lista_contatos[indice_contato_ajustado]["Favorito"] = True
        print("Contato marcado como favorito")
    else:
        print("Indice nao existe")
    return

def contatos_favoritos(lista_contatos):
    print("\nLista de contatos favoritos:")

    for indice, contato in enumerate(lista_contatos, start=1):

        if contato["Favorito"] == True:

            print(f'{indice}. {contato["Nome"]} - {contato["Telefone"]}')


lista_contatos = []

while True:
    print("\nBem vindo a sua agenda de contatos.")
    print("\n1. Visualizar lista de contatos")
    print("2. Adicionar contato")
    print("3. Editar contato")
    print("4. Excluir contato")
    print("5. Marcar contato como favorito")
    print("6. Lista de contatos favoritos")
    print("7. Sair")
    escolha = input("\nSelecione uma opção para seguir:")

    if escolha == "1":
        visualizar_contatos(lista_contatos)
    
    elif escolha == "2":
        nome = input("\nDigite o nome do contato: ")
        telefone = input("\nDigite o telefone do contato: ")
        email = input("\nDigite o email do contato: ")
        adicionar_contatos(nome, telefone, email, lista_contatos)

    elif escolha == "3":
        indice_contato = input("Qual o indice do contato que voce deseja alterar?")
        editar_contato(lista_contatos, indice_contato)

    elif escolha == "4":
        indice_contato = input("Qual o indice do contato que voce deseja excluir?")
        excluir_contato(indice_contato, lista_contatos)

    elif escolha == "5":
        indice_contato = input("Qual o indice do contato que voce deseja marcar como favorito?")
        marcar_favorito(indice_contato,lista_contatos)

    elif escolha == "6":
        contatos_favoritos(lista_contatos)
    
    elif escolha == "7":
        print("\nPrograma encerrado!")
        break