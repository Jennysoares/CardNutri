import algoritmoGenetico as ag
import base_dados as bd

total_dias = 1
populacao = list()
for i in range(0, 10):
    populacao.append(ag.ini_populacao(total_dias, 0))

fitness = ag.funcao_fitness(populacao)
pais = ag.funcao_dizimacao(populacao, fitness)
ag.cruzamento(pais)


# for pop in populacao:
#    cont += 1
#    print('\n====== DIA %s ======'%cont)
#    for keys in pop.keys():
#        print('  %s ->' % keys)
#        for valores in pop[keys]:
#            print('      *%s' % valores.nome)
