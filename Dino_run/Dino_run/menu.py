from pygame.locals import *
import pygame
from random import randint
import os
import dino

pygame.init()
#-----------------------------------------------------------------
def escolhe_som(som):
    audio = {1:'audio\m1.mp3', 2:'audio\m2.mp3'}
    return audio[som]

#-----------------------------------------------------------------
def cores_resultado(cont_resultado):
    cores = {1:(110,0,0),2:(110,20,20),
             3:(0,0,206), 4:(20,20, 206)
             }
    return cores[cont_resultado]

#-----------------------------------------------------------------
def player_menu(dino_menu):
    opcao = {1:'image\mi1.png',2:'image\mi2.png',3:'image\mi3.png',4:'image\mi4.png',
             5:'image\mi5.png',6:'image\mi6.png',7:'image\mi7.png',8:'image\mi8.png',
             9:'image\mi9.png',10:'image\mi10.png'}
    
    return opcao[dino_menu]
#-----------------------------------------------------------------
def b1_voa():  
    tipo = randint(1, 3)
    opcao = {1:'image\mb1.png',2:'image\mb2.png',
             3:'image\mb3.png'}
     
    return opcao[tipo]
#-----------------------------------------------------------------
def tela_menu(resultado):

    janela = pygame.display.set_mode((800,600))
    dino_menu = 0
    fundo_menu = pygame.image.load('image\md.png')
    chao_menu = pygame.image.load('image\ch.png')
    arvore1 = pygame.image.load('image\mtree2.png')
    arvore2 = pygame.image.load('image\mtree3.png')
    placa = pygame.image.load('image\msign.png')
    mush1 = pygame.image.load('image\mmush1.png')
    mush2 = pygame.image.load('image\mmush2.png')
    
    cont_resultado = 0
    
    # janela com placar de pontos-------------------------------------------------------
    font = pygame.font.SysFont('arial black',30)
    font2 = pygame.font.SysFont('arial black',45)
    font3 = pygame.font.SysFont('arial black',25)
    
    texto2 = font.render('Aperte "ESPAÇO" para jogar novamente!', True, (221,248,255), (221,248,255))
    pos_texto2= texto2.get_rect()
    pos_texto2.center = (1000,1000)
    #-----------------------------------------------------------------------------------
    pygame.display.set_caption('Dino -> Menu')
    clock = pygame.time.Clock()
    pygame.mixer.music.load('audio\m4.mp3')
    pygame.mixer.music.play()

    b1 = pygame.image.load('image\mb1.png')
    b1 = pygame.transform.scale(b1, (54, 40))
    xb1 = 900
    yb1 = 200
    veloc_b1 = 15

    
    # cria laço de repetição para manter janela aberta--------------------------
    while True:
        for event in pygame.event.get(): # captura eventos do jogo
            if event.type == pygame.QUIT:
                pygame.quit()
                return 2
        clock.tick(10)        

        if xb1 > -100:
            xb1 -= veloc_b1
            b1 = pygame.image.load(b1_voa())
            b1 = pygame.transform.scale(b1, (54, 40))
        else:
            xb1 = 1500         
        
        comando = pygame.key.get_pressed()
        if comando[pygame.K_SPACE]:
            return 1	

        comando = pygame.key.get_pressed()
        if comando[pygame.K_x]:
            return 2

        if dino_menu < 10:
            dino_menu += 1
            dino = pygame.image.load(player_menu(dino_menu))
            #dino = pygame.transform.scale(dino, (216, 150))
        else:
            dino_menu = 0
        
        if cont_resultado >= 4:
            cont_resultado = 1
        else:
            cont_resultado += 1
            
        if resultado == 0:
            texto = font.render('Aperte "ESPAÇO" para jogar ou "X" para sair!', True, (0,0,0), (221,248,255))
            pos_texto = texto.get_rect()
            pos_texto.center = (400,30)
                
        elif resultado != 0:
            texto = font2.render('Pontuação: ' + str(resultado), True, cores_resultado(cont_resultado),(221,248,255))
            pos_texto = texto.get_rect()
            pos_texto.center = (400,30)
            texto2 = font3.render('Aperte "ESPAÇO" para jogar novamente ou "X" para sair!', True, (0,0,0), (221,248,255))
            pos_texto2= texto2.get_rect()
            pos_texto2.center = (400,75)
       
        janela.blit(fundo_menu,(0,0))
        janela.blit(chao_menu,(0,500))
        janela.blit(dino,(240,370))   
        janela.blit(arvore1,(520,238))
        janela.blit(arvore2,(0,210))
        janela.blit(placa,(450,440))
        janela.blit(mush1,(720,472))
        janela.blit(mush2,(20,472))
        janela.blit(texto,pos_texto)
        janela.blit(texto2,pos_texto2)
        janela.blit(b1, (xb1,yb1))
        
        pygame.display.update()


