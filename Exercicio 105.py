def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de varios alunos.
    :param n: uma ou maisnotas dos alunos (aceita varias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    rest = {}
    print(*"=")
    rest['total'] = len(n)
    rest['media'] = sum(n)/len(n)
    rest['maior'] = max(n)
    rest['menor'] = min(n)
    if sit:
        if rest['media'] >= 7:
            rest['situacao'] = "BOA"
        elif 7 > rest['media'] >= 6:
            rest['situacao'] = "RAZOAVEL"
        elif rest['media'] < 6:
            rest['situacao'] = "RUIM"
    return rest


nota = notas(5, 5, 6.8, 10, 10, 8, 5.9, sit=False)
print(nota)
