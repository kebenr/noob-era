import pygame
import time
import random
import os
from random import randint, choice
from sys import exit
pygame.font.init()

WIDTH, HEIGHT = 900, 500
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('bork la')

DOG = pygame.image.load(os.path.join('ass','dog.png')).convert_alpha()
DOG = pygame.transform.rotozoom(DOG,0,2)

PETAL = pygame.image.load(os.path.join('ass','petal_scaled.png')).convert_alpha()
# PETAL = pygame.transform.rotozoom(PETAL,randint(0,360),choice([1,.5,.7]))

POOP = pygame.image.load(os.path.join('ass','poo_scaled.png')).convert_alpha()
# POOP = pygame.transform.rotozoom(POOP,randint(0,360),choice([1]))

BG = pygame.image.load(os.path.join('ass','dog_back.png')).convert_alpha()

DOG_END = pygame.transform.rotozoom(DOG,0,3)
DOG_END_RECT = DOG_END.get_rect(center = (450,250))

class Dog(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = DOG
		self.mask = pygame.mask.from_surface(self.image)
		self.rect = pygame.mask.Mask.get_rect(self.mask)
		self.rect.midbottom = (450,495)
		self.gravity = 0

	def player_input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE] and self.rect.bottom >= 495:
			self.gravity -= 20
		if keys[pygame.K_a] and self.rect.left >= -45:
			self.rect.x -= 7
		if keys[pygame.K_d] and self.rect.right <= 945:
			self.rect.x += 7

	def apply_gravity(self):
		self.gravity += 1
		self.rect.y += self.gravity
		if self.rect.bottom >= 495:
			self.rect.bottom = 495
			self.gravity = 0

	def update(self):
		self.player_input()
		self.apply_gravity()

class Stuff(pygame.sprite.Sprite):
	def __init__(self,type):
		super().__init__()

		if type == 'petal':
			self.image = PETAL

		else:
			self.image = POOP
		
		self.mask = pygame.mask.from_surface(self.image)
		self.rect = pygame.mask.Mask.get_rect(self.mask)
		self.rect.center = (random.randint(1,899),random.randint(-700,-20))

	def stuff_movement(self):
		self.rect.y += 5

	def die(self):
		if self.rect.y >= HEIGHT:
			self.kill()

	def update(self):
		self.stuff_movement()
		self.die()

def main():
	run = True
	FPS = 60
	main_font = pygame.font.SysFont('comicsans', 20)
	lost_font = pygame.font.SysFont('comicsans', 69)
	stuff = []
	amount = 0
	score = 0
	lost_count = 0
	difficulty = 500

	stuff_timer = pygame.USEREVENT + 1
	pygame.time.set_timer(stuff_timer,difficulty)
	
	player = pygame.sprite.GroupSingle()
	player.add(Dog())

	stuff_group = pygame.sprite.Group()

	clock = pygame.time.Clock()
	start_time = int(pygame.time.get_ticks()/1000) 

	lost = False


	def display_score():
		current_time = int(pygame.time.get_ticks()/1000) - start_time
		score_label = main_font.render(f'score: {current_time}', 1, 'mistyrose1')
		screen.blit(score_label, (WIDTH/2 - score_label.get_width()/2, 10))
		return current_time



	def redraw_screen():
		screen.blit(BG, (0,0))

		display_score()

		player.draw(screen)
		player.update()

		stuff_group.draw(screen)
		stuff_group.update()


		if lost:	
			lost_label = lost_font.render(f'final score: {score}', 1, 'mistyrose1')
			screen.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 250))

		pygame.display.update()

	while run:
		clock.tick(FPS)

		redraw_screen()

		if pygame.sprite.spritecollide(player.sprite,stuff_group,True,pygame.sprite.collide_mask):
			score = display_score()
			lost = True

		if lost:
			lost_count += 1
			if lost_count > FPS*3:
				run = False
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			
			if event.type == stuff_timer and lost == False:
				stuff_group.add(Stuff(choice(['petal','poop'])))
				if difficulty > 100:
					difficulty -= 1
					pygame.time.set_timer(stuff_timer,difficulty)

def main_menu():
    title_font = pygame.font.SysFont('comicsans', 69)
    run = True
    while run:
        screen.blit(BG, (0,0))
        screen.blit(DOG_END, DOG_END_RECT)
        title_label = title_font.render('press mouse go', 1, ('mistyrose1'))
        screen.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 350))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
            	run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
            	main()
    
    pygame.quit()
    exit()

main_menu()