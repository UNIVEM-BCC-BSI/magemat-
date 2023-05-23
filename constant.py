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
AMARELO = (244, 233, 51)
BRANCO = (255, 255, 255)

#Fonte
FONTE = 'arial'

#Carregar imagem das fases
#Menu
LOGO_MENU = 'LogoMenu.jpeg'
START_BTN = 'start_btn.png'

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

character_size = []
character_posY = []

     #Fase 0 - Esmerald Island
character_size.append(80)
character_posY.append(599)

# Fase 1 - City
character_size.append(100)
character_posY.append(603)

 # Fase 2 - Taverna Exterior
character_size.append(120)
character_posY.append(515)

 # Fase 3 - Taverna Interior
character_size.append(220)
character_posY.append(500)

 # Fase 4 - Fazenda
character_size.append(170)
character_posY.append(543)

# Fase 5 - Caverna Exterior
character_size.append(145)
character_posY.append(555)

# Fase 6 - Caverna Interior
character_size.append(175)
character_posY.append(535)

# Fase 7 - Floresta
character_size.append(185)
character_posY.append(350)

# Fase 8 - Templo
character_size.append(145)
character_posY.append(524)

# Fase 9 - Dentro do templo
character_size.append(130)
character_posY.append(540)

# Fase 10 - Porta Final
character_size.append(180)
character_posY.append(460)

# Fase 11 - Castelo Exterior
character_size.append(80)
character_posY.append(582)

# Fase 12 - Castelo Interior
character_size.append(180)
character_posY.append(420)