import pygame
import os
import random
import passaro
import cano
import chao

TELA_LARGURA = 500
TELA_ALTURA = 800

IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))

pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 50)
