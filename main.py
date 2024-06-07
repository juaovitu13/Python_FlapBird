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

def desenhar_tela(tela, passaros, canos, chao, pontos):
    tela.blit(IMAGEM_BACKGROUND, (0, 0))
    for passaro in passaros:
        passaro.desenhar(tela)
    for cano in canos:
        cano.desenhar(tela)

    texto = FONTE_PONTOS.render(f"Pontuação: {pontos}", 1, (255, 255, 255))
    tela.blit(texto, (TELA_LARGURA - 10 - texto.get_width(), 10))
    chao.desenhar(tela)
    pygame.display.update()

def main():
    passaros = [Passaro(230, 350)]
    chao = Chao(730)
    canos = [Cano(700)]
    tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
    pontos = 0
    relogio = pygame.time.Clock()

if __name__ == '__main__':
    main()
