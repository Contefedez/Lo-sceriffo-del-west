import pygame
from random import randint,choice
import sys

# class Ostacoli(pygame.sprite.Sprite):
#     def __init__(self,type):
#         super().__init__()

#         if type == "mosca":
#             bersaglio = pygame.image.load("bersaglio.png").convert_alpha()
#             self.ostacoli = bersaglio
#         if type == "bandito":
#             bandito = pygame.image.load("bandito.png").convert_alpha()
#             self.ostacoli = bandito
            
#         self.image = self.ostacoli
    
#     def spawn(self):
        

#     def destroy(self):
#         if self.rect.x < -100:
#             self.kill()



	
    


pygame.init()
larghezza = 1000
altezza = 500
screen = pygame.display.set_mode((larghezza,altezza))
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
sfondo_game = pygame.image.load("sfondo.png").convert()
sfondo_game = pygame.transform.smoothscale(sfondo_game, (1000,500))
bersaglio = pygame.image.load("bersaglio.png").convert()
inizio = pygame.image.load("start.png").convert()
volume = pygame.image.load("volume.png").convert()
audio = pygame.image.load("audio.png").convert()
best_score = pygame.image.load("best score.png").convert()
dollari = pygame.image.load("dollari.png").convert()
punteggio = pygame.image.load("punteggio.png").convert()
canzone = pygame.image.load("canzone.png").convert()
indietro = pygame.image.load("back.png").convert()
#audio

#classi
class Button():
	def __init__(self, pos, text_input, colore = "White" ):
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.text_input = text_input
        self.text = font.render(self.text_input, True, colore)
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

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("black")

        PLAY_BACK = Button( pos=(640, 460), text_input="BACK")
        PLAY_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.input(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("white")
        
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

        MENU_MOUSE_POS = pygame.mouse.get_pos()
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
