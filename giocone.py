import pygame

pygame.init()


screen = pygame.display.set_mode((1000,500))
pygame.display.set_caption("Lo sceriffo del west")
clock = pygame.time.Clock()
font = pygame.font.Font(None,50)
game_active = False
tempo_inizio = 0
punteggio = 0
timer = pygame.USEREVENT + 1
pygame.time.set_timer(timer,1000)
start = True

#immagini
sfondo_menu = pygame.image.load("home.png").convert()
sfondo_menu = pygame.transform.smoothscale(sfondo_menu, (1000,500))




#testi
titolo_gioco = font.render("LO SCERIFFO DEL WEST", False, (64,64,64))
rett_titolo = titolo_gioco.get_rect(center = (400,100))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((0,0,0))
    screen.blit(sfondo_menu,(0,0))
    screen.blit(titolo_gioco,rett_titolo)

    pygame.display.update()
    clock.tick(60)