class listaEtuple(object):
   #Tuple é um conjunto de dados na mes variavel definido com "()" e separado cada valor por virgula, as tuples não podem ser modificadas depois de instanciasdas
   meses = ('janeiro','fevereiro','março','abril')
   #listas também é um conjunto de dados porem separados por "[]", as listas podem ser atualizadas depois de atualizadas
    alunos = ['marcos','ruan']
    #printa na tela o primeiro indice
    print(alunos[0])
    #atualizando elementos da lista
    alunos [1] = 'jair'
    #adicionando novos elementos
    alunos.append('ricardo')
    #adicionando novos elementos em determinados indices
    alunos.insert(1,'paula')
    #ordenando a lista por ordem alfabetica
    alunos.sort()
    #retirando indices dizendo qual indice quer
    alunos.pop(1)
    #retirando elemntos pelo nome
    alunos.remov('paula')
    #concatenação com listas
    alunos2 = ['joana','jorge']
    totalDeAlunos = alunos + alunos2


    pass