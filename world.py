import pygame

class World(object):
	def __init__(self):
		
		self.image = pygame.image.load("images/background.png")
		self.rect = self.image.get_rect()
		
		self.solids = [
						[-10, 290, 355],
						[70, 165, 291],
						[38, 120, 228],
						[70, 149, 164],
						[119, 216, 116],
						[259, 336, 132]
					  ]