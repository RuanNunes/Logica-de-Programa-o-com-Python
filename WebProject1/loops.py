class loops(object):
    #loop infinito
    x = 0
    #while tem o significado de "enquanto"
    while x < 1:
        nome = input('Qual o seu nome')

    while True:
        nome = input("Loop Infinito")

    #exemplo 2 
    pessoas = []
    while x < 4:
        nome = input('Qual o seu nome?')
        print('olá seu nome é: ' , nome)
        pessoas.append(nome)
        print('A lista contem as seguintes pessoas: ', pessoas)
        x +=  1

    #while enquanto tiver determinado carro na lista
    carro = []
    while 'fiat' not in carro:
        carro= input('Ditete o nome de um carro:')
    
    #outra forma
    while True:
        carro = input('Digite o nome de um carro.')
        if carro == 'fiat':
            #volta ao inicio do loop ou seja vai fazer com que o while fique infinito pelo fato de ter o "true no inicio"
            continue
            
    while True:
        carro = input('Digite o nome de um carro.')
        if carro == 'fiat':
            #diferente do while anterior o break não volta no inicio do loop para ferificar novamente e sai dele direto fazendo com que não fique um loop infinito 
            break


    #FOR exemplos
    compras = ['arroz', 'feijão','macarão']
    for i in compras:
        prit(i)

    #somatorio de valores em lista com for em loop
    vendas = [1000,300,400,500,30,40,50]
    total = 0
    for i in vendas:
        total += i
    print(i)

    #for em dicionarios
    cores = {'verde':'green', 'preto': 'black', 'azul': 'blue'}
    for i in cores:
        #o elemento "[]" serve para pegar em qual indice está para pegar o valor do tipo do dicionario
        print(i, 'em Ingles significa ' , cores[i])

    #for com lista dentro de listas
    compras = [['arroz', 'feijão'],['macarão','batata'],['suco','refri']]
    #for emcadeado para pegar cada elemento de cada lista e printar na tela
    for i in compras:
        for item in i:
            print(item)

    #for com condição de um numero até determinado numero 
    for i in range (0,10):
        print(i)

    #contagem regressiva
    for i in range(0,10):
        print(10-i)




    pass




