import pygame
from pygame.locals import *
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
        self.upload_files()

    def new_game(self):
        #instancia as classes das sprites do jogo
        self.sprites = pygame.sprite.Group()
        self.mago = sprites.mago
        self.aprendiz = sprites.aprendiz
        self.sprites.add(self.mago)
        self.sprites.add(self.aprendiz)
        self.intro()
        self.run()

    def run(self):
        #loop do jogo
        self.play = True
        while self.play:
            self.relogio.tick(constant.FPS)
            self.events()
            self.is_phase()
            self.draw_sprites()
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
        self.sprites.draw(self.tela) #desenha
        pygame.display.update() #atualiza a tela a cada frame

    def upload_files(self):
        #carragar os arquivos de audios e imagens
        diretorio_imagens = os.path.join(os.getcwd(), 'imagens')
        #self.spritesheet = os.path.join(diretorio_imagens, constant.BACKGROUND_IMAGES[2])
        self.logo_start_string = os.path.join(diretorio_imagens, constant.LOGO_MENU) #retorna um valor em string
        self.logo_start = pygame.image.load(self.logo_start_string).convert()  # converte de string para imagem

        self.paginas = []
        for i in range(3):
            self.paginas_string = os.path.join(diretorio_imagens, constant.PAGINAS_IMAGES[i])
            self.paginas.append(pygame.image.load(self.paginas_string).convert())

        self.background_image = []
        for i in range(13):
            self.background_string = os.path.join(diretorio_imagens, constant.BACKGROUND_IMAGES[i])
            self.background_image.append(pygame.image.load(self.background_string).convert())

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

    def next_phase(self):
        constant.PLAYER_ATUAL = 0
        constant.APRENDIZ_POS = 80
        self.fase += 1
        self.mago.fase = self.fase
        self.aprendiz.fase = self.fase
        if self.fase > constant.TOTAL_FASES:
            self.aprendiz.fase = self.mago.fase = self.fase = 0

    def intro(self):
        self.tela.fill(constant.PRETO)
        self.show_text(
            'Em um universo de magia, existia um mago muito experiente e famoso chamado Merlin',28, constant.BRANCO, constant.LARGURA/2, constant.ALTURA/2)
        pygame.display.flip()
        pygame.time.wait(5000)
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
        pygame.time.wait(12000)
        self.tela.fill(constant.PRETO)
        self.show_text(
            'Após o incidente, um aprendiz chamado Alfredo insiste em aprender Magia com o mestre Merlin',
            28, constant.BRANCO, constant.LARGURA/2, constant.ALTURA/2 - 50)
        self.show_text(
            'Merlin exige que Alfredo desenvolva uma poção, para recuperar seus poderes',
            28, constant.BRANCO, constant.LARGURA/2, constant.ALTURA/2)
        self.show_text(
            'pois com isso possibilitara ensinar Alfredo',
            28, constant.BRANCO, constant.LARGURA/2, constant.ALTURA/2 + 50)
        pygame.display.flip()
        pygame.time.wait(14000)

    def show_text(self, text, size, color, x, y):
        #Exibe um texto na tela do jogo
        font = pygame.font.Font(self.font, size)
        text = font.render(text, True, color)
        text_rect = text.get_rect()
        text_rect.midtop = (x, y)
        self.tela.blit(text, text_rect)

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

    def game_over(self):
        pass


g = Game()
g.start()

while g.is_running:
    g.new_game()
    g.game_over()