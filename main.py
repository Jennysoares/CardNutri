import algoritmoGenetico as ag
from tkinter import *
from tkinter import ttk
from threading import Thread


def mouseBtnEsquerdo(evento):
    print(f'x: {str(evento.x)}, y: {str(evento.y)}')


def gerarCardapio():
    total_dias = 5
    populacao = list()
    taxa_mutacao = 0.05
    taxa_cruzamento = 0.8
    nInd = 50
    for i in range(0, nInd):
        populacao.append(ag.ini_populacao(total_dias, 0))

    geracao_atual = populacao
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


def mostrarCardapio():
    global imgTelaCardapios

    progressbar.start()
    cardapio = gerarCardapio()
    fitness = ag.funcao_fitness(cardapio, 2)
    menu.after(20, progressbar.stop())

    print(fitness)
    telaCardapios = Tk()
    telaCardapios.configure(background="black")
    telaCardapios.title("Cardápios Gerados")
    telaCardapios.iconbitmap(default="menu.ico")
    telaCardapios.geometry("1088x600+100+100")
    telaCardapios.wm_resizable(width=False, height=False)
    # imgTelaCardapios = PhotoImage(file="gift_page_landing_bg_Mobile_Image.png")
    # fundotelaCardapios = Label(telaCardapios, image=imgTelaCardapios)
    # fundotelaCardapios.place(x=0, y=0)

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
    second_frame.configure(background='MistyRose2')


    for cardapioIndices in fitness.values():

        cabecalho_cardapio = novo_cardapio + 1
        cabecalho_cardapioColunas = 0
        countDia = 0
        custo = ag.calcularCusto(cardapio[cardapioIndices])

        Label(second_frame, text=f"Cardápio {cardapioIndices}", width="162", height="3", font="Arial 8 bold",
              borderwidth=2, relief="groove", background="MistyRose3", foreground="white").grid(row=novo_cardapio, columnspan=10, sticky="w")
        Label(second_frame, text=f"Custo = {round(custo, 2)}", width="12", height="2", font="Arial 10 bold",
              borderwidth=2, relief="groove", background="thistle4", foreground="white").grid(row=cabecalho_cardapio, column=cabecalho_cardapioColunas, sticky="w")
        for refeicao in cardapio[1][0]:
            cabecalho_cardapioColunas += 1
            Label(second_frame, text=f"{refeicao}", width="28", height="2", font="Arial 10 bold", fg="black",
                  borderwidth=2, relief="groove", background="PeachPuff2").grid(row=cabecalho_cardapio, column=cabecalho_cardapioColunas, sticky="w")
        for cardapiosDia in cardapio[cardapioIndices]:
            cabecalho_cardapio += 1
            colunaRefeicao = 0
            countDia += 1
            Label(second_frame, text=f"Dia {countDia}", width="12", height="4", font="Arial 10 bold", borderwidth=2,
                  relief="groove", background="MistyRose3").grid(row=cabecalho_cardapio, column=0, sticky="w")
            for refeicao in cardapiosDia:
                colunaRefeicao += 1

                if refeicao == 'Lanche' or refeicao == 'Desjejum':
                    cor = 'lavender blush'
                else:
                    cor = 'LavenderBlush2'

                Label(second_frame, text='\n'.join(str(x.nome) for x in cardapiosDia[refeicao]), width="31", height="6",
                      font="Arial 8 bold", borderwidth=2, relief="groove", background=cor).grid(row=cabecalho_cardapio,
                                                                                column=colunaRefeicao, padx=(5, 5),

                                                                                sticky="w")
        Label(second_frame, text="", width="31", height="1",
              font="Arial 8 bold", borderwidth=2, background="MistyRose2").grid(row=cabecalho_cardapio+1,
                                                                                column=0, columnspan=4, padx=(5, 5),
                                                                                sticky="w")
        novo_cardapio = cabecalho_cardapio + 2
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
progressbar.place(x=135, y=249, width=200)
btGerarCardapio = Button(menu, text="Gerar Cardápio", width=15, height=2,
                         command=lambda: [Thread(target=mostrarCardapio).start()])
btGerarCardapio.place(x=182, y=174)

menu.bind('<Button-1>', mouseBtnEsquerdo)

menu.mainloop()

# geracao_atual = gerarCardapio()
# fitness = ag.funcao_fitness(geracao_atual)
# print(fitness)
# cardap = 0
# for cardapio in geracao_atual:
#    cont = 0
#    cardap += 1
#    print('\n====== Cardapio {} ======'.format(cardap))
#    custo = ag.calcularCusto(cardapio)
#    custo = round(custo, 2)
#    print(f'Custo = {custo}')
#    for cardapiodia in cardapio:
#        cont += 1
#        print('\n=* Dia {} =*'.format(cont))
#        for refeicao in cardapiodia:
#            print(f' - {refeicao} -> ', end='')
#            for prato in cardapiodia[refeicao]:
#                print(f'{prato.nome}, ', end='')
#            print()
