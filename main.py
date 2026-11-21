from collections import deque
from time import sleep

#Estruturas em memória. Todas começam vazias, como foi pedido no trabalho
triagem_fila = deque() #fila da triagem: entra no fim (append) e sai pelo início (popleft)
pilha = deque() #pilha de prontuários: entra e sai sempre pelo topo (append / pop)
lista = [] #lista de pacientes internados: uso list normal pois preciso mexer em qualquer posição
arvore = {} #árvore de especialidades: dicionários aninhados (área -> especialidade -> diagnóstico)

nome_arquivo = 'dados_sistema.txt' #único arquivo de persistência do sistema


# ================================ FILA ================================

def fila_inserir ():
    while True: #força a entrada do ID como inteiro
        id_paciente = input("ID do paciente: ").strip()
        try:
            id_paciente = int(id_paciente)
            break #se converteu certo, sai do laço
        except ValueError:
            print("Insira apenas números inteiros.")
    nome_paciente = input("Nome paciente: ").strip()
    while not nome_paciente: #não deixa o nome ficar vazio
        print("Digite um nome válido!")
        nome_paciente = input("Nome paciente: ").strip()
    prioridade_paciente = input("Prioridade [Alta / Média / Baixa]: ").strip().upper()
    while prioridade_paciente not in ('ALTA', 'MÉDIA', 'BAIXA'):
        print("Digite uma prioridade válida!")
        prioridade_paciente = input("Prioridade [Alta / Média / Baixa]: ").strip().upper()
    triagem_fila.append([id_paciente, nome_paciente, prioridade_paciente]) #append coloca sempre no FIM da fila
    print("Paciente adicionado na fila com sucesso.")

def fila_listar():
    if not triagem_fila:
        print("Fila vazia!")
    else:
        print("Fila atual: \n")
        for index, pac in enumerate(triagem_fila, start=1): #start=1 para a posição começar do 1 e não do 0
            print(f"Posição: {index} | Nome: {pac[1]} ID: {pac[0]} Prioridade: {pac[2]}")

def fila_atualizar():
    if not triagem_fila:
        print("Fila vazia!")
        return #return sai da função na hora, sem executar o resto
    id_paciente = input("ID do paciente para alteração: ").strip()
    try:
        id_paciente = int(id_paciente) #o ID foi guardado como int no fila_inserir, então comparo int com int
    except ValueError:
        print("Digite apenas números inteiros.")
        return
    paciente_encontrado = None #começa sem nada e só recebe o paciente se achar
    for pac in triagem_fila:
        if pac[0] == id_paciente: #pac[0] é o ID dentro da lista [id, nome, prioridade]
            paciente_encontrado = pac
            break
    if not paciente_encontrado:
        print("Paciente não encontrado. Tente novamente.")
    else:
        nova_prioridade_paciente = input("Nova prioridade [Alta / Média / Baixa]: ").strip().upper()
        while nova_prioridade_paciente not in ('ALTA', 'MÉDIA', 'BAIXA'):
            print("Digite uma prioridade válida!")
            nova_prioridade_paciente = input("Nova prioridade [Alta / Média / Baixa]: ").strip().upper()
        paciente_encontrado[2] = nova_prioridade_paciente #muda só o dado. A posição dele na fila continua a mesma
        print(f"Prioridade do paciente {paciente_encontrado[1]} alterada com sucesso!")

def fila_remover_chamar_paciente():
    if not triagem_fila:
        print("Fila vazia.")
    else:
        pac = triagem_fila.popleft() #popleft tira o PRIMEIRO da fila: quem chegou antes é atendido antes (FIFO)
        print(f"Chamando para atendimento: {pac[1]} (ID: {pac[0]} | Prioridade: {pac[2]}).")

# A fila só pode remover pelo início (popleft). Por isso tirei a opção de remover um paciente
# qualquer pelo nome: isso seria tirar alguém do meio da fila e quebraria a regra do FIFO.

def menu_fila():
    while True:
        print("\n--- FILA DE TRIAGEM ---")
        print("1 - Adicionar paciente")
        print("2 - Ver fila")
        print("3 - Atualizar prioridade")
        print("4 - Chamar próximo")
        print("0 - Voltar")
        opcao = input("Opção: ").strip()
        try:
            opcao = int(opcao)
        except ValueError:
            print("Digite um número válido.")
            continue #volta para o início do laço e mostra o menu de novo
        if opcao == 1:
            fila_inserir()
        elif opcao == 2:
            fila_listar()
        elif opcao == 3:
            fila_atualizar()
        elif opcao == 4:
            fila_remover_chamar_paciente()
        elif opcao == 0:
            print("Saindo das filas...")
            sleep(1)
            break
        else:
            print("Essa opção não existe!")


# ================================ PILHA ================================

def pilha_inserir():
    nome_paciente_pilha = input("Nome paciente: ").strip()
    while not nome_paciente_pilha:
        print("Digite um nome válido!")
        nome_paciente_pilha = input("Nome paciente: ").strip()
    historico_paciente = input("Descrição clínica: ").strip()
    while True: #força a idade a ser um número inteiro
        idade_paciente = input("Idade paciente: ").strip()
        try:
            idade_paciente = int(idade_paciente)
            break
        except ValueError:
            print("Digite um valor válido para idade do paciente.")
    cpf_paciente = input("CPF: ").strip().replace('.', '').replace('-', '')
    while not (cpf_paciente.isdigit() and len(cpf_paciente) == 11): #isdigit() verifica se tem só números
        print("Digite um CPF válido com 11 números.")
        cpf_paciente = input("CPF: ").strip().replace('.', '').replace('-', '')
    #CPF fica como string e não como int, pois se começar com 0 o int apagaria esse 0 da frente
    desejo_pilha = input("Deseja realmente inserir [S / N]? ").strip().upper()
    while desejo_pilha not in ('S', 'N'):
        print("Digite apenas S ou N.")
        desejo_pilha = input("Deseja realmente inserir [S / N]? ").strip().upper()
    if desejo_pilha == 'N': #o if fica fora do while, senão o append de baixo era feito mesmo dizendo N
        print("Inserção cancelada.")
        return
    pilha.append([nome_paciente_pilha, historico_paciente, idade_paciente, cpf_paciente]) #append coloca no TOPO da pilha
    print("Histórico adicionado com sucesso.")

def pilha_ver_histórico():
    if not pilha:
        print("Sem históricos para amostrar.")
        return
    while True:
        tamanho_consulta_historico = input("Quantos últimos históricos você deseja ver? ").strip()
        try:
            tamanho_consulta_historico = int(tamanho_consulta_historico)
            if tamanho_consulta_historico <= 0:
                print("Digite um número maior que 0.")
                continue
            break
        except ValueError:
            print("Valor quantitativo inválido.")
    print(f"Exibindo até {tamanho_consulta_historico} últimos históricos clínicos.\n")
    for index, pac in enumerate(reversed(pilha), start=1): #reversed percorre do topo (último que entrou) até a base
        marcador = ' <- TOPO'if index == 1 else '' #marca o topo para ficar claro qual sai primeiro
        print(f"{index}º | Nome: {pac[0]} | Idade: {pac[2]} | CPF: {pac[3]}{marcador}")
        print(f"Histórico clínico: {pac[1]}")
        print("\n")
        if index == tamanho_consulta_historico: #quando chega na quantidade pedida, para de mostrar
            break

def pilha_atualizar_prontuario():
    if not pilha:
        print("Pilha vazia. Nenhum prontuário para atualizar.")
        return
    pac = pilha[-1] #[-1] pega o TOPO da pilha. Na pilha só mexo no topo, nunca no meio
    print(f"Dados atuais do prontuário do topo:")
    print(f"Nome: {pac[0]} | Idade: {pac[2]} | CPF: {pac[3]}")
    print(f"Histórico clínico: {pac[1]}")
    print("\n")
    alterar_nome = input("Nome atualizado (ou aperte ENTER para deixar a atual): ").strip() or pac[0] #o 'or' usa o valor antigo se der ENTER vazio
    while True:
        alterar_idade = input("Idade atualizada (ou aperte ENTER para deixar a atual): ").strip() or str(pac[2])
        try:
            alterar_idade = int(alterar_idade)
            break
        except ValueError:
            print("Digite uma idade válida.")
    alterar_historico_clinico = input("Histórico clínico atualizado (ou aperte ENTER para deixar a atual): ").strip() or pac[1]
    desejo_pilha = input("Deseja realmente atualizar os dados [S / N]? ").strip().upper()
    while desejo_pilha not in ('S', 'N'):
        print("Digite apenas S ou N.")
        desejo_pilha = input("Deseja realmente atualizar os dados [S / N]? ").strip().upper()
    if desejo_pilha == 'N':
        print("Atualização cancelada.")
        return
    pac[0] = alterar_nome #altero direto na lista que está no topo, sem fazer append (append criaria um prontuário repetido)
    pac[1] = alterar_historico_clinico
    pac[2] = alterar_idade #o CPF não muda, por isso nem peço ele
    print("Dados atualizados com sucesso!")

def pilha_remover_prontuario():
    if not pilha:
        print("Pilha vazia. Nenhum prontuário para remover.")
        return
    pac = pilha[-1] #mostra o topo, que é o único que pode sair
    print(f"Prontuário do topo:")
    print(f"Nome: {pac[0]} | Idade: {pac[2]} | CPF: {pac[3]}")
    print(f"Histórico clínico: {pac[1]}")
    print("\n")
    decisao_pilha = input("Deseja realmente remover [S / N]? ").strip().upper()
    while decisao_pilha not in ('S', 'N'):
        print("Digite apenas S ou N.")
        decisao_pilha = input("Deseja realmente remover [S / N]? ").strip().upper()
    if decisao_pilha == 'N':
        print("Remoção cancelada.")
        return
    pilha.pop() #pop() sem índice tira o TOPO: o último que entrou é o primeiro a sair (LIFO)
    print("Histórico removido com sucesso!")

def menu_pilha():
    while True:
        print("\n--- PILHA DE PRONTUÁRIOS ---")
        print("1 - Adicionar prontuário")
        print("2 - Ver últimos prontuários")
        print("3 - Atualizar prontuário do topo")
        print("4 - Remover prontuário do topo")
        print("0 - Sair")
        opcao = input("Opção: ").strip()
        try:
            opcao = int(opcao)
        except ValueError:
            print("Digite um número válido.")
            continue
        if opcao == 1:
            pilha_inserir()
        elif opcao == 2:
            pilha_ver_histórico()
        elif opcao == 3:
            pilha_atualizar_prontuario()
        elif opcao == 4:
            pilha_remover_prontuario()
        elif opcao == 0:
            print("Saindo das pilhas...")
            sleep(1)
            break
        else:
            print("Essa opção não existe!")


# ================================ LISTA ================================

def lista_inserir():
    nome_paciente_fila = input("Nome paciente: ").strip()
    while not nome_paciente_fila:
        print("Digite um nome válido!")
        nome_paciente_fila = input("Nome paciente: ").strip()
    historico_paciente_fila = input("Descrição clínica: ").strip()
    while True:
        idade_paciente_fila = input("Idade paciente: ").strip()
        try:
            idade_paciente_fila = int(idade_paciente_fila)
            break
        except ValueError:
            print("Digite um valor válido para idade do paciente.")
    cpf_paciente_fila = input("CPF: ").strip().replace('.', '').replace('-', '')
    while not (cpf_paciente_fila.isdigit() and len(cpf_paciente_fila) == 11):
        print("Digite um CPF válido com 11 números.")
        cpf_paciente_fila = input("CPF: ").strip().replace('.', '').replace('-', '')
    comorbidade_paciente_fila = input("Comorbidade: ").strip()
    data_internacao_fila = input("Data internação: ").strip()
    while True:
        numero_leito_fila = input("Número leito: ").strip()
        try:
            numero_leito_fila = int(numero_leito_fila)
        except ValueError:
            print("Digite um valor inteiro válido para leitos.")
            continue
        leito_ocupado = False
        for pac in lista: #verifica se já tem alguém internado nesse leito
            if pac[6] == numero_leito_fila:
                leito_ocupado = True
                break
        if leito_ocupado:
            print(f"Leito {numero_leito_fila} já está ocupado! Escolha outro.")
        else:
            break
    desejo_lista = input("Deseja realmente cadastrar esses dados [S / N]? ").strip().upper() #faltava o upper(), aí 's' minúsculo não era aceito
    while desejo_lista not in ('S', 'N'):
        print("Digite apenas S ou N.")
        desejo_lista = input("Deseja realmente cadastrar esses dados [S / N]? ").strip().upper()
    if desejo_lista == 'N':
        print("Cadastro cancelado.")
        return
    lista.append([nome_paciente_fila, historico_paciente_fila, idade_paciente_fila, cpf_paciente_fila, comorbidade_paciente_fila, data_internacao_fila, numero_leito_fila])
    print("Paciente-leito cadastrado com sucesso.")

def lista_pacientes_internados():
    print("Carregando lista de pacientes internados. Aguarde!")
    sleep(1.5)
    if not lista:
        print("Sem pacientes internados.")
    else:
        for index, pac in enumerate(lista): #aqui o índice começa no 0, igual ao índice real dentro da lista
            print(f"Índice: {index} | Nome: {pac[0]} | Idade: {pac[2]} | CPF: {pac[3]}")
            print(f"Comorbidade(s): {pac[4]} | Data internação: {pac[5]} | Número leito: {pac[6]}")
            print(f"Histórico clínico: {pac[1]}")
            print("\n")
    #essa função agora só lista (o R do CRUD). A parte de remover foi para a lista_remover

def lista_atualizar():
    if not lista:
        print("Sem pacientes internados.")
        return
    nome_paciente = input("Nome paciente: ").strip()
    paciente_encontrado = None
    for pac in lista:
        if pac[0].lower() == nome_paciente.lower(): #lower() nos dois para não diferenciar maiúscula de minúscula
            paciente_encontrado = pac
            break
    if not paciente_encontrado:
        print("Paciente não encontrado. Tente novamente.")
        return
    pac = paciente_encontrado
    print(f"Nome: {pac[0]} | Idade: {pac[2]} | CPF: {pac[3]}")
    print(f"Comorbidade(s): {pac[4]} | Data internação: {pac[5]} | Número leito: {pac[6]}")
    print(f"Histórico clínico: {pac[1]}")
    print("\n")
    alterar_nome = input("Nome atualizado (ou aperte ENTER para deixar a atual): ").strip() or pac[0]
    while True:
        alterar_idade = input("Idade atualizada (ou aperte ENTER para deixar a atual): ").strip() or str(pac[2])
        try:
            alterar_idade = int(alterar_idade)
            break
        except ValueError:
            print("Digite uma idade válida.")
    alterar_comorbidade = input("Comorbidade atualizada (ou aperte ENTER para deixar a atual): ").strip() or pac[4]
    while True:
        alterar_leito = input("Número leito atualizado (ou aperte ENTER para deixar a atual): ").strip() or str(pac[6])
        try:
            alterar_leito = int(alterar_leito)
            break
        except ValueError:
            print("Digite um valor inteiro válido para leitos.")
    alterar_historico_clinico = input("Histórico clínico atualizado (ou aperte ENTER para deixar a atual): ").strip() or pac[1]
    desejo_lista = input("Deseja realmente atualizar os dados [S / N]? ").strip().upper()
    while desejo_lista not in ('S', 'N'):
        print("Digite apenas S ou N.")
        desejo_lista = input("Deseja realmente atualizar os dados [S / N]? ").strip().upper()
    if desejo_lista == 'N':
        print("Atualização cancelada.")
        return
    pac[0] = alterar_nome #altero direto no paciente que já está na lista
    pac[1] = alterar_historico_clinico
    pac[2] = alterar_idade
    pac[4] = alterar_comorbidade
    pac[6] = alterar_leito #CPF e data de internação não mudam
    print("Dados atualizados com sucesso!")

def lista_remover():
    if not lista:
        print("Sem pacientes internados.")
        return
    nome_paciente = input("Nome paciente: ").strip()
    paciente_encontrado = None
    for pac in lista:
        if pac[0].lower() == nome_paciente.lower():
            paciente_encontrado = pac
            break
    if not paciente_encontrado:
        print("Paciente não encontrado. Tente novamente.")
        return
    pac = paciente_encontrado
    print(f"Nome: {pac[0]} | Idade: {pac[2]} | CPF: {pac[3]}")
    print(f"Comorbidade(s): {pac[4]} | Data internação: {pac[5]} | Número leito: {pac[6]}")
    print(f"Histórico clínico: {pac[1]}")
    print("\n")
    decisao_lista = input("Deseja realmente remover [S / N]? ").strip().upper()
    while decisao_lista not in ('S', 'N'):
        print("Digite apenas S ou N.")
        decisao_lista = input("Deseja realmente remover [S / N]? ").strip().upper()
    if decisao_lista == 'N':
        print("Remoção cancelada.")
        return
    lista.remove(pac) #na lista posso remover de qualquer posição, diferente da fila e da pilha
    print("Paciente-leito removido com sucesso! Leito liberado.")

def menu_lista():
    while True:
        print("\n--- LISTA DE PACIENTES ---")
        print("1 - Cadastrar paciente-leito")
        print("2 - Ver lista pacientes-leito")
        print("3 - Atualizar cadastro paciente-leito")
        print("4 - Remover paciente-leito")
        print("0 - Sair")
        opcao = input("Opção: ").strip()
        try:
            opcao = int(opcao)
        except ValueError:
            print("Digite um número válido.")
            continue
        if opcao == 1:
            lista_inserir()
        elif opcao == 2:
            lista_pacientes_internados()
        elif opcao == 3:
            lista_atualizar()
        elif opcao == 4:
            lista_remover()
        elif opcao == 0:
            print("Saindo da lista...")
            sleep(1)
            break
        else:
            print("Essa opção não existe!")


# ================================ ÁRVORE ================================
# A árvore tem 3 níveis fixos, igual pastas no computador:
# Área (raiz) -> Especialidade (filho) -> Diagnóstico (folha, sem filhos = dicionário vazio {})
# Exemplo: {'Clinica Geral': {'Cardiologia': {'Arritmia': {}, 'Hipertensao': {}}}}

def arvore_adicionar(area, especialidade, diagnostico):
    if area not in arvore: #se a área ainda não existe, cria ela com um dicionário vazio
        arvore[area] = {}
    if especialidade not in arvore[area]: #mesma coisa para a especialidade dentro da área
        arvore[area][especialidade] = {}
    arvore[area][especialidade][diagnostico] = {} #o diagnóstico é a folha, por isso recebe {} (não tem filhos)
    #essa função é usada tanto no arvore_inserir quanto no carregar_dados, por isso separei ela

def arvore_inserir():
    area = input("Área (ex: Clinica Geral): ").strip()
    especialidade = input("Especialidade (ex: Cardiologia): ").strip()
    diagnostico = input("Diagnóstico (ex: Arritmia): ").strip()
    if not area or not especialidade or not diagnostico:
        print("Nenhum campo pode ficar vazio!")
        return
    arvore_adicionar(area, especialidade, diagnostico)
    print("Inserido na árvore com sucesso.")

def arvore_exibir():
    if not arvore:
        print("Árvore vazia.")
        return
    for area in arvore: #primeiro nível: as áreas (raízes)
        print(area)
        for especialidade in arvore[area]: #segundo nível: especialidades de cada área
            print("    " + especialidade) #os espaços na frente mostram o nível da árvore
            for diagnostico in arvore[area][especialidade]: #terceiro nível: diagnósticos (folhas)
                print("        " + diagnostico)

def arvore_atualizar():
    area = input("Área: ").strip()
    especialidade = input("Especialidade: ").strip()
    diagnostico = input("Diagnóstico atual: ").strip()
    if area in arvore and especialidade in arvore[area] and diagnostico in arvore[area][especialidade]: #navega nível por nível
        novo = input("Novo nome do diagnóstico: ").strip()
        if not novo:
            print("Nome inválido!")
            return
        del arvore[area][especialidade][diagnostico] #apaga a chave com o nome antigo
        arvore[area][especialidade][novo] = {} #cria de novo com o nome novo
        print("Diagnóstico atualizado com sucesso!")
    else:
        print("Caminho não encontrado na árvore.")

def arvore_remover():
    area = input("Área: ").strip()
    especialidade = input("Especialidade: ").strip()
    diagnostico = input("Diagnóstico: ").strip()
    if area in arvore and especialidade in arvore[area] and diagnostico in arvore[area][especialidade]:
        del arvore[area][especialidade][diagnostico]
        if not arvore[area][especialidade]: #se a especialidade ficou sem diagnóstico, apago ela também
            del arvore[area][especialidade]
        if not arvore[area]: #e se a área ficou sem especialidade, apago a área
            del arvore[area]
        #faço essa limpeza pois no arquivo só salvo caminhos completos (área|especialidade|diagnóstico)
        print("Diagnóstico removido com sucesso!")
    else:
        print("Caminho não encontrado na árvore.")

def menu_arvore():
    while True:
        print("\n--- ÁRVORE DE ESPECIALIDADES E DIAGNÓSTICOS ---")
        print("1 - Inserir diagnóstico")
        print("2 - Exibir árvore")
        print("3 - Atualizar diagnóstico")
        print("4 - Remover diagnóstico")
        print("0 - Sair")
        opcao = input("Opção: ").strip()
        try:
            opcao = int(opcao)
        except ValueError:
            print("Digite um número válido.")
            continue
        if opcao == 1:
            arvore_inserir()
        elif opcao == 2:
            arvore_exibir()
        elif opcao == 3:
            arvore_atualizar()
        elif opcao == 4:
            arvore_remover()
        elif opcao == 0:
            print("Saindo da árvore...")
            sleep(1)
            break
        else:
            print("Essa opção não existe!")


# ============================= PERSISTÊNCIA =============================

def salvar_dados():
    #'w' apaga o que tinha no arquivo e escreve tudo de novo com o que está na memória agora
    #encoding='utf-8' para os acentos (Média, Clínica...) não ficarem estranhos no arquivo
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo: #o with fecha o arquivo sozinho no final
        for pac in triagem_fila: #percorre do primeiro ao último, então a ordem da fila fica igual no arquivo
            arquivo.write(f"FILA|{pac[0]}|{pac[1]}|{pac[2]}\n")
        for pac in pilha: #percorre da base até o topo, então ao carregar com append o topo volta a ser o último
            arquivo.write(f"PILHA|{pac[0]}|{pac[1]}|{pac[2]}|{pac[3]}\n")
        for pac in lista:
            arquivo.write(f"LISTA|{pac[0]}|{pac[1]}|{pac[2]}|{pac[3]}|{pac[4]}|{pac[5]}|{pac[6]}\n")
        for area in arvore: #mesmos 3 for do arvore_exibir, mas escrevendo cada caminho completo numa linha
            for especialidade in arvore[area]:
                for diagnostico in arvore[area][especialidade]:
                    arquivo.write(f"ARVORE|{area}|{especialidade}|{diagnostico}\n")
    print(f"Dados salvos com sucesso em {nome_arquivo}!")

def carregar_dados():
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo: #'r' é só para leitura
            linhas = arquivo.readlines() #cada linha do arquivo vira um item da lista 'linhas'
    except FileNotFoundError: #se o arquivo ainda não existe (nunca salvou nada)
        print(f"Arquivo {nome_arquivo} não encontrado. Salve os dados primeiro.")
        return
    triagem_fila.clear() #limpo tudo antes de carregar, senão os dados ficariam duplicados
    pilha.clear()
    lista.clear()
    arvore.clear()
    for linha in linhas:
        partes = linha.strip().split('|') #split('|') separa a linha a cada '|' (igual o exercício 8 e 10)
        if partes[0] == 'FILA': #partes[0] é o identificador da estrutura
            triagem_fila.append([int(partes[1]), partes[2], partes[3]]) #int() pois no arquivo tudo vira texto
        elif partes[0] == 'PILHA':
            pilha.append([partes[1], partes[2], int(partes[3]), partes[4]])
        elif partes[0] == 'LISTA':
            lista.append([partes[1], partes[2], int(partes[3]), partes[4], partes[5], partes[6], int(partes[7])])
        elif partes[0] == 'ARVORE':
            arvore_adicionar(partes[1], partes[2], partes[3]) #reaproveito a mesma função de inserir da árvore
    print("Dados carregados com sucesso!")


# ============================ MENU PRINCIPAL ============================

def menu_principal():
    while True:
        print("\n" + " SISTEMA HOSPITALAR ".center(40, "-")) #center(tamanho, caractere) para centralizar
        print("1 - Fila de triagem")
        print("2 - Histórico de prontuários")
        print("3 - Lista de pacientes-leito")
        print("4 - Árvore de especialidade e diagnósticos")
        print("5 - Salvar dados")
        print("6 - Carregar dados")
        print("0 - Sair")
        op = input("Opção: ").strip()
        try:
            op = int(op)
        except ValueError:
            print("Digite um valor válido!")
            continue
        if op == 1:
            menu_fila()
        elif op == 2:
            menu_pilha()
        elif op == 3:
            menu_lista()
        elif op == 4:
            menu_arvore()
        elif op == 5:
            salvar_dados()
        elif op == 6:
            carregar_dados()
        elif op == 0: #0 sem aspas, pois o op já foi convertido para int lá em cima
            user = input("Deseja salvar os dados antes de sair? [S/N] ").strip().upper()
            while user not in ('S', 'N'):
                print("Digite apenas S ou N!")
                user = input("Deseja salvar os dados antes de sair? [S/N] ").strip().upper()
            if user == 'S':
                salvar_dados()
            print("Encerrando programa. Até logo!")
            sleep(1)
            break
        else:
            print("Essa opção não existe!")

menu_principal() #começa o programa chamando o menu principal