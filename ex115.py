'''Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples. O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.'''

from time import sleep

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número inteiro válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar o número!\033[m')
            return 0
        else:
            return n

def linha(tam = 42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt(('Sua opção: '))
    return opc

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else: 
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome}, foi criado com sucesso!')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arq, nome = 'desconhecido', idade = 0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados.')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()

arq = 'ex115.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo.
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa.
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do Sistema. Até logo!')
        break
    else:
        print('ERRO! Digite uma opção válida!')
    sleep(2)