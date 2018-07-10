import random
from tkinter import *

class Tela(object):

    LARGURA = 800;
    ALTURA = 800;

    status1 = ''
    status2 = ''

    def __init__(self):
        self.root = Tk()
        self.root.geometry('%ix%i' % (self.LARGURA, self.ALTURA))
        self.root.title('Guess Game')
        
        self.renderizaTela()

        self.root.mainloop()


    def getMensagemInstrucao(self):
        return 'O jogador terá de adivinhar em 10 tentativas um número gerado aleatoriamente de 1 a 100'

    def renderizaTela(self):
        self.frame = Frame(pady = 50)
        self.frame.pack();
        self.l = Label(self.frame, text = "Bem vindo ao GuessGame")
        self.l.pack();

        self.frame_instrucoes = Frame(self.frame);
        self.frame_instrucoes.pack()
        self.l2 = Label(self.frame, text = self.getMensagemInstrucao())
        self.l2.pack()

        self.frame_campo = Frame(self.frame);
        self.frame_campo.pack();
        self.l3= Label(self.frame_campo, text= "Qual é o seu palpite?");
        self.l3.pack(side = LEFT);
        self.input_palpite = Entry(self.frame_campo);
        self.input_palpite.pack(side = LEFT);

        self.frame_lista_palpites = Frame(self.frame);
        self.frame_lista_palpites.pack();
        self.l4 = Label(self.frame_lista_palpites, text="Palpites: ");
        self.l4.pack(side =  LEFT);

        self.frame_dica = Frame(self.frame);
        self.frame_dica.pack();
        self.l5 = Label(self.frame_dica, text="Dica: ");
        self.l5.pack(side =  LEFT);




class GuessGame(object):

    def __init__(self):
        
        self.numero_gerado = random.randrange(1, 101);
        self.tentativa = 0;
        self.game_over = False;

    def executarJogada(self, palpite):

    	# Checa se palpite esta valido
    	if(not self.isPalpiteValido(palpite)):
    	    return '';
    	# Checa se palpite é o numero gerado
    	if(palpite == self.numero_gerado):
    	    return 'Parabens!'

    	self.tentativa += 1;


	# Carrega status
    # 	if self.tentativa == 1:
    #        self.status1 = ''
    #        self.status2 = self.SetStatus(palpite)
    #     else:
    #        self.status1 = self.status2
    #        self.status2 = self.SetStatus(palpite)
	    
    # # Retorna mensagem da pista
	   # return self.FornecerPista(self.status1, self.status2)



    def isPalpiteValido(self, palpite):
        try:
            self.palpite = int(palpite)
            if (self.palpite < 1) or (self.palpite > 100):
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

#
# apresentar jogo ao usuário
#
# print('Você tem 10 chances de acertar o número que eu estou pensando.')
# print('Trata-se de um valor entre 1 e 100. Então, vamos lá!')
# print()

#
# repetir 10 vezes:
#
# for tentativa in range(1,11):
# #   ler e validar palpite
    
# #   testar palpite
#     if palpite == n:
#         acertou = True
#         break
# #   determinar status do palpite
#     if tentativa == 1:
#         status1 = ''
#         status2 = SetStatus(n, palpite)
#     else:
#         status1 = status2
#         status2 = SetStatus(n, palpite)
# #   fornecer pista ao jogador
#     FornecerPista(status1, status2)
# # comunicar resultado ao usuário
# if acertou:
#     print('\nParabéns !')
#     print('\nVocê acertou o número ', n, ' após ', tentativa, ' tentativa(s) !!!')
#     print('\n\nAté mais !!')
# else:
#     print('\nLamento, mas após ', tentativa, ' tentativas, você não conseguiu acertar o número ', n, ' que eu estava pensando !!!')
#     print('\n\nAté mais !!')
