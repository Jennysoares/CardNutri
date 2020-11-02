import algoritmoGenetico as ag
import base_dados as bd

total_dias = 5
populacao = list()
for i in range(0, 10):
    populacao.append(ag.ini_populacao(total_dias, 0))


fitness = ag.funcao_fitness(populacao)
pais = ag.funcao_dizimacao(populacao, fitness)
filho = ag.cruzamento(pais, 0.8)
filho_mutado = ag.mutacao(filho, 0.05)


# for pop in populacao:
#    cont += 1
#    print('\n====== DIA %s ======'%cont)
#    for keys in pop.keys():
#        print('  %s ->' % keys)
#        for valores in pop[keys]:
#            print('      *%s' % valores.nome)
