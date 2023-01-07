import pygame

class RpsGame:
	def __init__(self):
		self.screen = pygame.display.get_surface()

	def draw(self):
		self.screen.fill((255, 255, 255))

	def run(self):
		self.draw()