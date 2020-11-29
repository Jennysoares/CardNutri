import timeit
import algoritmoGenetico as ag
from tkinter import *
from tkinter import ttk
import tkinter as tk
from threading import Thread
import base_dados as bd


def gerarCardapio():
    total_dias = 5
    populacao = list()
    taxa_mutacao = 0.05
    taxa_cruzamento = 0.8
    nInd = 50

    for i in range(0, nInd):
        populacao.append(ag.ini_populacao(total_dias, 0))

    geracao_atual = populacao
    fitness = ag.funcao_fitness(geracao_atual, 2)
    print(f'Fitness geração inicial = {fitness}')
    custo = dict()
    indices = 0
    while True:
        custo.update({round(ag.calcularCusto(geracao_atual[indices]), 2): indices})
        indices += 1
        if indices == nInd:
            break

    print(f'Custo gerção inicial = {custo}')

    for i in range(0, 500):

        fitness = ag.funcao_fitness(geracao_atual, 1)
        corte_populacao = ag.funcao_dizimacao_corte(geracao_atual, fitness)

        nova_populacao = []
        for k in range(0, int(nInd / 2)):
            pais = ag.funcao_dizimacao_pais(corte_populacao)
            filhos_gerados = ag.cruzamento(pais, taxa_cruzamento)
            filhos_mutados = ag.mutacao(filhos_gerados, taxa_mutacao)
            nova_populacao.append(filhos_mutados[0])
            nova_populacao.append(filhos_mutados[1])

        geracao_atual = nova_populacao

    return geracao_atual


def mostrarAlimentos(cardapTodo, ref):
    alimentosPage = Tk()
    alimentosPage.title("Alimentos dos Pratos")
    alimentosPage.geometry("450x400+300+200")
    alimentosPage.wm_resizable(width=False, height=False)

    cTableContainer = tk.Canvas(alimentosPage)
    fTable = tk.Frame(cTableContainer)

    sbHorizontalScrollBar = tk.Scrollbar(alimentosPage)
    sbVerticalScrollBar = tk.Scrollbar(alimentosPage)

    cTableContainer.config(xscrollcommand=sbHorizontalScrollBar.set, yscrollcommand=sbVerticalScrollBar.set,
                           highlightthickness=0)
    sbHorizontalScrollBar.config(orient=tk.HORIZONTAL, command=cTableContainer.xview)
    sbVerticalScrollBar.config(orient=tk.VERTICAL, command=cTableContainer.yview)

    sbHorizontalScrollBar.pack(fill=tk.X, side=tk.BOTTOM, expand=tk.FALSE)
    sbVerticalScrollBar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
    cTableContainer.pack(fill=tk.BOTH, side=tk.LEFT, expand=tk.TRUE)
    cTableContainer.create_window(0, 0, window=fTable, anchor=tk.NW)

    nutri = list(bd.nutrientes.keys())
    linha = 0
    coluna = 0

    for prato in cardapTodo[ref]:
        if len(prato.alimentos) > 0:
            Label(fTable, text=f"{prato.nome}", bg="gray", fg="black", font="Arial 10 bold", padx=3, pady=3).grid(
                row=linha,
                column=coluna, stick="nsew", padx=1, pady=1)
            fTable.grid_columnconfigure(coluna, weight=1)
            for nutriente in nutri:
                coluna += 1
                Label(fTable, text=f"{nutriente}", bg="white", fg="black", font="Arial 10 bold", padx=3,
                      pady=3).grid(row=linha, column=coluna, stick="nsew", padx=1, pady=1)
                fTable.grid_columnconfigure(coluna, weight=1)

            for alimentos in prato.alimentos:
                linha += 1
                coluna = 0
                Label(fTable, text=f"{alimentos.nome}", bg="white", fg="black", font="Arial 10 bold",
                      padx=3, pady=3).grid(row=linha, column=coluna, stick="nsew", padx=1, pady=1)
                fTable.grid_columnconfigure(coluna, weight=1)
                for key in alimentos.nutrientes:
                    coluna += 1
                    Label(fTable, text=f"{alimentos.nutrientes[key]}", bg="white", fg="black", font="Arial 10 bold",
                          padx=3, pady=3).grid(row=linha, column=coluna, stick="nsew", padx=1, pady=1)
                    fTable.grid_columnconfigure(coluna, weight=1)

            linha += 1
            coluna = 0
            cTableContainer.update_idletasks()
            cTableContainer.config(scrollregion=fTable.bbox())

    alimentosPage.mainloop()


def mostrarCardapio():
    progressbar.start()
    inicio = timeit.default_timer()
    cardapio = gerarCardapio()

    fitness = ag.funcao_fitness(cardapio, 2)
    menu.after(20, progressbar.stop())

    print(f'\nFitness cardapio final: {fitness}')
    telaCardapios = Tk()
    telaCardapios.configure(background="black")
    telaCardapios.title("Cardápios Gerados")
    telaCardapios.iconbitmap(default="menu.ico")
    telaCardapios.geometry("1088x600+200+100")
    telaCardapios.wm_resizable(width=False, height=False)

    novo_cardapio = 0

    mainframe = Frame(telaCardapios)
    mainframe.pack(fill=BOTH, expand=1)
    my_canvas = Canvas(mainframe)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    myscrollbar = ttk.Scrollbar(mainframe, orient=VERTICAL, command=my_canvas.yview)
    myscrollbar.pack(side=RIGHT, fill=Y)
    my_canvas.configure(yscrollcommand=myscrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame = Frame(my_canvas)
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
    second_frame.configure(background='#E7DDE0')

    for cardapioIndices in fitness.values():

        cabecalho_cardapio = novo_cardapio + 1
        cabecalho_cardapioColunas = 0
        countDia = 0
        custo = ag.calcularCusto(cardapio[cardapioIndices])

        Label(second_frame, text=f"Cardápio {cardapioIndices}", width="162", height="3", font="Arial 8 bold",
              borderwidth=1, relief="solid", background="#EA6B66", foreground="white").grid(row=novo_cardapio,
                                                                                            columnspan=10, sticky="w")

        Label(second_frame, text=f"Custo = {round(custo, 2)}", width="12", height="2", font="Arial 10 bold",
              borderwidth=1, relief="solid", background="#F8CECC").grid(row=cabecalho_cardapio,
                                                                        column=cabecalho_cardapioColunas, sticky="w")
        for refeicao in cardapio[1][0]:
            cabecalho_cardapioColunas += 1
            Label(second_frame, text=f"{refeicao}", width="28", height="2", font="Arial 10 bold", fg="black",
                  borderwidth=1, relief="solid", background="#F5F5F5").grid(row=cabecalho_cardapio, sticky="w",
                                                                            column=cabecalho_cardapioColunas)
        for cardapiosDia in cardapio[cardapioIndices]:
            cabecalho_cardapio += 1
            colunaRefeicao = 0
            countDia += 1
            Label(second_frame, text=f"Dia {countDia}", width="12", height="4", font="Arial 10 bold", borderwidth=1,
                  relief="solid", background="#F5F5F5").grid(row=cabecalho_cardapio, column=0, sticky="w")

            for refeicao in cardapiosDia:
                colunaRefeicao += 1

                if refeicao == 'Lanche' or refeicao == 'Desjejum':
                    cor = '#FFCCCC'
                    fonte = 'black'
                else:
                    cor = '#FF9999'
                    fonte = 'black'

                labeL_pratos = Label(second_frame, text='\n'.join(str(x.nome) for x in cardapiosDia[refeicao]),
                                     width="31", height="6", font="Arial 8 bold", borderwidth=1, relief="solid",
                                     background=cor, foreground=fonte)
                labeL_pratos.grid(row=cabecalho_cardapio, column=colunaRefeicao, padx=(5, 5), sticky="w")
                labeL_pratos.bind("<Button-1>",
                                  lambda e, card=cardapiosDia, refei=refeicao: mostrarAlimentos(card, refei))
        Label(second_frame, text="", width="31", height="1", font="Arial 8 bold", borderwidth=1,
              background="#E7DDE0").grid(row=cabecalho_cardapio + 1, column=0, columnspan=4, padx=(5, 5), sticky="w")

        novo_cardapio = cabecalho_cardapio + 2
    fim = timeit.default_timer()
    print(f'\nTempo de execução: {fim - inicio}')
    telaCardapios.mainloop()


menu = Tk()
menu.title("Cardápios Nutricionais")
menu.iconbitmap(default="menu.ico")
menu.geometry("450x300+500+200")
menu.wm_resizable(width=False, height=False)
imgMenu = PhotoImage(file="menuFundo.png")
fundoMenu = Label(menu, image=imgMenu)
fundoMenu.place(x=0, y=0)
progressbar = ttk.Progressbar(menu, mode="indeterminate")
progressbar.place(x=142, y=205, width=200)
btGerarCardapio = Button(menu, text="Gerar Cardápio", width=15, height=2,
                         command=lambda: [Thread(target=mostrarCardapio).start()])
btGerarCardapio.place(x=183, y=137)
Label(menu, text="Clique no botão acima para gerar sugestões de cardápios escolares para período \n"
                 "integral com o menor erro nutricional e custo possível.",
      background="black", foreground="white").place(x=10, y=249)

menu.mainloop()
