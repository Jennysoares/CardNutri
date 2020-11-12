import csv
import classes

alimentos_grupo = dict([('Cereais e derivados', 0),
                        ('Verduras, hortaliças e derivados', 0,),
                        ('Frutas e derivados', 0,),
                        ('Gorduras e óleos', 0,),
                        ('Pescados e frutos do mar', 0,),
                        ('Carnes e derivados', 0,),
                        ('Leite e derivados', 0,),
                        ('Bebidas', 0,),
                        ('Ovos e derivados', 0,),
                        ('Produtos açucarados', 0,),
                        ('Miscelâneas', 0,),
                        ('alimentos industrializados', 0,),
                        ('Alimentos preparados', 0,),
                        ('Leguminosas e derivados', 0,),
                        ('Nozes e sementes', 0,), ])

for key in alimentos_grupo:
    aux = list()
    with open('alimentos.csv', 'r', encoding='utf-8-sig') as ficheiro:
        reader = csv.reader(ficheiro, delimiter=';')
        for linha in reader:
            if linha[11] == key:
                nutrientes = dict(Energia=linha[2],
                                  Proteína=linha[3],
                                  Lipídeos=linha[4],
                                  Carboidrato=linha[5],
                                  Fibra=linha[6],
                                  Cálcio=linha[7],
                                  Magnésio=linha[8],
                                  Ferro=linha[9],
                                  Zinco=linha[10])
                alimento = classes.Alimento(linha[0], linha[1], 0, nutrientes, linha[11])
                aux.append(alimento)
    alimentos_grupo[key] = aux

todos_alimentos = []
for key in alimentos_grupo.keys():
    todos_alimentos += (alimentos_grupo[key])

pratos_grupo = dict([('Acompanhamento Arroz', 0),
                     ('Acompanhamento Feijão', 0),
                     ('Bebida Láctea', 0)],
                    Guarnição=0,
                    Principal=0,
                    Sobremesa=0,
                    Bebida=0,
                    Fruta=0,
                    Lanche=0)

for key in pratos_grupo:
    aux = list()
    with open('pratos.csv', 'r', encoding='utf-8-sig') as ficheiro:
        reader = csv.DictReader(ficheiro, delimiter=';')
        for prat in reader:
            energ = 0
            prot = 0
            lip = 0
            carbo = 0
            fibra = 0
            calcio = 0
            magne = 0
            ferro = 0
            zinco = 0

            if prat['Tipo'] == key:
                i = 0
                dict_alimentos = dict()
                alimentos_prato = prat['Alimentos'].split(',')

                tamanho = len(alimentos_prato)

                while True:
                    for busca in todos_alimentos:
                        if busca.id == alimentos_prato[i]:
                            dict_alimentos.update({busca: float(alimentos_prato[i + 1])})
                            energ += (float(busca.nutrientes['Energia']) * (float(alimentos_prato[i + 1]))) / 100
                            prot += (float(busca.nutrientes['Proteína']) * float(alimentos_prato[i + 1])) / 100
                            lip += (float(busca.nutrientes['Lipídeos']) * float(alimentos_prato[i + 1])) / 100
                            carbo += (float(busca.nutrientes['Carboidrato']) * float(alimentos_prato[i + 1])) / 100
                            fibra += (float(busca.nutrientes['Fibra']) * float(alimentos_prato[i + 1])) / 100
                            calcio += (float(busca.nutrientes['Cálcio']) * float(alimentos_prato[i + 1])) / 100
                            magne += (float(busca.nutrientes['Magnésio']) * float(alimentos_prato[i + 1])) / 100
                            ferro += (float(busca.nutrientes['Ferro']) * float(alimentos_prato[i + 1])) / 100
                            zinco += (float(busca.nutrientes['Zinco']) * float(alimentos_prato[i + 1])) / 100

                    if i + 2 >= tamanho:
                        break
                    else:
                        i = i + 2

                nutrientes = dict(Energia=energ,
                                  Proteína=prot,
                                  Lipídeos=lip,
                                  Carboidrato=carbo,
                                  Fibra=fibra,
                                  Cálcio=calcio,
                                  Magnésio=magne,
                                  Ferro=ferro,
                                  Zinco=zinco)

                prato = classes.Prato(prat['Valor'], prat['Nome'], prat['Tipo'], prat['Consistência'], dict_alimentos,
                                      nutrientes, prat['Custo'], prat['Cor'])
                aux.append(prato)

    pratos_grupo[key] = aux

refNutricional = dict(Energia=0,
                      Proteína=0,
                      Lipídeos=0,
                      Carboidrato=0,
                      Fibra=0,
                      Cálcio=0,
                      Magnésio=0,
                      Ferro=0,
                      Zinco=0,
                      CustoAluno=0)

with open('referencial.csv', 'r', encoding='utf-8-sig') as ficheiro:
    reader = csv.DictReader(ficheiro, delimiter=';')
    for ref in reader:
        for chave in refNutricional.keys():
            refNutricional[chave] = float(ref[chave]) * 5

tipos_refeicao = list()
desjejum = classes.Refeicao(1, 'Desjejum', ['Lanche', 'Fruta', 'Bebida Láctea'])
tipos_refeicao.append(desjejum)
almoco = classes.Refeicao(2, 'Almoço',
                          ['Acompanhamento Arroz', 'Acompanhamento Feijão', 'Guarnição', 'Principal',
                           'Bebida', 'Sobremesa'])
tipos_refeicao.append(almoco)
lanche = classes.Refeicao(4, 'Lanche', ['Lanche', 'Fruta', 'Bebida'])
tipos_refeicao.append(lanche)
jantar = classes.Refeicao(3, 'Jantar',
                          ['Acompanhamento Arroz', 'Acompanhamento Feijão', 'Guarnição', 'Principal',
                           'Bebida', 'Sobremesa'])
tipos_refeicao.append(jantar)


