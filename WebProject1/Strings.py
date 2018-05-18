class strings(object):
    primeiro_nome = 'Ruan'
    segundo_nome = 'Schwanz'
    terceiro_nome = 'Nunes'
    #concatenação de string em python
    nome_completo = primeiro_nome + ' ' + segundo_nome + ' ' + terceiro_nome
    #multiplicação em variaveis string
    nome_multiplicado = primeiro_nome * 5
    print(nome_completo)
    print(nome_multiplicado)

    #funções das variaveis tipo string
    #len te retorna a quantidade de caracteres da variavel
    len(primeiro_nome)
    # usando indices, retorna o primeiro caracter da string
    primeiro_nome[0]
    #usando indices de traz pra frente, lembre-se que ao retornar de traz pra frente inicia do numero 1
    primeiro_nome[-1]
    #pegando mais de uma letra (pega da primeira letra até a segunda)
    primeiro_nome[0:2]
    primeiro_nome[:2]
    #pegando de traz pra frente omitindo o 0
    primeiro_nome[-2:]


