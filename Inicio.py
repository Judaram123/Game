import pygame
# ------------------------------------------------------------
BLANCO =[255,255,255]
VERDE=[0,255,0]
ROJO=[255,0,0]
NEGRO=[0,0,0]
AZUL=[30,175,227]
ROSA= [255,0,255]
MORADO = [131,0,255]

ANCHO  = 860
ALTO = 640
CENTRO = (ANCHO//2,ALTO//2)
# ------------------------------------------------------------
def main():
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    fin=False
    pantalla.fill(NEGRO)
    pygame.display.flip()
    #CICLO PRINCIPAL
    while not fin:
        #GESTION DE EVENTOS
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                fin=True
    pass
# ------------------------------------------------------------
if __name__ == '__main__':
    main()
