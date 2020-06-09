from random import randint
from pygame.locals import *
import menu
import pygame
import dino

opcao = menu.tela_menu(0)

while opcao != 2:
    dino.limpa_tela()    
    if opcao == 2:
        break
    elif opcao == 1:
        resultado =  dino.tela_jogo()
        opcao = menu.tela_menu(resultado)
    print('Placar = %d' %resultado)
    
pygame.quit()    
