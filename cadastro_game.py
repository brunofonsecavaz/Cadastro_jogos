def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

# verifica se o arquivo existe
def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

#caso nao esxista arquivo cria um
def criarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro ao criar arquivo')
    else:
        print(f'Arquivo {nomeArquivo} criado comn sucesso\n')

#insere no arquivo o nome do jogo e do video game
def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        a.write(f'Jogo:{nomeJogo}\nVideo-Game: {nomeVideogame}\n') #escreve no arquivo
    finally:
        a.close()

# abre os dados para leitura, e printa na tela a lista com os dados
def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt' )
    except:
        print('Erro ao ler arquivo')
    else:
        print(a.read())
    finally:
        a.close()


#Programa principal
arquivo = 'games.txt'
if existeArquivo(arquivo):
    print('Arquivo localizado no computador')
else:
    print('Arquivo inexistente')
    criarArquivo(arquivo)

while True:
    print('MENU')
    print('1 - Cadastrar novo jogo')
    print('2 - Listar cadastro')
    print('3 - sair')

    op = valida_int('Escolha a opçao desejada: ', 1, 3)
    if op == 1: #cadastro novo item inserindo no arquivo
        print('Opçao de cadastro selecionada\n')
        nomeJogo = input('Nome do jogo: ')
        nomeVideogame = input('Nome do video game: ')
        cadastrarJogo(arquivo, nomeJogo, nomeVideogame)

    elif op == 2: #mostra a lista
        print('Opçao de listragem selecionada...\n')
        listarArquivo(arquivo)


    elif op == 3:
        print('Encerrando o programa...')
        break