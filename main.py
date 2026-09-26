import tkinter

from interface.janela import criar_janela
from interface.visor import criar_visor
from interface.botoes import criar_botoes

janela = criar_janela()
visor = criar_visor(janela)
criar_botoes(janela, visor)

janela.mainloop()