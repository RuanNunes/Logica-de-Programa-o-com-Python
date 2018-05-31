class Condicionante(object):
   # idade = int(input('Digite sua Idade'))
   # idadeCarteira = int(input('Digite sua Idade para saber se voce pode tirar carteira'))
   # if idade >= 18:
    #    print('voce é maior de idade')
     #   print('teste de identação')
    #else:
     #   print('Voce é menor de idade')
    #print('fora do if Teste de identação')


   # if idade >= 18:
    #    print('Parabéns Voce ja pode tirar sua abilitação')
    #elif idade >= 22:
     #   print('Parabéns voce ja pode ser piloto de avião')
    #else:
     #   print('Aguade Mais alguns anos para poder tirar sua carteira')
    
    ## multiplas condições
    idade = int(input('Digite sua Idade'))
    sexo = input('Digite o sexo M ou F').lower()
    if sexo == 'm':
        if idade >= 18:
            print('Homem maior de idade')
        else:
            print('Homem menor de idade')
    elif idade >= 18:
        print('Mulher maior de idade')
    else:
        print('Mulher menor de idade')
        
            

    pass




