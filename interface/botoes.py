import tkinter


# CRIAÇÃO E CONFIGURAÇÃO DOS BOTÕES
def criar_botoes(janela, visor):

    # Adiciona o texto do botão diretamente no visor
    def clicar_botao(texto):

        if texto == 'C':
            visor.delete(0, 'end')
        else:
            visor.insert('end', texto)

    # PERMITE USAR O TECLADO DO COMPUTADOR
    def tecla_pressionada(evento):

        tecla = evento.keysym

        # NÚMEROS
        if tecla in '0123456789':
            clicar_botao(tecla)

        # OPERADORES DO TECLADO
        elif evento.char in '+-/*.':
            clicar_botao(evento.char)

        # ENTER
        elif tecla == 'Return':
            clicar_botao('=')

        # ESC
        elif tecla == 'Escape':
            clicar_botao('C')

        # BACKSPACE
        elif tecla == 'BackSpace':
            if visor.get():
                visor.delete(len(visor.get()) - 1, 'end')

    # CAPTURA AS TECLAS PRESSIONADAS
    janela.bind('<Key>', tecla_pressionada)

    # CRIAÇÃO DA ÁREA DOS BOTÕES
    botoes = tkinter.Frame(
        janela,
        bg='black'
    )

    botoes.grid(
        row=2,
        column=0,
        columnspan=4,
        padx=10,
        pady=10,
        sticky='nsew'
    )

    # CONFIGURAÇÃO DAS COLUNAS
    for coluna in range(4):
        botoes.columnconfigure(
            coluna,
            weight=1,
            uniform='colunas'
        )

    # CONFIGURAÇÃO DAS LINHAS
    for linha in range(5):
        botoes.rowconfigure(
            linha,
            weight=1
        )

    # ESTILO VISUAL DOS BOTÕES
    estilo_botao = {
        'bg': '#080b08',
        'fg': '#39ff14',
        'font': ('Courier New', 18, 'bold'),
        'activebackground': '#123b12',
        'activeforeground': '#39ff14',
        'bd': 3,
        'relief': 'raised',
        'highlightthickness': 1,
        'highlightbackground': '#202820',
        'highlightcolor': '#39ff14'
    }

    # ORGANIZAÇÃO DOS BOTÕES DA CALCULADORA
    botoes_calculadora = [
        ['C', '**', '√', '/'],
        ['7', '8', '9', 'x'],
        ['4', '5', '6', '-'],
        ['1', '2', '3', '+'],
        ['0', '', '.', '=']
    ]

    # CRIA CADA BOTÃO AUTOMATICAMENTE
    for linha, botoes_linha in enumerate(botoes_calculadora):

        for coluna, texto in enumerate(botoes_linha):

            # Ignora posições vazias da grade
            if texto == '':
                continue

            botao = tkinter.Button(
                botoes,
                text=texto,
                command=lambda texto=texto: clicar_botao(texto),
                **estilo_botao
            )

            # O botão 0 ocupa duas colunas
            if texto == '0':
                botao.grid(
                    row=linha,
                    column=coluna,
                    columnspan=2,
                    sticky='nsew',
                    padx=2,
                    pady=2
                )

            # Demais botões ocupam apenas uma coluna
            else:
                botao.grid(
                    row=linha,
                    column=coluna,
                    sticky='nsew',
                    padx=2,
                    pady=2
                )