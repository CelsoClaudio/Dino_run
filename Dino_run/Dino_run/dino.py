from random import randint
from pygame.locals import *
import pygame
import os

pygame.init()

#-----------------------------------------------------------------
def limpa_tela():
    os.system('cls' if os.name=='nt' else 'clear')
    return
#-----------------------------------------------------------------
def cria_tela():
    janela = pygame.display.set_mode((800,600))# cria janela do jogo
    return janela
#-----------------------------------------------------------------
def escolhe_som(som):
    audio = {1:'audio\m1.mp3', 2:'audio\m2.mp3'}
    return audio[som]
#-----------------------------------------------------------------
def player(player, pula):
    opcao = {1:'image\mr1.png',2:'image\mr2.png',3:'image\mr3.png',4:'image\mr4.png',
             5:'image\mr5.png',6:'image\mr6.png',7:'image\mr7.png',8:'image\mr8.png',
             9:'image\mj1.png',10:'image\mj2.png',11:'image\mj3.png',12:'image\mj4.png',
             13:'image\mj5.png',14:'image\mj6.png',15:'image\mj7.png',16:'image\mj8.png',
             17:'image\mj8.png',18:'image\mj8.png',19:'image\mj8.png',20:'image\mj8.png',
             21:'image\mj9.png',22:'image\mj10.png',23:'image\mj11.png',24:'image\mj12.png',
             25:'image\ma1.png',26:'image\ma2.png',27:'image\ma3.png',28:'image\ma4.png',
             29:'image\ma5.png',30:'image\ma5.png',31:'image\ma6.png',32:'image\ma6.png',
             33:'image\ma7.png',34:'image\ma7.png',35:'image\ma8.png',36:'image\ma8.png',
             37:'image\ma4.png',38:'image\ma3.png',39:'image\ma2.png',40:'image\ma1.png',             
             }
    if pula == 0:
        return opcao[player]
    elif pula == 1:
        return opcao[(player + 8)]
    elif pula == 2:
        return opcao[(player + 24)]      
#-----------------------------------------------------------------
def obstaculo():  
    tipo = randint(1, 5)
    opcao = {1:('image\mstone.png',440), 2:('image\mtree.png',385),
             3:('image\mcrate.png',440), 4:('image\mbush1.png',440),
             5:('image\mbush2.png',440)} 
    return opcao[tipo]

#-----------------------------------------------------------------
def obstaculo_voa():  
    tipo = randint(1, 3)
    opcao = {1:('image\mb1.png',340),2:('image\mb2.png',340),
             3:('image\mb3.png',340)}
     
    return opcao[tipo]
#-----------------------------------------------------------------
def tela_jogo():
    xfd = 0
    yfd = 0

    xd = 100
    yd = 370

    xch = 0
    ych = 500

    veloc_fd = 5
    veloc_ch = 20
    alt_pulo = 25

    ndino = 1
    puladino = 0
    abaixadino = 0
    voa = 0
    obt = randint(1,3)
    
    pula = 0
    cont = 0

    xobj = randint(900, 2000)
    fundo = pygame.image.load('image\md.png')
    cmd = pygame.image.load('image\cmd.png')
    janela = cria_tela()
    obj1 = obstaculo()
    yobj = obj1[1]
    cont_aceleracao = 0

    #objetos com tratamento de colisão-------------------------------------------
    obj = pygame.image.load(obj1[0]).convert_alpha()
    obj_mask = pygame.mask.from_surface(obj)
    obj_rect = obj.get_rect()

    dino = pygame.image.load(player(1, 0)).convert_alpha()
    dino_mask = pygame.mask.from_surface(dino)
    dino_rect = dino.get_rect()
    # janela com placar de pontos-------------------------------------------------------
    placar = 0
    font = pygame.font.SysFont('arial black',30)
    texto = font.render('Placar: ' + str(placar), True, (0,0,0), (221,248,255))
    pos_texto = texto.get_rect()
    pos_texto.center = (120,30)
    #-----------------------------------------------------------------------------------

    chao = pygame.image.load('image\ch.png')
    pygame.display.set_caption('Dino -> Jogar')
    clock = pygame.time.Clock()

    pygame.mixer.music.load('audio\m3.mp3')
    pygame.mixer.music.play()


    # cria laço de repetição para manter janela aberta---------------------------
    while True:
        clock.tick(15)

        if cont_aceleracao < 50:
            cont_aceleracao += 1
        else:
            cont_aceleracao = 0
            veloc_ch += 2 
        placar += 1
        texto = font.render('Placar: ' + str(placar), True, (0,0,0), (221,248,255)) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return placar
            
        xch -= veloc_ch
        if xch <= -800:
            xch = 0
        xfd -= veloc_fd
        if xfd <= -800:
            xfd = 0

        xobj -= veloc_ch
        if xobj < -100:
            obt = randint(1,3)
            xobj = randint(900, 2000)
        if obt < 3:            
            obj1 = obstaculo()
            yobj = obj1[1]
            obt = 5
        elif obt == 3:
            yobj = 350
            if voa < 3:              
                obj1 = obstaculo_voa()
                voa += 1
            else:
                voa = 1
        obj = pygame.image.load(obj1[0]).convert_alpha()
        #comandos de pular e agachar-------------------------------------------------------------
        comandos = pygame.key.get_pressed()
        if (comandos[pygame.K_w] or comandos[pygame.K_UP]) and pula == 0:
            pula = 1
            pygame.mixer.music.load(escolhe_som(1))
            pygame.mixer.music.play()
            
        if (comandos[pygame.K_s] or comandos[pygame.K_DOWN])  and pula == 0:
            pula = 2
            pygame.mixer.music.load(escolhe_som(2))
            pygame.mixer.music.play()
        #------------------------------------------------------------------------------
        #colisão
        offset = (xobj - xd, yobj - yd)
        result = dino_mask.overlap(obj_mask, offset)
        if result:
            return (placar-1)

        #movimentos do dinossauro-------------------------------
        if pula == 0:
            ndino += 1
            if ndino > 8:
                ndino = 1
            dino = pygame.image.load(player(ndino, pula)).convert_alpha()        

        elif pula == 1:
            puladino += 1
            if puladino < 16:           
                dino = pygame.image.load(player(puladino, pula)).convert_alpha()
                if cont < 8:
                    yd -= alt_pulo
                    cont += 1
                else:
                    yd += alt_pulo
            else:
                puladino = 0
                pula = 0
                cont = 0
                yd = 365
                pygame.mixer.music.load('audio\m3.mp3')
                pygame.mixer.music.play()

        elif pula == 2:
            yd = 413
            abaixadino += 1
            if abaixadino < 16:
                dino = pygame.image.load(player(abaixadino, pula)).convert_alpha()
                
            else:
                abaixadino = 0
                pula = 0
                cont = 0
                yd = 365
                pygame.mixer.music.load('audio\m3.mp3')
                pygame.mixer.music.play()


                
        #-----------------------------------------------------------  
        janela.blit(fundo,(int(xfd),int(yfd)))
        janela.blit(chao,(int(xch),int(ych)))
        janela.blit(dino,(int(xd),int(yd)))
        janela.blit(obj,(int(xobj),int(yobj)))
        janela.blit(texto, pos_texto)
        janela.blit(cmd,(550,5))
        pygame.display.update()

