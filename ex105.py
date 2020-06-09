'''Faça um programa que tenha uma função nota() que pode receber várias notas de alunos e vai retornar um dicionario
com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (Opcional)
Adicione também as docstrings da função.'''

def nota(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (Aceita várias).
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n) / len(n)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'Boa'
        elif r['Média'] >= 5:
            r['Situação'] = 'Razoavél'
        else:
            r['Situação'] = 'Ruim'
    return r


resp = nota(5.5, 6, 7.8, 9, 10, sit=True)
print(resp)
help(nota)


