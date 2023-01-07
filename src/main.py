import pygame
from rps.rps import RpsGame

class App:
	def __init__(self):
		self.setup()

	def setup(self):
		self.timer = pygame.time.Clock()
		self.FPS = 60

		dimensions = (1280, 720)
		self.screen = pygame.display.set_mode(dimensions)
		pygame.display.set_caption("PyGame Gamebox")

		self.loaded = RpsGame()

	def cycle(self):
		events = pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT:
				exit()
		# ^ for closing the window

		self.loaded.run()

		pygame.display.update()
		self.timer.tick(self.FPS)
		# ^ for the games I'm making, delta time is unnecessary

	def start(self):
		self.running = True
		while self.running:
			self.cycle()


	
def main():
	app = App()
	app.start()


if __name__ == '__main__':
	main()