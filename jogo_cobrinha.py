import pygame, random
from pygame.locals import *

#funcao para retornar numero aleatorio multiplo de 10
def num_aleatorio_alin():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//10*10, y//10*10)

def colisao(c1,c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

#macros
# nao entendo esses numeros
UP = 0
RIGTH = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Cobrinha')

# para criar a cobra, usaremos uma lista
cobra = [(200,200), (210,200), (220,200)]
cobra_pele = pygame.Surface((10,10))
cobra_pele.fill((255,255,255)) # pintar

maca = pygame.Surface((10,10))
maca.fill((255,0,0))
maca_pos = num_aleatorio_alin()

direcao = LEFT

#alterar configuracao de tempo de movimento da cobra
tempo = pygame.time.Clock()

# jogos sao matrizes

while True:
    tempo.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    #movimentar a cobra ao usar as teclas
    if event.type == KEYDOWN:
        if event.key == K_UP: #existe um codigo para cada tecla do teclado
            direcao = UP
        if event.key == K_DOWN:
            direcao = DOWN
        if event.key == K_RIGHT:
            direcao = RIGTH
        if event.key == K_LEFT:
            direcao = LEFT

    if colisao(cobra[0], maca_pos):
        maca_pos = num_aleatorio_alin()
        cobra.append((0,0)) #aumentar a cobra

    for i in range(len(cobra) - 1, 0, -1 ):
        cobra[i] = (cobra[i-1][0], cobra[i-1][1])

    if direcao == UP:
        cobra[0] = (cobra[0][0], cobra[0][1] - 10)
    if direcao == DOWN:
        cobra[0] = (cobra[0][0], cobra[0][1] + 10)
    if direcao == RIGTH:
        cobra[0] = (cobra[0][0] + 10, cobra[0][1])
    if direcao == LEFT:
        cobra[0] = (cobra[0][0] - 10, cobra[0][1])

    screen.fill((0,0,0))
    screen.blit(maca, maca_pos) # mostrar a maca
    for pos in cobra:
        screen.blit(cobra_pele,pos) # mostrar a cobra


    pygame.display.update()