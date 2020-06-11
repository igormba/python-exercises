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
        C += 1
    print(linha())
    opc = leiaInt(('Sua opção: '))
    return opc
