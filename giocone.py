import pygame
from random import randint,choice
import sys

pygame.init()
larghezza = 1000
altezza = 500
screen = pygame.display.set_mode((larghezza,altezza))
pygame.display.set_caption("Lo sceriffo del west")
font = pygame.font.Font(None,50)
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
bandito = pygame.image.load("bandito.png").convert()

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

#classi
class Button():
	def __init__(self, pos, text_input, colore = "bianco" ):
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.text_input = text_input
        self.text = self.font.render(self.text_input, True, colore)
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
        
# def mostra_score():
#     tempo = int((pygame.time.get_ticks() - tempo_inizio) / 1000)
#     score = test_font.render(f"Punteggio:{tempo}", False, (64,64,64))
#     rettangolo_score = score.get_rect(center= (400,50))
#     screen.blit(score, rettangolo_score)
#     return tempo

def play():
    while True:
        tempo_corrente = pygame.time.get_ticks()
        tempo = (tempo_corrente - inizio_round) / 1000
        screen.blit(sfondo_game, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and colpi > 0 and tempo < round_duration:
                if event.button == 1:  # Tasto sinistro del mouse
                    for target in bersagli:
                        target_x, target_y = target
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        distance = ((target_x - mouse_x) ** 2 + (target_y - mouse_y) ** 2) ** 0.5
                        if distance <= raggio:
                            bersagli.remove(target)
                            spawn()
                            punteggio += 1
                            colpi += 2

                            if colpi > max_colpi:
                                colpi = max_colpi
                    
                    else:  
                        colpi -= 1
                    
                    if colpi == 0:
                       game_active = False
        
        if len(bersagli) < 5 and tempo < durata_round:
            spawn()

        score_text = font.render(f"Score: {punteggio}", True, bianco)
        screen.blit(score_text, (125, 10))

        shots_text = font.render(f"Shots: {colpi}", True, bianco)
        screen.blit(shots_text, (330, 10))
        
        while tempo_rimasto > 0:
            tempo_rimasto = durata_round - tempo
            time_text = font.render(f"Tempo Rimasto: {tempo_rimasto:.1f}", True, bianco)
            screen.blit(time_text, (530, 10))
        game_active = False
                
        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("bianco")
        
        OPTIONS_BACK = Button( pos=(640, 460), text_input="BACK")

        
        OPTIONS_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.input(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        screen.blit(sfondo_menu, (0, 0))

        mouse_pos = pygame.mouse.get_pos()
        PLAY_BUTTON = Button( pos=(640, 250), text_input="PLAY")
        OPTIONS_BUTTON = Button( pos=(640, 400), text_input="OPTIONS")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.input(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.input(MENU_MOUSE_POS):
                    options()
                

        pygame.display.update()

main_menu()

clock.tick(60)
