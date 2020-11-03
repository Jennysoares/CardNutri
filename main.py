import algoritmoGenetico as ag

total_dias = 5
populacao = list()
taxa_mutacao = 0.05
taxa_cruzamento = 0.8
nInd = 100
for i in range(0, nInd):
    populacao.append(ag.ini_populacao(total_dias, 0))

geracao_atual = populacao
la = 0
for i in range(0, 500):

    fitness = ag.funcao_fitness(geracao_atual)
    corte_populacao = ag.funcao_dizimacao_corte(geracao_atual, fitness)

    nova_populacao = []
    for k in range(0, int(nInd/2)):
        pais = ag.funcao_dizimacao_pais(corte_populacao)
        filhos_gerados = ag.cruzamento(pais, taxa_cruzamento)
        filhos_mutados = ag.mutacao(filhos_gerados, taxa_mutacao)
        nova_populacao.append(filhos_mutados[0])
        nova_populacao.append(filhos_mutados[1])

    geracao_atual = nova_populacao

fitness = ag.funcao_fitness(geracao_atual)

cardap = 0
for cardapio in geracao_atual:
    cont = 0
    cardap += 1
    print('\n====== Cardapio {} ======'.format(cardap))
    for cardapiodia in cardapio:
        cont += 1
        print('\n=* Dia {} =*'.format(cont))
        for refeicao in cardapiodia:
            print(f' - {refeicao} -> ', end='')
            for prato in cardapiodia[refeicao]:
                print(f'{prato.nome}, ', end='')
            print()
