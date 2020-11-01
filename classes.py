import random
import base_dados as bd

class Alimento:
    def __init__(self, id, nome, valor, nutrientes, grupo):
        self.id = id
        self.nome = nome
        self.valor = valor
        self.nutrientes = nutrientes
        self.grupo = grupo

class Prato:
    def __init__(self, id, nome, tipo, consistencia, alimentos, nutrientesTotal, preco, cor):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.consistencia = consistencia
        self.alimentos = alimentos
        self.nutrientesTotal = nutrientesTotal
        self.cor = cor
        self.preco = preco

class Refeicao:
    def __init__(self, id, nome, composicao):
        self.id = id
        self.nome = nome
        self.composicao = composicao

    def gerar_cardapio(self):
        pratos = list()

        for composicao in self.composicao:

            if composicao in bd.pratos_grupo.keys():
                escolha = random.choice(bd.pratos_grupo[composicao])
                pratos.append(escolha)

        return pratos



