import tkinter


# CRIAÇÃO E CONFIGURAÇÃO DO VISOR
def criar_visor(janela):

    # Moldura externa do visor
    moldura_visor = tkinter.Frame(
        janela,
        bg='#080808',
        bd=3,
        relief='sunken',
        highlightthickness=2,
        highlightbackground='#151515'
    )

    moldura_visor.grid(
        row=1,
        column=0,
        columnspan=4,
        padx=12,
        pady=8,
        sticky='nsew'
    )

    # Permite que o visor ocupe todo o espaço disponível
    moldura_visor.columnconfigure(0, weight=1)
    moldura_visor.rowconfigure(0, weight=1)

    # Campo onde os números e operações serão exibidos
    visor = tkinter.Entry(
        moldura_visor,
        bg='#061006',
        fg='#39ff14',
        font=('Courier New', 22, 'bold'),
        bd=0,
        relief='flat',
        justify='right'
    )

    visor.grid(
        row=0,
        column=0,
        sticky='nsew',
        padx=5,
        pady=5
    )

    return visor