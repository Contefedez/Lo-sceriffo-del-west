import pygame
from random import randint
import sys

pygame.init()
larghezza = 1000
altezza = 500
screen = pygame.display.set_mode((larghezza,altezza))
pygame.display.set_caption("Lo sceriffo del west")
font = pygame.font.Font("docktrin.ttf",50)
game_active = False
bianco = (255,255,255)

#tempo
clock = pygame.time.Clock()
inizio_round = pygame.time.get_ticks()
durata_round = 30

#round
punteggio = 0
colpi = 0
max_colpi = 10

#bersagli
raggio = 30
bersagli = []
bersaglio = pygame.image.load("bersaglio.png").convert()
rettangolo_bersaglio = bersaglio.get_rect(center = (30,30))
bandito = pygame.image.load("bandito.png").convert()
rettangolo_bandito = bandito.get_rect(center = (30,30))

#testi
titolo = font.render("LO SCERIFFO DEL WEST", False, (bianco))
rettangolo_titolo = titolo.get_rect(center= (150,90))
canzoni = font.render("CANZONI", False, (bianco))
rettangolo_canzoni = canzoni.get_rect(center= (150,90))

#immagini
sfondo_menu = pygame.image.load("home.png").convert()
sfondo_menu = pygame.transform.smoothscale(sfondo_menu, (1000,500))
sfondo_game = pygame.image.load("sfondo.png").convert()
sfondo_game = pygame.transform.smoothscale(sfondo_game, (1000,500))
inizio = pygame.image.load("start.png").convert()
volume = pygame.image.load("volume.png").convert()
audio = pygame.image.load("audio.png").convert()
best_punteggio = pygame.image.load("best punteggio.png").convert()
dollari = pygame.image.load("dollari.png").convert()
punteggio = pygame.image.load("punteggio.png").convert()
canzone = pygame.image.load("canzone.png").convert()
indietro = pygame.image.load("back.png").convert()

#audio
canzone1 = pygame.mixer.Sound("canzone1.mp3")
canzone2 = pygame.mixer.Sound("canzone2.mp3")
sparo = pygame.mixer.Sound("shot.mp3")

#classi
class Button():
	def __init__(self, pos, testo):
		self.testo = testo
        self.x_pos = pos[0]
		self.y_pos = pos[1]
        self.text = font.render(self.testo, True, bianco)
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        
	def update(self, screen):
		screen.blit(self.text, self.text_rect)
	def input(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False
#testi
titolo_gioco = font.render("LO SCERIFFO DEL WEST", False, (64,64,64))
rett_titolo = titolo_gioco.get_rect(center = (400,100))

def spawn():
    z = randint(0,2)
    if z == 1:
        x = randint(raggio, larghezza - raggio)
        y = randint(100, altezza - raggio)
        bersagli.append((x,y,z))
    else:
        z = 2
        x = randint(raggio, larghezza - raggio)
        y = randint(100, altezza - raggio)
        bersagli.append((x,y,z))
        
def play():
    while True:
        tempo_corrente = pygame.time.get_ticks()
        tempo = (tempo_corrente - inizio_round) / 1000
        screen.blit(sfondo_game, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and colpi > 0 and tempo < durata_round:
                if event.button == 1:  
                    sparo.play()
                    for bersa in bersagli:
                        target_x, target_y = bersa[0], bersa[1]
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        distance = ((target_x - mouse_x) ** 2 + (target_y - mouse_y) ** 2) ** 0.5
                        if distance <= raggio:
                            bersagli.remove(bersa)
                            spawn()
                            punteggio += 1
                            colpi += 2

                            if colpi > max_colpi:
                                colpi = max_colpi
                    
                    else:  
                        colpi -= 1
                    
                    if colpi == 0:
                       main_menu()
        
        if len(bersagli) < 5 and tempo < durata_round:
            spawn()

        for bersaglioso in bersagli:
            if bersaglioso[2] == 1:
                rettangolo_bersaglio.center = (bersaglioso[0], bersaglioso[1])
                screen.blit(bersaglio,rettangolo_bersaglio)
            if bersaglioso[2] == 2:
                rettangolo_bandito.center = (bersaglioso[0], bersaglioso[1])
                screen.blit(bandito,(bersaglioso[0],bersaglioso[1]))

        score_text = font.render(f"Score: {punteggio}", True, bianco)
        screen.blit(score_text, (125, 10))

        shots_text = font.render(f"Shots: {colpi}", True, bianco)
        screen.blit(shots_text, (330, 10))
        
        while tempo_rimasto > 0:
            tempo_rimasto = durata_round - tempo
            time_text = font.render(f"Tempo Rimasto: {tempo_rimasto:.1f}", True, bianco)
            screen.blit(time_text, (530, 10))
        main_menu()
                
        pygame.display.update()
    
def options():
    while True:
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(sfondo_menu,(0,0))
        back_opzioni = Button( pos=(840, 460), text_input="BACK")
        back_opzioni.update(screen)
        canzone_1 = Button(pos = (500,400), text = "S-1")
        canzone_2 = Button(pos = (700,400), text = "S-2")
        screen.blit(canzoni,rettangolo_canzoni)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_opzioni.input(mouse_pos):
                    main_menu()
                if canzone_1.input(mouse_pos):
                    canzone1.play()
                if canzone_2.input(mouse_pos):
                    canzone2.play()

        pygame.display.update()

def main_menu():
    while True:
        screen.blit(sfondo_menu, (0, 0))
        mouse_pos = pygame.mouse.get_pos()
        play = Button( pos=(640, 250), text_input="PLAY")
        options = Button( pos=(640, 400), text_input="OPTIONS")
        screen.blit(titolo,rettangolo_titolo)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play.input(mouse_pos):
                    play()
                if options.input(mouse_pos):
                    options()
                

        pygame.display.update()

main_menu()

clock.tick(60)
