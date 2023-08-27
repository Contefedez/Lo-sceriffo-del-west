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
bersaglio = pygame.image.load("bersaglio.png").convert()
rettangolo_bersaglio = bersaglio.get_rect(center = (30,30))
bandito = pygame.image.load("bandito.png").convert()
rettangolo_bandito = bandito.get_rect(center = (30,30))

#testi
canzoni = font.render("CANZONI", False, (bianco))
rettangolo_canzoni = canzoni.get_rect(center= (350,100))

#immagini
sfondo_menu = pygame.image.load("home.png").convert()
sfondo_menu = pygame.transform.smoothscale(sfondo_menu, (1000,500))
sfondo_game = pygame.image.load("sfondo.png").convert()
sfondo_game = pygame.transform.smoothscale(sfondo_game, (1000,500))
inizio = pygame.image.load("start.png").convert()

#audio
canzone1 = pygame.mixer.Sound("canzone1.mp3")
canzone2 = pygame.mixer.Sound("canzone2.mp3")
sparo = pygame.mixer.Sound("shot.mp3")

#classi
class Button():
	def __init__(self, image, pos, font, text_input, colore, secondocolore):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.colore, self.secondocolore = colore, secondocolore
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.colore)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def input(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.secondocolore)
		else:
			self.text = self.font.render(self.text_input, True, self.colore)


def get_font(size): 
    return pygame.font.Font("docktrin.ttf", size)

def spawn(bersagli):
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
    screen.blit(sfondo_game, (0,0))
    tempo_corrente = pygame.time.get_ticks()
    tempo = (tempo_corrente - inizio_round) / 1000
    punteggio = 0
    colpi = 10
    bersagli = []
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
                        spawn(bersagli)
                        punteggio += 1
                        colpi += 2
                    else:  
                        colpi -= 1
                    if colpi == 0:
                       main_menu()
    
    if len(bersagli) < 5 and tempo < durata_round:
        spawn(bersagli)

    for bersaglioso in bersagli:
        if bersaglioso[2] == 1:
            rettangolo_bersaglio.center = (bersaglioso[0], bersaglioso[1])
            screen.blit(bersaglio,rettangolo_bersaglio)
        if bersaglioso[2] == 2:
            rettangolo_bandito.center = (bersaglioso[0], bersaglioso[1])
            screen.blit(bandito,rettangolo_bandito)

    score_text = font.render(f"Score: {punteggio}", True, bianco)
    screen.blit(score_text, (125, 10))

    shots_text = font.render(f"Shots: {colpi}", True, bianco)
    screen.blit(shots_text, (330, 10))
    
    tempo_rimasto = durata_round - tempo
    while tempo_rimasto > 0:
        time_text = font.render(f"Tempo Rimasto: {tempo_rimasto:.1f}", True, bianco)
        screen.blit(time_text, (530, 10))
    main_menu()
            
    pygame.display.update()
    
def options():
    while True:
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(sfondo_menu,(0,0))
        back_opzioni = Button( image=None, pos=(420, 325), font=get_font(75),text_input="BACK", colore="White", secondocolore="Green")
        back_opzioni.update(screen)
        canzone_1 = Button( image=None, pos = (270,200), font=get_font(75),text_input = "S-1", colore="White", secondocolore="Green" )
        canzone_2 = Button(image=None,pos = (450,200),font=get_font(75), text_input = "S-2", colore="White", secondocolore="Green")
        screen.blit(canzoni,rettangolo_canzoni)
        back_opzioni.changeColor(mouse_pos)
        back_opzioni.update(screen)
        canzone_1.changeColor(mouse_pos)
        canzone_1.update(screen)
        canzone_2.changeColor(mouse_pos)
        canzone_2.update(screen)

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
        titolo_gioco = get_font(80).render("LO SCERIFFO DEL WEST", False, bianco)
        rettangolo_titolo = titolo_gioco.get_rect(center = (380,100))
        mouse_pos = pygame.mouse.get_pos()
        play_b = Button( image=None,pos=(340, 200),font=get_font(60), text_input="PLAY",colore="White", secondocolore="Green")
        options_b = Button( image=None,pos=(340, 300),font=get_font(60), text_input="OPTIONS",colore="White", secondocolore="Green")
        screen.blit(titolo_gioco,rettangolo_titolo)
        for button in [play_b, options_b]:
            button.changeColor(mouse_pos)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_b.input(mouse_pos):
                    play()
                if options_b.input(mouse_pos):
                    options()
                

        pygame.display.update()

main_menu()

clock.tick(60)
