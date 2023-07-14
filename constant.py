#Dimensões da tela
LARGURA = 1280
ALTURA = 720

TOTAL_FASES = 12


PLAYER_POS_X = 0
APRENDIZ_POS = 80
PLAYER_POS_Y = ALTURA - 112
PLAYER_ATUAL = 0
SPEED = 4

#Titulo do jogo
TITULO = 'MAGE MAT'

#fps
FPS = 30

#Cores
PRETO = (0, 0, 0)
PRETO_T = (0, 0, 0, 150)
PRETO_T2 = (0, 0, 0, 60)
AMARELO = (244, 233, 51)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)

#Fonte
FONTE = 'arial'

#Carregar imagem das fases
#Menu
LOGO_MENU = 'LogoMenu.jpeg'
START_BTN = 'start_btn.png'

WINNER = 'winner.png'
GAME_OVER = 'Game_Over.jpeg'

FASES_I = [2, 4, 6, 7, 8, 10, 12]

#Taverna externo
BACKGROUND_IMAGES = []

BACKGROUND_IMAGES.append('esmeraldIsland.png')
BACKGROUND_IMAGES.append('City.png')
BACKGROUND_IMAGES.append('tavern_externo.png')
BACKGROUND_IMAGES.append('taverna_interno.png')
BACKGROUND_IMAGES.append('fazenda.png')
BACKGROUND_IMAGES.append('Caverna_exterior.png')
BACKGROUND_IMAGES.append('Caverna_interior.png')
BACKGROUND_IMAGES.append('floresta.png')
BACKGROUND_IMAGES.append('temple.png')
BACKGROUND_IMAGES.append('dentro_templo.png')
BACKGROUND_IMAGES.append('porta_final.png')
BACKGROUND_IMAGES.append('castle1.png')
BACKGROUND_IMAGES.append('interior_castelo.png')

PAGINAS_IMAGES = []
PAGINAS_IMAGES.append('pg1.png')
PAGINAS_IMAGES.append('pg2.png')
PAGINAS_IMAGES.append('pg3.png')

VIDAS = []
VIDAS.append('vida3.png')
VIDAS.append('vida2.png')
VIDAS.append('vida1.png')
VIDAS.append('vida0.png')

character_size = []
character_posY = []
mage_character_posY = []
character_collide = []
distance = []

#Fase 0 - Esmerald Island
character_size.append(110)
character_posY.append(569)
mage_character_posY.append(569)
character_collide.append(LARGURA-64)
distance.append(80)

# Fase 1 - City
character_size.append(125)
character_posY.append(563)
mage_character_posY.append(563)
character_collide.append(LARGURA-64)
distance.append(80)

 # Fase 2 - Taverna Exterior
character_size.append(120)
character_posY.append(515)
mage_character_posY.append(515)
character_collide.append(570)
distance.append(80)

 # Fase 3 - Taverna Interior
character_size.append(220)
character_posY.append(500)
mage_character_posY.append(500)
character_collide.append(1050)
distance.append(160)

 # Fase 4 - Fazenda
character_size.append(170)
character_posY.append(543)
mage_character_posY.append(543)
character_collide.append(500)
distance.append(110)

# Fase 5 - Caverna Exterior
character_size.append(145)
character_posY.append(555)
mage_character_posY.append(555)
character_collide.append(1060)
distance.append(90)

# Fase 6 - Caverna Interior
character_size.append(175)
character_posY.append(535)
mage_character_posY.append(535)
character_collide.append(490)
distance.append(115)

# Fase 7 - Floresta
character_size.append(185)
character_posY.append(450)
mage_character_posY.append(300)
character_collide.append(380)
distance.append(80)

# Fase 8 - Templo
character_size.append(145)
character_posY.append(524)
mage_character_posY.append(524)
character_collide.append(660)
distance.append(100)

# Fase 9 - Dentro do templo
character_size.append(130)
character_posY.append(540)
mage_character_posY.append(540)
character_collide.append(LARGURA-64)
distance.append(90)

# Fase 10 - Porta Final
character_size.append(180)
character_posY.append(500)
mage_character_posY.append(350)
character_collide.append(360)
distance.append(80)

# Fase 11 - Castelo Exterior
character_size.append(75)
character_posY.append(582)
mage_character_posY.append(582)
character_collide.append(590)
distance.append(55)

# Fase 12 - Castelo Interior
character_size.append(180)
character_posY.append(500)
mage_character_posY.append(350)
character_collide.append(375)
distance.append(80)