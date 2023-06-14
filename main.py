import pygame
import pygame.gfxdraw
from pygame.locals import *
from random import randint
import constant
import os
import sprites


class Game:
    def __init__(self):
        #Cria tela do jogo
        pygame.init()
        self.tela = pygame.display.set_mode((constant.LARGURA, constant.ALTURA))
        pygame.display.set_caption(constant.TITULO)
        self.relogio = pygame.time.Clock()
        self.is_running = True
        self.font = pygame.font.match_font(constant.FONTE)
        self.fase = 0
        self.cont = 0
        self.cont_text = 0
        self.vidaV = 0
        self.pos = 0
        self.key = True
        self.write_text = []
        self.pergunta = []
        self.resposta = []
        self.question = True
        self.upload_files()

    def new_game(self):
        #instancia as classes das sprites do jogo
        self.answers = ['', '', '', '', '']
        self.sprites = pygame.sprite.Group()
        self.mago = sprites.mago
        self.aprendiz = sprites.aprendiz
        self.sprites.add(self.mago)
        self.sprites.add(self.aprendiz)
        self.mago.fase = 0
        self.aprendiz.fase = 0
        self.sort_question()
        self.text()
        self.intro()
        self.run()

    def run(self):
        #loop do jogo
        self.play = True
        while self.play:
            self.relogio.tick(constant.FPS)
            self.draw_sprites()
            self.events()
            self.is_phase()
            self.update_sprites()

    def events(self):
        #define os eventos do jogo
        move = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.play:
                    self.play = False
                self.is_running = False

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.play = False
                    self.is_running = False

        if pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT]:
            move = 1
            if self.aprendiz.collide_right() == False:
                    self.next_phase()

        if pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT]:
            move = 2
        self.mago.move(move, 1)
        self.aprendiz.move(move, 0)

    def update_sprites(self):
        #atualizar sprites
        self.sprites.update()

    def draw_sprites(self):
        #desenhar sprites
        '''self.tela.fill(constant.PRETO) #limpa a tela'''
        self.background(constant.LARGURA / 2, 0)
        self.vidas()
        if self.fase not in constant.FASES_I:
            if constant.APRENDIZ_POS < 800 and self.key:
                self.text_box()
            elif constant.APRENDIZ_POS > 800 and self.key:
                self.key = False
                self.cont_text += 4

        if self.aprendiz.collide_right() == False and self.fase in constant.FASES_I:
            if self.question:
                self.answers = ['', '', '', '']
                for i in range(len(self.answers)):
                    j = randint(3, 75)
                    j = str(j)
                    while True:
                        if j in self.answers or j == self.resposta[self.pos]:
                            j = randint(3, 75)
                            j = str(j)
                        else:
                            break
                    self.answers[i] = j
                if self.fase == 8:
                    for i in range(len(self.answers)):
                        aux = int(self.answers[i])
                        if aux % 2 != 0:
                            aux += 1
                            aux = str(aux)
                            while True:
                                if aux in self.answers or aux == self.resposta[self.pos]:
                                    aux = int(aux)
                                    aux += 2
                                    aux = str(aux)
                                else:
                                    break
                        aux = str(aux)
                        self.answers[i] = aux
                if self.fase == 10:
                    for i in range(len(self.answers)):
                        aux = randint(950, 2500)
                        if aux % 2 == 0:
                            aux += 1
                            aux = str(aux)
                            while True:
                                if aux in self.answers or aux == self.resposta[self.pos]:
                                    aux = int(aux)
                                    aux += 2
                                    aux = str(aux)
                                else:
                                    break
                        aux = str(aux)
                        self.answers[i] = aux
                i = randint(0, 3)
                self.answers[i] = self.resposta[self.pos]
                self.question = False

            if self.question == False:
                self.question_box()
        if self.pos < 8:
            self.sprites.draw(self.tela) #desenha
            pygame.display.update()  # atualiza a tela a cada frame

    def upload_files(self):
        #carragar os arquivos de audios e imagens
        diretorio_imagens = os.path.join(os.getcwd(), 'imagens')
        #self.spritesheet = os.path.join(diretorio_imagens, constant.BACKGROUND_IMAGES[2])
        self.logo_start_string = os.path.join(diretorio_imagens, constant.LOGO_MENU) #retorna um valor em string
        self.logo_start = pygame.image.load(self.logo_start_string).convert()  # converte de string para imagem
        self.winner_string = os.path.join(diretorio_imagens, constant.WINNER)
        self.winner_img = pygame.image.load(self.winner_string).convert()

        self.vida = []
        for i in range(4):
            self.vida_string = os.path.join(diretorio_imagens, constant.VIDAS[i])
            self.vida.append(pygame.image.load(self.vida_string).convert_alpha())
            self.vida[i] = pygame.transform.scale(self.vida[i], (130, 60))

        self.paginas = []
        for i in range(3):
            self.paginas_string = os.path.join(diretorio_imagens, constant.PAGINAS_IMAGES[i])
            self.paginas.append(pygame.image.load(self.paginas_string).convert())

        self.background_image = []
        for i in range(13):
            self.background_string = os.path.join(diretorio_imagens, constant.BACKGROUND_IMAGES[i])
            self.background_image.append(pygame.image.load(self.background_string).convert())

    def text(self):
        self.write_text.append('E assim começa a aventura de Merlin e seu aprendiz')
        self.write_text.append('Partindo da ilha da Esmeralda, eles irão se aventurar')
        self.write_text.append('para recuperar os poderes de Merlin')
        self.write_text.append('e derrotar o mago do mal, Baltazar!!')

        self.write_text.append('Algum tempo se passa até chegarem à uma cidade que nunca')
        self.write_text.append('haviam visto, com contruções altas e brilhantes')
        self.write_text.append('mas não parecia haver vestígios de Baltazar naquela região')
        self.write_text.append('então eles decidem continuar sua Viagem')

        self.write_text.append('Após conseguirem desfazer o selo da porta, eles entram')
        self.write_text.append('na antiga taverna, e ao longe se deparam com ingrediente')
        self.write_text.append('em cima do balcão, e parece ser uma das poções necessárias')
        self.write_text.append('para recuperar os poderes do mago')

        self.write_text.append('Após ajudarem o fazendeiro ele lhes entregou um ingrediente')
        self.write_text.append('e passou informações. Informações essas que te levaram')
        self.write_text.append('até a entrada de uma caverna')
        self.write_text.append('')

        self.write_text.append('Com a escolha correta, Merlin e seu aprendiz conseguem')
        self.write_text.append('adentrar o labirinto com sucesso e continuam o caminho')
        self.write_text.append('para sua jornada, onde sentem seu objetivo próximo')
        self.write_text.append('')

        self.write_text.append('Após a vitória sobre o aprendiz de Baltazar')
        self.write_text.append('vocês encontram um grande castelo que pertence à')
        self.write_text.append('Baltazar. O seu objetivo está logo a frente')
        self.write_text.append('')

    def sort_question(self):
        resp = 0
        i = randint(1, 25)
        j = randint(1, 25)
        k = randint(1, 25)
        resp = i + j + k
        resp = str(resp)
        self.resposta.append(resp)
        i = str(i)
        j = str(j)
        k = str(k)
        self.pergunta.append(f'Na parede ao lado existe, {i} Quadros vermelhos, {j} Quadros brancos, {k} ')
        self.pergunta.append('Quadros azuis, ao total possui quantos quadros?')
        self.pergunta.append('')
        self.pergunta.append(f'{i} + {j} + {k}= ?')

        i = randint(40, 100)
        j = randint(1, 40)
        resp = i - j
        resp = str(resp)
        self.resposta.append(resp)
        i = str(i)
        j = str(j)
        self.pergunta.append(f'No dia anterior o fazendeiro possuía {i} ovelhas, e agora tem apenas {j}. ')
        self.pergunta.append('Quantas ovelhas desapareceram?')
        self.pergunta.append('')
        self.pergunta.append(f'{i} - {j}= ?')

        i = randint(2, 15)
        j = randint(1, 10)
        resp = i * j
        resp = str(resp)
        self.resposta.append(resp)
        i = str(i)
        j = str(j)
        self.pergunta.append(f'Seria preciso utilizar {i} de pernas de aranha ')
        self.pergunta.append(f'multiplicado por {j} de elixir misterioso para efetuar a magia')
        self.pergunta.append('')
        self.pergunta.append(f'{i} x {j}= ?')

        i = randint(4, 30)
        if i % 2 != 0:
            i += 1
        j = 2
        resp = i / j
        resp = int(resp)
        resp = str(resp)
        self.resposta.append(resp)
        i = str(i)
        j = str(j)

        self.pergunta.append('O aprendiz invocou uma magia que me deixou paralisado, para me')
        self.pergunta.append(f'libertar eu precisaria de uma dosagem exata de dois elixires, no qual {i}')
        self.pergunta.append(f'do elixir azul e {j} do elixir vermelho, faça uma divisão dos dois elixires.')
        self.pergunta.append(f'{i} / {j}= ?')

        j = randint(1, 50)
        if j % 2 == 0:
            j -= 1

        resp = j
        resp = str(resp)
        self.resposta.append(resp)

        '''self.pergunta.append(f'A entrada da esquerda é composta pos {i} paredes, e a entrada da direita')
        self.pergunta.append(f'é composta por {j} paredes, a entrada da sorte é composto')
        self.pergunta.append(f'por número de paredes impares, escolha a opção correta.')
        self.pergunta.append('')'''
        self.pergunta.append(f'Ao se aproximar da árvore, vocês encontram uma placa que diz:')
        self.pergunta.append(f'Para conseguir prosseguir pelo caminho correto escolha a opção')
        self.pergunta.append(f'com número ímpar. Escolha sabiamente!!')
        self.pergunta.append('')

        i = randint(950, 2500)
        if i % 2 != 0:
            i += 1

        resp = i
        resp = str(resp)
        self.resposta.append(resp)

        self.pergunta.append(f'Ao chegarmos na porta nos encontramos novamente com o aprendiz de ')
        self.pergunta.append('Baltazar, felizmente temos uma magia que pode o derrotar.')
        self.pergunta.append('Escolha o número par para lançar a magia que garanta a vitória')
        self.pergunta.append('')

        self.pergunta.append('Somando o (veneno de aranha, o líquido suspeito e o pó misterioso).')
        self.pergunta.append('Depois, some com 21 litros do precioso sangue de unicórnio a essa')
        self.pergunta.append('quantidade e, finalmente, divide tudo por 3')
        self.pergunta.append('(3 + 21) / 3=?')

        self.resposta.append('8')

        i = randint(20, 40)
        j = randint(5, 19)
        k = randint(1, 7)

        resp = (i - j) * k
        resp = str(resp)
        self.resposta.append(resp)
        i = str(i)
        j = str(j)
        k = str(k)
        self.pergunta.append(f'Composto por {i} elixires sagrados subtraídos por {j} essência de acônito')
        self.pergunta.append(f'e multiplica por {k},para realizar o feitiço e avançamos para o saguão principal')
        self.pergunta.append('Qual é o resultado desse efeito colateral?')
        self.pergunta.append(f'({i} - {j}) * {k}=?')


    def is_phase(self):
        if self.fase == 4:
            self.fazendeiro = sprites.fazendeiro
            self.sprites.add(self.fazendeiro)
            self.fazendeiro.move(0, 2)
        if self.fase == 5:
            pygame.sprite.Sprite.kill(sprites.fazendeiro)
        if self.fase == 6:
            self.troll = sprites.troll
            self.sprites.add(self.troll)
            self.troll.move(0, 3)
        if self.fase == 7 or self.fase == 10:
            pygame.sprite.Sprite.kill(sprites.troll)
            self.aprendiz_mal = sprites.aprendiz_mal
            self.sprites.add(self.aprendiz_mal)
            self.aprendiz_mal.move(0, 4)
        if self.fase == 8 or self.fase == 11:
            pygame.sprite.Sprite.kill(sprites.aprendiz_mal)
        if self.fase == 12:
            self.baltazar = sprites.baltazar
            self.sprites.add(self.baltazar)
            self.baltazar.move(0, 5)
        if self.pos >= 8:
            pygame.sprite.Sprite.kill(sprites.baltazar)
            pygame.sprite.Sprite.kill(sprites.aprendiz)
            pygame.sprite.Sprite.kill(sprites.mago)

    def next_phase(self):
        constant.PLAYER_ATUAL = 0
        constant.APRENDIZ_POS = 80
        self.fase += 1
        self.question = True
        self.key = True
        self.mago.fase = self.fase
        self.aprendiz.fase = self.fase
        if self.fase > constant.TOTAL_FASES:
            self.aprendiz.fase = self.mago.fase = self.fase = 0

    def intro(self):
        self.tela.fill(constant.PRETO)
        self.show_text(
            'Em um universo de magia, existia um mago muito experiente e famoso chamado Merlin',28, constant.BRANCO, constant.LARGURA/2, constant.ALTURA/2)
        pygame.display.flip()
        pygame.time.wait(4000)
        self.tela.fill(constant.PRETO)
        self.show_text(
            'Ele habitava a Ilha da Esmeralda ',
            28, constant.BRANCO, constant.LARGURA / 2, constant.ALTURA / 2 -50)
        self.show_text(
            'E por conta de sua fama e rivalidade acabou perdendo seus poderes',
            28, constant.BRANCO, constant.LARGURA/2, constant.ALTURA/2)
        self.show_text(
            'Em um duelo com um bruxo maligno chamado Baltazar',
            28, constant.BRANCO, constant.LARGURA/2, constant.ALTURA/2 + 50)
        pygame.display.flip()
        pygame.time.wait(5300)
        self.tela.fill(constant.PRETO)
        self.show_text(
            'Após o incidente, um aprendiz chamado (nome) insiste em aprender Magia com o mestre Merlin',
            28, constant.BRANCO, constant.LARGURA/2, constant.ALTURA/2 - 50)
        self.show_text(
            'Merlin exige que (nome) desenvolva uma poção, para recuperar seus poderes',
            28, constant.BRANCO, constant.LARGURA/2, constant.ALTURA/2)
        self.show_text(
            'pois com isso possibilitara ensinar (nome)',
            28, constant.BRANCO, constant.LARGURA/2, constant.ALTURA/2 + 50)
        pygame.display.flip()
        pygame.time.wait(6000)

    def show_text(self, text, size, color, x, y):
        #Exibe um texto na tela do jogo
        font = pygame.font.Font(self.font, size)
        text = font.render(text, True, color)
        text_rect = text.get_rect()
        text_rect.midtop = (x, y)
        self.tela.blit(text, text_rect)

    def vidas(self):
        vidas_rect = self.vida[self.vidaV].get_rect()
        vidas_rect.topleft = (5, 5)
        self.tela.blit(self.vida[self.vidaV], vidas_rect)

    def background(self, x, y):
        #desenha o cenário
        background_rect = self.background_image[self.fase].get_rect()
        background_rect.midtop = (x, y)
        self.tela.blit(self.background_image[self.fase], background_rect)

    def show_logo_image(self, x, y):
        #coloca uma imagem no menu
        start_logo_rect = self.logo_start.get_rect()
        start_logo_rect.midtop = (x,y)
        self.tela.blit(self.logo_start, start_logo_rect)

    def credits(self):
        waiting = True
        pg = 0
        paginas_rect = self.paginas[pg].get_rect()
        paginas_rect.midtop = (constant.LARGURA/2, 0)
        self.tela.blit(self.paginas[pg], paginas_rect)
        pygame.display.flip()
        while waiting:
            mouse1 = pygame.mouse.get_pos()
            #print(mouse1)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        waiting = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 19 + 74 > mouse1[0] > 19 and 638 + 69 > mouse1[1] > 638:  # ESC Créditos
                        waiting = False
                    if 1049 + 72 > mouse1[0] > 1049 and 333 + 89 > mouse1[1] > 333 and pg == 1:
                        pg += 1
                        paginas_rect = self.paginas[pg].get_rect()
                        paginas_rect.midtop = (constant.LARGURA / 2, 0)
                        self.tela.blit(self.paginas[pg], paginas_rect)
                    if 1049 + 72 > mouse1[0] > 1049 and 333 + 89 > mouse1[1] > 333 and pg == 0:
                        pg += 1
                        paginas_rect = self.paginas[pg].get_rect()
                        paginas_rect.midtop = (constant.LARGURA / 2, 0)
                        self.tela.blit(self.paginas[pg], paginas_rect)
                    if 155 + 68 > mouse1[0] > 155 and 321 + 90 > mouse1[1] > 321 and pg == 1:
                        pg -= 1
                        paginas_rect = self.paginas[pg].get_rect()
                        paginas_rect.midtop = (constant.LARGURA / 2, 0)
                        self.tela.blit(self.paginas[pg], paginas_rect)
                    if 155 + 68 > mouse1[0] > 155 and 321 + 90 > mouse1[1] > 321 and pg == 2:
                        pg -= 1
                        paginas_rect = self.paginas[pg].get_rect()
                        paginas_rect.midtop = (constant.LARGURA / 2, 0)
                        self.tela.blit(self.paginas[pg], paginas_rect)
            pygame.display.flip()

        self.show_logo_image(constant.LARGURA / 2, 0)
        self.show_text('JOGAR', 26, constant.AMARELO, constant.LARGURA / 2 + 6, constant.ALTURA / 1.34)
        self.show_text('SAIR', 26, constant.AMARELO, 280, constant.ALTURA / 1.34)
        self.show_text('CRÉDITOS', 26, constant.AMARELO, 1000, constant.ALTURA / 1.34)
        pygame.display.flip()

    def text_box(self):
        pygame.gfxdraw.box(self.tela, pygame.Rect(constant.LARGURA / 2 - 300, 60, 600, 250), constant.PRETO_T)
        pygame.draw.rect(self.tela, constant.PRETO, pygame.Rect(constant.LARGURA / 2 - 300, 60, 600, 250), 3)
        self.show_text(self.write_text[self.cont_text], 20, constant.BRANCO, constant.LARGURA / 2, 110)
        self.show_text(self.write_text[self.cont_text + 1], 20, constant.BRANCO, constant.LARGURA / 2, 150)
        self.show_text(self.write_text[self.cont_text + 2], 20, constant.BRANCO, constant.LARGURA / 2, 190)
        self.show_text(self.write_text[self.cont_text + 3], 20, constant.BRANCO, constant.LARGURA / 2, 230)

    def question_box(self):
        waiting = True
        while waiting:
            mouse = pygame.mouse.get_pos()
            #print(mouse)
            self.background(constant.LARGURA / 2, 0)
            self.vidas()
            pygame.gfxdraw.box(self.tela, pygame.Rect(constant.LARGURA / 2 - 300, 60, 600, 250), constant.PRETO_T)
            pygame.draw.rect(self.tela, constant.PRETO, pygame.Rect(constant.LARGURA / 2 - 300, 60, 600, 250), 3)
            self.show_text(self.pergunta[self.cont], 17, constant.BRANCO, constant.LARGURA / 2, 100)
            self.show_text(self.pergunta[self.cont + 1], 17, constant.BRANCO, constant.LARGURA / 2, 130)
            self.show_text(self.pergunta[self.cont + 2], 17, constant.BRANCO, constant.LARGURA / 2, 160)
            if self.fase != 7:
                self.show_text(self.pergunta[self.cont + 3], 19, constant.BRANCO, constant.LARGURA / 2, 180)
            else:
                self.show_text(self.pergunta[self.cont + 3], 19, constant.BRANCO, constant.LARGURA / 2, 190)

            pygame.gfxdraw.box(self.tela, pygame.Rect(constant.LARGURA / 2 - 260, 240, 100, 50), constant.PRETO_T2)
            pygame.draw.rect(self.tela, constant.PRETO, pygame.Rect(constant.LARGURA / 2 - 260, 240, 100, 50), 3)
            self.show_text(self.answers[0], 20, constant.BRANCO, constant.LARGURA / 2 - 210, 255)

            pygame.gfxdraw.box(self.tela, pygame.Rect(constant.LARGURA / 2 - 120, 240, 100, 50), constant.PRETO_T2)
            pygame.draw.rect(self.tela, constant.PRETO, pygame.Rect(constant.LARGURA / 2 - 120, 240, 100, 50), 3)
            self.show_text(self.answers[1], 20, constant.BRANCO, constant.LARGURA / 2 - 70, 255)

            pygame.gfxdraw.box(self.tela, pygame.Rect(constant.LARGURA / 2 + 20, 240, 100, 50), constant.PRETO_T2)
            pygame.draw.rect(self.tela, constant.PRETO, pygame.Rect(constant.LARGURA / 2 + 20, 240, 100, 50), 3)
            self.show_text(self.answers[2], 20, constant.BRANCO, constant.LARGURA / 2 + 70, 255)

            pygame.gfxdraw.box(self.tela, pygame.Rect(constant.LARGURA / 2 + 160, 240, 100, 50), constant.PRETO_T2)
            pygame.draw.rect(self.tela, constant.PRETO, pygame.Rect(constant.LARGURA / 2 + 160, 240, 100, 50), 3)
            self.show_text(self.answers[3], 20, constant.BRANCO, constant.LARGURA / 2 + 210, 255)
            #pygame.display.update()  # atualiza a tela a cada frame
            self.relogio.tick(constant.FPS)
            self.mago.move(0, 1)
            self.aprendiz.move(0, 0)
            self.update_sprites()
            self.sprites.draw(self.tela)
            pygame.display.flip()
            for event in pygame.event.get():
                pos = 4
                if event.type == pygame.QUIT:
                    waiting = False
                    self.play = False
                    self.is_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        waiting = False
                        self.play = False
                        self.is_running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if constant.LARGURA / 2 - 260 + 100 > mouse[0] > constant.LARGURA / 2 - 260 and 240 + 50 > mouse[1] > 240:   # JOGAR
                        pos = 0
                    elif constant.LARGURA / 2 - 120 + 100 > mouse[0] > constant.LARGURA / 2 - 120 and 240 + 50 > mouse[1] > 240:  # SAIR
                        pos = 1
                    elif constant.LARGURA / 2 + 20 + 100 > mouse[0] > constant.LARGURA / 2 + 20 and 240 + 50 > mouse[1] > 240:  # Créditos
                        pos = 2
                    elif constant.LARGURA / 2 + 160 + 100 > mouse[0] > constant.LARGURA / 2 + 160 and 240 + 50 > mouse[1] > 240:  # Créditos
                        pos = 3
                if pos >= 0 and pos < 4 and self.answers[pos] == self.resposta[self.pos]:
                    if self.fase == 12:
                        self.cont += 4
                        self.pos += 1
                        if self.pos >= 8:
                            self.winner()
                            waiting = False
                            self.play = False
                            self.is_running = False
                        else:
                            for i in range(len(self.answers)):
                                j = randint(1, 51)
                                j = str(j)
                                self.answers[i] = j
                            i = randint(0, 3)
                            self.answers[i] = self.resposta[self.pos]
                            self.question_box()
                    if self.pos < 8:
                        self.next_phase()
                        self.cont += 4
                        self.pos += 1
                        waiting = False
                elif pos >= 0 and pos < 4:
                    self.vidaV += 1

                if self.vidaV >= 3:
                    self.game_over()
                    if self.play == False:
                        waiting = False

    def wait_press(self):
        #espera o jogador clicar em um botão para começar o jogo
        waiting = True
        while waiting:
            mouse = pygame.mouse.get_pos()
            #print(mouse)
            self.relogio.tick(constant.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.is_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        waiting = False
                        self.is_running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 535+224 > mouse[0] > 535 and 507+92 > mouse[1] > 507:   #JOGAR
                        waiting = False
                    if 176+224 > mouse[0] > 176 and 507+92 > mouse[1] > 507:   #SAIR
                        self.is_running = False
                        waiting = False
                    if 889+224 > mouse[0] > 889 and 507+92 > mouse[1] > 507:   #Créditos
                        self.credits()

                '''if event.type == pygame.KEYUP:
                    waiting = False'''

    def start(self):
        #menu
        self.show_logo_image(constant.LARGURA/2, 0)
        self.show_text('JOGAR', 26, constant.AMARELO, constant.LARGURA/2+6, constant.ALTURA/1.34)
        self.show_text('SAIR', 26, constant.AMARELO, 280, constant.ALTURA / 1.34)
        self.show_text('CRÉDITOS', 26, constant.AMARELO, 1000, constant.ALTURA / 1.34)
        pygame.display.flip()
        self.wait_press()

    def winner(self):
        waiting = True
        while waiting:
            winner_rect = self.winner_img.get_rect()
            winner_rect.topleft = (0, 0)
            self.tela.blit(self.winner_img, winner_rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        waiting = False
            pygame.display.flip()

    def game_over(self):
        waiting = True
        while waiting:
            mouse = pygame.mouse.get_pos()
            self.relogio.tick(constant.FPS)
            self.tela.fill(constant.PRETO)
            self.show_text("Você Perdeu", 32, constant.BRANCO, constant.LARGURA / 2, 210)
            self.show_text("Deseja jogar novamente?", 32, constant.BRANCO, constant.LARGURA / 2, 280)
            self.show_text("SIM", 30, constant.BRANCO, 460, 408)
            self.show_text("NÃO", 30, constant.BRANCO, 812, 408)
            pygame.draw.rect(self.tela, constant.BRANCO, pygame.Rect(400, 390, 130, 65), 3)
            pygame.draw.rect(self.tela, constant.BRANCO, pygame.Rect(750, 390, 130, 65), 3)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.play = False
                    self.is_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        waiting = False
                        self.play = False
                        self.is_running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 400 + 130 > mouse[0] > 400 and 390 + 65 > mouse[1] > 390:
                        waiting = False
                        self.play = False
                    if 750 + 130 > mouse[0] > 750 and 390 + 65 > mouse[1] > 390:
                        waiting = False
                        self.play = False
                        self.is_running = False
        pygame.sprite.Group().empty()



g = Game()
g.start()

while g.is_running:
    g.new_game()
    if g.is_running:
        constant.APRENDIZ_POS = 80
        constant.PLAYER_ATUAL = 0
        g = Game()
        g.start()