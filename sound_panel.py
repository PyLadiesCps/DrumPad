from Tkinter import *
import pygame.mixer

class SoundPanel(Frame):

    def on_off(self):
        if self.tocando.get():
            #loops -1 = tocar pra sempre
            self.track.play(loops = -1)
        else:
            self.track.stop()

    def muda_volume(self, v):
        self.track.set_volume(self.volume.get())

    def __init__(self, app, mixer, sound_file):
        Frame.__init__(self, app)

        #http://www.pygame.org/docs/ref/mixer.html#pygame.mixer.Sound
        #cria um objeto de som, preferencialmente OGG ou WAV. suporte MP3 limitado
        self.track = mixer.Sound(sound_file)

        #cria uma variavel numerica pra ser setada no botao
        self.tocando = IntVar()

        #cria um botao de check pra definir on_off
        botaoTocar = Checkbutton(self, variable = self.tocando,
                            command = self.on_off,
                            text = sound_file)
        #posiciona o botao na tela
        botaoTocar.pack(side = RIGHT)

        #cria uma variavel numerica pra armazenar volume
        self.volume = DoubleVar()
        #define ela como o volume da faixa
        self.volume.set(self.track.get_volume())

        #cria um botao de escala pra definir volume
        escala = Scale(self, variable = self.volume,
            from_ = 0.0, to = 1.0, resolution = 0.1,
            command = self.muda_volume,
            label = 'Volume', orient = HORIZONTAL)
        #posiciona o botao na tela
        escala.pack(side = RIGHT)

