import tkinter


# ============================================================
# CRIAÇÃO E CONFIGURAÇÃO DA JANELA PRINCIPAL
# ============================================================
def criar_janela():

    janela = tkinter.Tk()

    # Remove a barra de título padrão do sistema
    janela.overrideredirect(True)

    # Define o tamanho fixo da calculadora
    janela.geometry('350x450')

    # Impede que a janela seja redimensionada
    janela.resizable(False, False)

    # Define o fundo principal da janela
    janela.configure(bg='black')

    # Configuração das colunas e linhas da janela
    janela.columnconfigure(0, weight=1)
    janela.rowconfigure(0, weight=0)
    janela.rowconfigure(1, weight=0)
    janela.rowconfigure(2, weight=1)


    # ========================================================
    # MOVIMENTAÇÃO DA JANELA
    # ========================================================

    # Guarda a posição inicial do mouse ao começar o movimento
    def iniciar_movimento(evento):

        janela.x = evento.x_root
        janela.y = evento.y_root


    # Calcula a nova posição da janela enquanto ela é arrastada
    def mover_janela(evento):

        x = janela.winfo_x() + evento.x_root - janela.x
        y = janela.winfo_y() + evento.y_root - janela.y

        janela.geometry(f'+{x}+{y}')

        janela.x = evento.x_root
        janela.y = evento.y_root


    # Minimiza a janela
    def minimizar_janela():

        # Devolve temporariamente a barra de título do sistema
        janela.overrideredirect(False)

        janela.iconify()


    # ========================================================
    # BARRA DE TÍTULO PERSONALIZADA
    # ========================================================

    barra_titulo = tkinter.Frame(
        janela,
        bg='#080808',
        height=40,
        bd=2,
        relief='raised'
    )

    barra_titulo.grid(
        row=0,
        column=0,
        sticky='ew'
    )

    # Permite arrastar a janela segurando a barra de título
    barra_titulo.bind(
        '<Button-1>',
        iniciar_movimento
    )

    barra_titulo.bind(
        '<B1-Motion>',
        mover_janela
    )


    # ========================================================
    # TÍTULO DA CALCULADORA
    # ========================================================

    titulo = tkinter.Label(
        barra_titulo,
        text='Calculadora',
        bg='#080808',
        fg='#39ff14',
        font=('Courier New', 16, 'bold')
    )

    titulo.pack(
        side='left',
        padx=12
    )

    # Permite arrastar a janela segurando o próprio título
    titulo.bind(
        '<Button-1>',
        iniciar_movimento
    )

    titulo.bind(
        '<B1-Motion>',
        mover_janela
    )


    # ========================================================
    # CONTROLES DA JANELA
    # ========================================================

    controles_janela = tkinter.Frame(
        barra_titulo,
        bg='#080808'
    )

    controles_janela.pack(
        side='right'
    )


    # Botões personalizados de minimizar e fechar
    controles = ['−', '×']


    # Cria os controles automaticamente
    for controle in controles:

        botao = tkinter.Label(
            controles_janela,
            text=controle,
            bg='#080808',
            fg='#39ff14',
            font=('Courier New', 18, 'bold'),
            width=3
        )

        botao.pack(
            side='left'
        )


        # Fecha a calculadora ao clicar no "×"
        if controle == '×':

            botao.bind(
                '<Button-1>',
                lambda evento: janela.destroy()
            )


        # Minimiza a calculadora ao clicar no "−"
        elif controle == '−':

            botao.bind(
                '<Button-1>',
                lambda evento: minimizar_janela()
            )


    # Retorna a janela para ser utilizada pelo main.py
    return janela