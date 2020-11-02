import algoritmoGenetico as ag
import base_dados as bd

total_dias = 5
populacao = list()
taxa_mutacao = 0.05
taxa_cruzamento = 0.8
nInd = 10
for i in range(0, nInd):
    populacao.append(ag.ini_populacao(total_dias, 0))

geracao_atual = populacao

for i in range(0, 50):

    fitness = ag.funcao_fitness(geracao_atual)

    nova_populacao = []
    for k in range(0, int(nInd/2)):
        pais = ag.funcao_dizimacao(geracao_atual, fitness)
        filhos_gerados = ag.cruzamento(pais, taxa_cruzamento)
        filhos_mutados = ag.mutacao(filhos_gerados, taxa_mutacao)
        nova_populacao.append(filhos_mutados[0])
        nova_populacao.append(filhos_mutados[1])

    geracao_atual = nova_populacao

fitness = ag.funcao_fitness(geracao_atual)
print("\n-=-=-=--=-=-=--=-=-=- MELHORES CARDAPIOS -=-=-=--=-=-=--=-=-=-\n")

# for pop in populacao:
#    cont += 1
#    print('\n====== DIA %s ======'%cont)
#    for keys in pop.keys():
#        print('  %s ->' % keys)
#        for valores in pop[keys]:
#            print('      *%s' % valores.nome)
