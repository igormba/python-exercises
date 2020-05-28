'''Crie um programa onde o usúario digite uma expressão qualquer que use parênteses. Seu programa deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''

pilha = list()
expressao = str(input('Digite uma expressão: '))
for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão não é válida!')