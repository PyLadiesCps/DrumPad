from Tkinter import *
from sound_panel import *
import pygame.mixer
import os

#inicia a aplicação gráfica
app = Tk()
app.title('DrumPad PyLadies')

#http://www.pygame.org/docs/ref/mixer.html
#inicia a parte de sons do pygame
mixer = pygame.mixer
mixer.init()

#pega o diretório atual (.)
files = os.listdir(".")

#inicia um SoundPanel para todos os arquivos terminados em .aif
for fname in files:
    if fname.endswith('.aif'):
        SoundPanel(app, mixer, fname).pack()

#função que encerra a aplicação
def termina():
    mixer.stop()
    app.destroy()

#define que quando clicado no X, chama a função acima
app.protocol('WM_DELETE_WINDOW', termina)

#inicia execução
app.mainloop()
