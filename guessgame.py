import random
from tkinter import *
from PIL import Image, ImageTk

class Tela(object):

    LARGURA = 562;
    ALTURA = 430;

    status1 = ''
    status2 = ''

    color_bg = '#879BDD'
    color_enfasis = '#425AA8'
    color_text= 'white'

    def __init__(self):
        self.root = Tk()
        self.root.geometry('%ix%i' % (self.LARGURA, self.ALTURA))
        self.root.title('Guess Game')
        
        self.guessgame = GuessGame()

        # Foto do guessgame
        temp_image = Image.open('banner.png')
        temp_image = temp_image.resize((558, 140), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(temp_image)
        
        self.renderizaTela()

        self.root.mainloop()


    def getMensagemInstrucao(self):
        return 'O jogador terá de adivinhar em 10 tentativas um número gerado aleatoriamente de 1 a 100'

    def renderizaTela(self):
        self.frame = Frame(pady = 50, bg=self.color_bg)
        self.frame.pack();
        self.l = Label(self.frame, text = "Bem vindo ao GuessGame",
                       font=("Arial", 30), pady=40, bg=self.color_bg,
                       fg=self.color_text, padx=30, image=self.photo)
        self.l.pack();

        # Instrucoes
        self.frame_instrucoes = Frame(self.frame);
        self.frame_instrucoes.pack()
        self.l2 = Label(self.frame, text = self.getMensagemInstrucao(),
                        pady=10, bg=self.color_bg, fg=self.color_text)
        self.l2.pack()

        # Palpites
        self.frame_campo = Frame(self.frame, bg=self.color_bg);
        self.frame_campo.pack();
        self.l3= Label(self.frame_campo, text= "Qual é o seu palpite?", bg=self.color_bg, fg=self.color_text);
        self.l3.pack(side = LEFT);
        self.input_palpite = Entry(self.frame_campo, bg='#B9BAF1');
        self.input_palpite.pack(side = LEFT, padx=10);
        self.input_palpite.focus()
        self.b = Button(self.frame_campo, text="Dar Palpite", command = self.darPalpite,
                        bg=self.color_enfasis, font=("Arial", 8, 'bold'), fg='white')
        self.b.pack(side= LEFT)
        self.b2 = Button(self.frame_campo, text='Jogar Novamente', command = self.reiniciarJogo,
                         bg=self.color_enfasis, font=("Arial", 8, 'bold'), fg='white')

        # Tentativas
        self.frame_tentativas = Frame(self.frame);
        self.frame_tentativas.pack();
        self.label_tentativa = Label(self.frame_tentativas, text='Tentativas:', bg=self.color_bg, fg=self.color_text)
        self.label_numero_tentativa = Label(self.frame_tentativas, text='0', bg=self.color_bg, fg=self.color_text)
        self.label_tentativa.pack(side = LEFT);
        self.label_numero_tentativa.pack(side = LEFT);

        # Lista de palpites
        self.frame_lista_palpites = Frame(self.frame);
        self.frame_lista_palpites.pack();
        self.l4 = Label(self.frame_lista_palpites, text="Palpites: ", bg=self.color_bg, fg=self.color_text);
        self.l4.pack(side =  LEFT);
        self.label_palpites = Label(self.frame_lista_palpites, text='', bg=self.color_bg, fg=self.color_text)
        self.label_palpites.pack()
        
        # Dicas
        self.frame_dica = Frame(self.frame, width=100, bg=self.color_bg);
        self.frame_dica.pack();
        self.l5 = Label(self.frame_dica, text="Dica: ", bg=self.color_bg, fg=self.color_text, pady=10);
        self.l5.pack(side =  LEFT);
        self.label_dica = Label(self.frame_dica, bg=self.color_bg, font=("Arial", 12, 'bold'),fg='#F8C34E')
        self.label_dica.pack(side = LEFT)

        # Numero Gerado
        self.frame_numero = Frame(self.frame, bg=self.color_bg, heigh=40);
        self.frame_numero.pack();
        self.l6 = Label(self.frame_numero, text="Numero gerado: ", bg=self.color_bg, fg=self.color_text )
        self.l7 = Label(self.frame_numero, text="", bg=self.color_bg, font=("Arial", 12, 'bold'),fg='#F8C34E' )

    def darPalpite(self):
        
        dica = self.guessgame.getDica(self.input_palpite.get())

        # Atualiza as Labels das dicas, palpites e tentativas
        self.label_dica['text'] = dica
        self.label_numero_tentativa['text'] = self.guessgame.tentativa
        self.label_palpites['text'] = self.guessgame.palpites

        # Apaga o que está escrito no Entry palpite
        self.input_palpite.delete(0, len(self.input_palpite.get()))

        if(self.guessgame.game_over):
            self.acabaJogo()

    def acabaJogo(self):

        # Desabilita o botão do palpite, apaga botao de palpite e mostra botão de jogar novamente.
        self.input_palpite['state'] = DISABLED
        self.b.forget()
        self.b2.pack()

        # Mostra o numero gerado pelo computador
        self.l6.pack()
        self.l7['text'] = self.guessgame.getNumeroGerado()
        self.l7.pack()

    def reiniciarJogo(self):
        del self.guessgame
        self.guessgame = GuessGame()
        self.b.pack()
        self.b2.forget()
        self.l6.forget()
        self.l7.forget()
        self.input_palpite['state'] = NORMAL
        self.label_dica['text'] = ''
        self.label_numero_tentativa['text'] = 0
        self.label_palpites['text'] = ''


class GuessGame(object):

    def __init__(self):
        
        self.numero_gerado = random.randrange(1, 101);
        self.tentativa = 0;
        self.game_over = False;
        self.palpites = []

    def getNumeroGerado(self):
        return self.numero_gerado

    def getDica(self, palpite):
        
        # Checa se palpite esta valido
        if not self.isPalpiteValido(palpite):
            return 'Palpite inválido, por favor digite novamente';

        palpite = int(palpite)

        self.tentativa += 1;
        self.palpites.append(palpite)
        
        # Checa se palpite é o numero gerado
        if(palpite == self.numero_gerado):
            self.game_over = True;
            return 'Parabens!'

        if(self.tentativa == 10):
            self.game_over = True
            return 'Infelizmente você perdeu! Mas não desanime, jogue novamente!'
        
        
	# Carrega status
        if self.tentativa == 1:
            self.status1 = ''
            self.status2 = self.SetStatus(palpite)
        else:
            self.status1 = self.status2
            self.status2 = self.SetStatus(palpite)
            
        # Retorna mensagem da pista
        return self.FornecerPista(self.status1, self.status2)


    def isPalpiteValido(self, palpite):
        try:
            self.palpite = int(palpite)
            if (self.palpite < 1) or (self.palpite > 100) or (self.palpite in self.palpites):
                raise ValueError
        except ValueError:
            return False;

        return True;
        

    def SetStatus(self, palpite):
        'Determina e seta o status de cada palpite'
        dif = abs(self.numero_gerado-palpite)
        if dif <= 3:
            status = 'MQ'
        elif dif >= 4 and dif <= 6:
            status = 'QT'
        elif dif >= 7 and dif <= 9:
            status = 'FR'
        else:
            status = 'MF'
        return status
            
    def FornecerPista(self,st1, st2):
        'Gera a pista a ser dada ao usuário'
        mensagem = ''
        if st1 == '':
            # Fornecer primeira pista
            if st2 == 'MQ':
                mensagem = 'Seu palpite está muito quente!';
            elif st2 == 'QT':
                mensagem = 'Seu palpite está quente!'
            elif st2 == 'FR':
                mensagem = 'Seu palpite está frio!'
            else:
                mensagem = 'Seu palpite está muito frio!'
        else:
            # Fornecer pista
            if st1 == 'MQ':
                if st2 == 'MQ':
                    mensagem = 'Seu palpite continua muito quente!'
                elif st2 == 'QT':
                    mensagem = 'OOps, seu palpite deu uma esfriada mas ainda está quente!'
                elif st2 == 'FR':
                    mensagem = 'OOps, seu palpite agora ficou frio!'
                else:
                    mensagem = 'OOps, seu palpite agora ficou muito frio!'
            elif st1 == 'QT':
                if st2 == 'MQ':
                    mensagem = 'OOps, seu palpite deu uma esquentada e agora está muito quente!'
                elif st2 == 'QT':
                    mensagem = 'Seu palpite continua quente!'
                elif st2 == 'FR':
                    mensagem = 'OOps, seu palpite deu uma esfriada e agora ficou frio!'
                else:
                    print('OOps, seu palpite deu uma esfriada e agora ficou muito frio!')
            elif st1 == 'FR':
                if st2 == 'MQ':
                    mensagem = 'OOps, seu palpite deu uma esquentada e agora está muito quente!'
                elif st2 == 'QT':
                    mensagem = 'Seu palpite deu uma esquentada e agora está quente!'
                elif st2 == 'FR':
                    mensagem = 'OOps, seu palpite continua frio!'
                else:
                    mensagem = 'OOps, seu palpite deu uma esfriada e agora ficou muito frio!'
            else:
                if st2 == 'MQ':
                    mensagem = 'OOps, seu palpite deu uma esquentada e agora está muito quente!'
                elif st2 == 'QT':
                    mensagem = 'Seu palpite deu uma esquentada e agora está quente!'
                elif st2 == 'FR':
                    mensagem = 'OOps, seu palpite deu uma esquentadinha mas ainda está frio!'
                else:
                    mensagem = 'Seu palpite continua muito frio!'
        return mensagem

Tela()
