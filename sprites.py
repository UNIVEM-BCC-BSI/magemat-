import pygame
import constant

call = 0

class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #sprites do mago
        self.sprites_list = []
        self.sprites_list_Back = []
        self.sprites_idle = []
        self.sprites_idleB = []
        # sprites do aprendiz
        self.sprites_list_aprendiz = []
        self.sprites_idle_aprendiz = []
        self.sprites_list_aprendiz_Back = []
        self.sprites_idleB_aprendiz = []
        #sprite fazendeiro
        self.sprites_idleB_fazendeiro = []
        #troll
        self.sprites_idle_troll = []
        self.sprites_attack_troll = []
        #aprendiz mal
        self.sprites_idle_aprendiz_mal = []
        #baltazar
        self.sprites_idle_baltazar = []

        self.is_walking_forward = True


        #mago parado
        self.sprites_idle.append(pygame.image.load('sprites/1_IDLE_000.png'))
        self.sprites_idle.append(pygame.image.load('sprites/1_IDLE_001.png'))
        self.sprites_idle.append(pygame.image.load('sprites/1_IDLE_002.png'))
        self.sprites_idle.append(pygame.image.load('sprites/1_IDLE_003.png'))
        self.sprites_idle.append(pygame.image.load('sprites/1_IDLE_004.png'))
        #mago parado olhando para trás
        self.sprites_idleB.append(pygame.transform.flip(pygame.image.load
                                                        ('sprites/1_IDLE_000.png'), True, False))
        self.sprites_idleB.append(pygame.transform.flip(pygame.image.load
                                                        ('sprites/1_IDLE_001.png'), True, False))
        self.sprites_idleB.append(pygame.transform.flip(pygame.image.load
                                                        ('sprites/1_IDLE_002.png'), True, False))
        self.sprites_idleB.append(pygame.transform.flip(pygame.image.load
                                                        ('sprites/1_IDLE_003.png'), True, False))
        self.sprites_idleB.append(pygame.transform.flip(pygame.image.load
                                                        ('sprites/1_IDLE_004.png'), True, False))
        #mago andando para frente
        self.sprites_list.append(pygame.image.load('sprites/2_WALK_000.png'))
        self.sprites_list.append(pygame.image.load('sprites/2_WALK_001.png'))
        self.sprites_list.append(pygame.image.load('sprites/2_WALK_002.png'))
        self.sprites_list.append(pygame.image.load('sprites/2_WALK_003.png'))
        self.sprites_list.append(pygame.image.load('sprites/2_WALK_004.png'))
        #mago andando para tras
        self.sprites_list_Back.append(pygame.image.load('sprites/2_WALKB_000.png'))
        self.sprites_list_Back.append(pygame.image.load('sprites/2_WALKB_001.png'))
        self.sprites_list_Back.append(pygame.image.load('sprites/2_WALKB_002.png'))
        self.sprites_list_Back.append(pygame.image.load('sprites/2_WALKB_003.png'))
        self.sprites_list_Back.append(pygame.image.load('sprites/2_WALKB_004.png'))

        self.sprites_list_aprendiz.append(pygame.image.load('sprites/A2_WALK_000.png'))
        self.sprites_list_aprendiz.append(pygame.image.load('sprites/A2_WALK_001.png'))
        self.sprites_list_aprendiz.append(pygame.image.load('sprites/A2_WALK_002.png'))
        self.sprites_list_aprendiz.append(pygame.image.load('sprites/A2_WALK_003.png'))
        self.sprites_list_aprendiz.append(pygame.image.load('sprites/A2_WALK_004.png'))

        self.sprites_idle_aprendiz.append(pygame.image.load('sprites/A1_IDLE_000.png'))
        self.sprites_idle_aprendiz.append(pygame.image.load('sprites/A1_IDLE_001.png'))
        self.sprites_idle_aprendiz.append(pygame.image.load('sprites/A1_IDLE_002.png'))
        self.sprites_idle_aprendiz.append(pygame.image.load('sprites/A1_IDLE_003.png'))
        self.sprites_idle_aprendiz.append(pygame.image.load('sprites/A1_IDLE_004.png'))

        self.sprites_idleB_aprendiz.append(pygame.image.load('sprites/A1_IDLEB_000.png'))
        self.sprites_idleB_aprendiz.append(pygame.image.load('sprites/A1_IDLEB_001.png'))
        self.sprites_idleB_aprendiz.append(pygame.image.load('sprites/A1_IDLEB_002.png'))
        self.sprites_idleB_aprendiz.append(pygame.image.load('sprites/A1_IDLEB_003.png'))
        self.sprites_idleB_aprendiz.append(pygame.image.load('sprites/A1_IDLEB_004.png'))

        self.sprites_list_aprendiz_Back.append(pygame.image.load('sprites/A2_WALKB_000.png'))
        self.sprites_list_aprendiz_Back.append(pygame.image.load('sprites/A2_WALKB_001.png'))
        self.sprites_list_aprendiz_Back.append(pygame.image.load('sprites/A2_WALKB_002.png'))
        self.sprites_list_aprendiz_Back.append(pygame.image.load('sprites/A2_WALKB_003.png'))
        self.sprites_list_aprendiz_Back.append(pygame.image.load('sprites/A2_WALKB_004.png'))

        self.sprites_idleB_fazendeiro.append(pygame.image.load('sprites/Fazendeiro0.png'))
        self.sprites_idleB_fazendeiro.append(pygame.image.load('sprites/Fazendeiro1.png'))
        self.sprites_idleB_fazendeiro.append(pygame.image.load('sprites/Fazendeiro2.png'))
        self.sprites_idleB_fazendeiro.append(pygame.image.load('sprites/Fazendeiro3.png'))
        self.sprites_idleB_fazendeiro.append(pygame.image.load('sprites/Fazendeiro4.png'))
        self.sprites_idleB_fazendeiro.append(pygame.image.load('sprites/Fazendeiro5.png'))
        self.sprites_idleB_fazendeiro.append(pygame.image.load('sprites/Fazendeiro6.png'))
        self.sprites_idleB_fazendeiro.append(pygame.image.load('sprites/Fazendeiro7.png'))
        self.sprites_idleB_fazendeiro.append(pygame.image.load('sprites/Fazendeiro8.png'))
        self.sprites_idleB_fazendeiro.append(pygame.image.load('sprites/Fazendeiro9.png'))

        self.sprites_attack_troll.append(pygame.transform.flip(pygame.image.load
                                                             ('sprites/Troll_01_1_ATTACK_000.png'), True, False))
        self.sprites_attack_troll.append(pygame.transform.flip(pygame.image.load
                                                             ('sprites/Troll_01_1_ATTACK_001.png'), True, False))
        self.sprites_attack_troll.append(pygame.transform.flip(pygame.image.load
                                                             ('sprites/Troll_01_1_ATTACK_002.png'), True, False))
        self.sprites_attack_troll.append(pygame.transform.flip(pygame.image.load
                                                             ('sprites/Troll_01_1_ATTACK_003.png'), True, False))
        self.sprites_attack_troll.append(pygame.transform.flip(pygame.image.load
                                                             ('sprites/Troll_01_1_ATTACK_004.png'), True, False))
        self.sprites_attack_troll.append(pygame.transform.flip(pygame.image.load
                                                             ('sprites/Troll_01_1_ATTACK_005.png'), True, False))
        self.sprites_attack_troll.append(pygame.transform.flip(pygame.image.load
                                                             ('sprites/Troll_01_1_ATTACK_006.png'), True, False))
        self.sprites_attack_troll.append(pygame.transform.flip(pygame.image.load
                                                             ('sprites/Troll_01_1_ATTACK_007.png'), True, False))
        self.sprites_attack_troll.append(pygame.transform.flip(pygame.image.load
                                                             ('sprites/Troll_01_1_ATTACK_008.png'), True, False))
        self.sprites_attack_troll.append(pygame.transform.flip(pygame.image.load
                                                             ('sprites/Troll_01_1_ATTACK_009.png'), True, False))

        self.sprites_idle_troll.append(pygame.transform.flip(pygame.image.load
                                                             ('sprites/Troll_01_1_IDLE_000.png'), True, False))
        self.sprites_idle_troll.append(pygame.transform.flip(pygame.image.load
                                                             ('sprites/Troll_01_1_IDLE_001.png'), True, False))
        self.sprites_idle_troll.append(pygame.transform.flip(pygame.image.load
                                                             ('sprites/Troll_01_1_IDLE_002.png'), True, False))
        self.sprites_idle_troll.append(pygame.transform.flip(pygame.image.load
                                                             ('sprites/Troll_01_1_IDLE_003.png'), True, False))
        self.sprites_idle_troll.append(pygame.transform.flip(pygame.image.load
                                                             ('sprites/Troll_01_1_IDLE_004.png'), True, False))
        self.sprites_idle_troll.append(pygame.transform.flip(pygame.image.load
                                                             ('sprites/Troll_01_1_IDLE_005.png'), True, False))
        self.sprites_idle_troll.append(pygame.transform.flip(pygame.image.load
                                                             ('sprites/Troll_01_1_IDLE_006.png'), True, False))
        self.sprites_idle_troll.append(pygame.transform.flip(pygame.image.load
                                                             ('sprites/Troll_01_1_IDLE_007.png'), True, False))
        self.sprites_idle_troll.append(pygame.transform.flip(pygame.image.load
                                                             ('sprites/Troll_01_1_IDLE_008.png'), True, False))
        self.sprites_idle_troll.append(pygame.transform.flip(pygame.image.load
                                                             ('sprites/Troll_01_1_IDLE_009.png'), True, False))

        self.sprites_idle_aprendiz_mal.append(pygame.transform.flip(pygame.image.load
                                                                    ('sprites/1_EA_IDLE_000.png'), True, False))
        self.sprites_idle_aprendiz_mal.append(pygame.transform.flip(pygame.image.load
                                                                    ('sprites/1_EA_IDLE_001.png'), True, False))
        self.sprites_idle_aprendiz_mal.append(pygame.transform.flip(pygame.image.load
                                                                    ('sprites/1_EA_IDLE_002.png'), True, False))
        self.sprites_idle_aprendiz_mal.append(pygame.transform.flip(pygame.image.load
                                                                    ('sprites/1_EA_IDLE_003.png'), True, False))
        self.sprites_idle_aprendiz_mal.append(pygame.transform.flip(pygame.image.load
                                                                    ('sprites/1_EA_IDLE_004.png'), True, False))

        self.sprites_idle_baltazar.append(pygame.transform.flip(pygame.image.load
                                                                ('sprites/Baltazar_IDLE_000.png'), True, False))
        self.sprites_idle_baltazar.append(pygame.transform.flip(pygame.image.load
                                                                ('sprites/Baltazar_IDLE_001.png'), True, False))
        self.sprites_idle_baltazar.append(pygame.transform.flip(pygame.image.load
                                                                ('sprites/Baltazar_IDLE_002.png'), True, False))
        self.sprites_idle_baltazar.append(pygame.transform.flip(pygame.image.load
                                                                ('sprites/Baltazar_IDLE_003.png'), True, False))
        self.sprites_idle_baltazar.append(pygame.transform.flip(pygame.image.load
                                                                ('sprites/Baltazar_IDLE_004.png'), True, False))

        self.atual = 0
        self.atualM = 0
        self.atualF = 0
        self.atualAM = 0
        self.atualB = 0
        self.fase = 0
        #self.pos_x = constant.PLAYER_POS_X

        if call == 0:
            self.image = self.sprites_list[self.atual]
            self.rect = self.image.get_rect()
            self.rect.topleft = (0, constant.character_posY[self.fase])
            self.image = pygame.transform.scale(self.image,
                                                    (constant.character_size[self.fase], constant.character_size[self.fase]))
        elif call == 1:
            self.image = self.sprites_list_aprendiz[self.atual]
            self.rect = self.image.get_rect()
            self.rect.topleft = (80, constant.character_posY[self.fase])
            self.image = pygame.transform.scale(self.image,
                                                 (constant.character_size[self.fase], constant.character_size[self.fase]))
        elif call == 4:
            self.image = self.sprites_idle_aprendiz_mal[self.atualAM]
            self.rect = self.image.get_rect()
            self.rect.topleft = (80, constant.character_posY[self.fase])
            self.image = pygame.transform.scale(self.image,
                                                (constant.character_size[self.fase], constant.character_size[self.fase]))

    def atualizar(self, i, personagem):
        self.atual += 0.5
        self.atualM += 0.4
        if i == 1:
            self.is_walking_forward = True
            if personagem == 0:
                if self.atual >= len(self.sprites_list_aprendiz):
                    self.atual = 0
                self.image = self.sprites_list_aprendiz[int(self.atual)]
                self.image = pygame.transform.scale(self.image, (
                    constant.character_size[self.fase], constant.character_size[self.fase]))
            else:
                if constant.APRENDIZ_POS < constant.PLAYER_ATUAL:
                    if self.atualM >= len(self.sprites_idleB):
                        self.atualM = 0
                    self.image = self.sprites_idleB[int(self.atualM)]
                    self.image = pygame.transform.scale(self.image, (
                        constant.character_size[self.fase], constant.character_size[self.fase]))
                else:
                    if constant.PLAYER_ATUAL + 80 >= constant.APRENDIZ_POS:
                        if self.atualM >= len(self.sprites_list):
                            self.atualM = 0
                        self.image = self.sprites_list[int(self.atualM)]
                        self.image = pygame.transform.scale(self.image, (
                            constant.character_size[self.fase], constant.character_size[self.fase]))
        elif i == 2:
            self.is_walking_forward = False
            if personagem == 0:
                if self.atual >= len(self.sprites_list):
                    self.atual = 0
                self.image = self.sprites_list_aprendiz_Back[int(self.atual)]
                self.image = pygame.transform.scale(self.image, (
                    constant.character_size[self.fase], constant.character_size[self.fase]))
            else:
                if constant.APRENDIZ_POS < constant.PLAYER_ATUAL:
                    if self.atualM >= len(self.sprites_idleB):
                        self.atualM = 0
                    self.image = self.sprites_idleB[int(self.atualM)]
                    self.image = pygame.transform.scale(self.image, (
                        constant.character_size[self.fase], constant.character_size[self.fase]))

        elif i == 0:
            if personagem == 0:
                if self.is_walking_forward:
                    if self.atual >= len(self.sprites_idle_aprendiz):
                        self.atual = 0
                    self.image = self.sprites_idle_aprendiz[int(self.atual)]
                    self.image = pygame.transform.scale(self.image, (
                        constant.character_size[self.fase], constant.character_size[self.fase]))
                else:
                    if self.atual >= len(self.sprites_idleB_aprendiz):
                        self.atual = 0
                    self.image = self.sprites_idleB_aprendiz[int(self.atual)]
                    self.image = pygame.transform.scale(self.image, (
                        constant.character_size[self.fase], constant.character_size[self.fase]))
            elif personagem == 1:
                if constant.APRENDIZ_POS < constant.PLAYER_ATUAL:
                    if self.atualM >= len(self.sprites_idleB):
                        self.atualM = 0
                    self.image = self.sprites_idleB[int(self.atualM)]
                    self.image = pygame.transform.scale(self.image, (
                        constant.character_size[self.fase], constant.character_size[self.fase]))
                else:
                    if self.atualM >= len(self.sprites_idle):
                        self.atualM = 0
                    self.image = self.sprites_idle[int(self.atualM)]
                    self.image = pygame.transform.scale(self.image, (
                        constant.character_size[self.fase], constant.character_size[self.fase]))
            elif personagem == 2:
                self.atualF += 0.4
                if self.atualF >= len(self.sprites_idleB_fazendeiro):
                    self.atualF = 0
                self.image = self.sprites_idleB_fazendeiro[int(self.atualF)]
                self.image = pygame.transform.scale(self.image, (
                    constant.character_size[self.fase]+50, constant.character_size[self.fase]+135))
            elif personagem == 3:
                self.atualF += 0.6
                if self.atualF >= len(self.sprites_idle_troll):
                    self.atualF = 0
                    self.switch = False
                self.image = self.sprites_idle_troll[int(self.atualF)]
                self.image = pygame.transform.scale(self.image, (
                    constant.character_size[self.fase] + 480, constant.character_size[self.fase] + 360))
            elif personagem == 4:
                self.atualAM += 0.4
                if self.atualAM >= len(self.sprites_idle_aprendiz_mal):
                    self.atualAM = 0
                self.image = self.sprites_idle_aprendiz_mal[int(self.atualAM)]
                self.image = pygame.transform.scale(self.image, (
                    constant.character_size[self.fase]+100, constant.character_size[self.fase]+100))
            elif personagem == 5:
                self.atualB += 0.4
                if self.atualB >= len(self.sprites_idle_baltazar):
                    self.atualB = 0
                self.image = self.sprites_idle_baltazar[int(self.atualB)]
                self.image = pygame.transform.scale(self.image, (
                    constant.character_size[self.fase] + 100, constant.character_size[self.fase] + 100))

    def collide_left(self):
        if constant.APRENDIZ_POS <= constant.PLAYER_POS_X:
            return False
        else:
            return True

    def collide_right(self):
        if constant.APRENDIZ_POS >= constant.LARGURA-64:
            return False
        else:
            return True

    def move(self, d, personagem):
        if d == 1:
            if self.collide_right():
                constant.APRENDIZ_POS += constant.SPEED
                if constant.PLAYER_ATUAL + 80 <= constant.APRENDIZ_POS:
                    constant.PLAYER_ATUAL+= constant.SPEED
                self.atualizar(d, personagem)
                if personagem == 0:
                    self.rect = self.image.get_rect()
                    self.rect.topleft = (constant.APRENDIZ_POS, constant.character_posY[self.fase])
                else:
                    self.rect = self.image.get_rect()
                    self.rect.topleft = (constant.PLAYER_ATUAL, constant.character_posY[self.fase])

        elif d == 2:
            if self.collide_left():
                constant.APRENDIZ_POS -= constant.SPEED
                self.atualizar(d, personagem)
                if personagem == 0:
                    self.rect = self.image.get_rect()
                    self.rect.topleft = (constant.APRENDIZ_POS, constant.character_posY[self.fase])
                else:
                    self.rect = self.image.get_rect()
                    self.rect.topleft = (constant.PLAYER_ATUAL, constant.character_posY[self.fase])

        elif d == 0:
            self.atualizar(d, personagem)
            if personagem == 0:
                self.rect = self.image.get_rect()
                self.rect.topleft = (constant.APRENDIZ_POS, constant.character_posY[self.fase])
            elif personagem == 1:
                self.rect = self.image.get_rect()
                self.rect.topleft = (constant.PLAYER_ATUAL, constant.character_posY[self.fase])
            elif personagem == 2:
                self.rect = self.image.get_rect()
                self.rect.topleft = (constant.LARGURA/2, constant.character_posY[self.fase]-85)
            elif personagem == 3:
                self.rect = self.image.get_rect()
                self.rect.topleft = (constant.LARGURA / 2 + 100, constant.character_posY[self.fase]-285)
            elif personagem == 4:
                self.rect = self.image.get_rect()
                self.rect.topleft = (constant.LARGURA / 2 + 200, constant.character_posY[self.fase]-300)
            elif personagem == 5:
                self.rect = self.image.get_rect()
                self.rect.topleft = (constant.LARGURA / 2 + 200, constant.character_posY[self.fase] - 210)
        else:
            pass

mago= Sprite()
call += 1
aprendiz = Sprite()
call += 1
fazendeiro = Sprite()
call += 1
troll = Sprite()
call += 1
aprendiz_mal = Sprite()
call += 1
baltazar = Sprite()
