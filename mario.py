import pygame
from states import walking, running, jumping, falling, standing

class Mario(pygame.sprite.Sprite):
	"""This class represents Mario"""
	def __init__(self, position, world):
		pygame.sprite.Sprite.__init__(self)
		self.world = world
		
		self.image = pygame.image.load('images/smw_mario_sheet.png')
		self.rect = self.image.get_rect()
		
		self.actions = {	"front":			(245, 75, 20, 30),
	  						"back":				(285, 75, 20, 30),
							
							"left":				(165, 75, 20, 30),
							"left-walking1":	(45, 75, 20, 30),
							"left-walking2":	(5, 75, 20, 30),
							"left-jump":		(165, 115, 20, 30),
							"left-fall":		(125, 115, 20, 30),
							"left-run1":		(165, 155, 20, 30),
							"left-run2":		(125, 155, 20, 30),
							"left-run3":		(85, 155, 20, 30),
							"left-turn":		(5, 115, 20, 30),
							
							"right": 			(205, 75, 20, 30),
						  	"right-walking1": 	(325, 75, 20, 30),
						  	"right-walking2": 	(365, 75, 20, 30),
							"right-jump":		(205, 115, 20, 30),
							"right-fall":		(245, 115, 20, 30),
						  	"right-run1": 		(205, 155, 20, 30),
							"right-run2":		(245, 155, 20, 30),
							"right-run3":		(285, 155, 20, 30),
							"right-turn":		(365, 115, 20, 30)				
					   }
		
		self.action = "left"
		self.area = pygame.rect.Rect(self.actions[self.action])
		self.rect.topleft = position
		
		self.walking_state = walking.Walking(self)
		self.running_state = running.Running(self)
		self.jumping_state = jumping.Jumping(self)
		self.falling_state = falling.Falling(self)
		self.standing_state = standing.Standing(self)
		self.state = self.standing_state
		
		self.direction = "left"
		
		self.jump_frame = 0
		self.jump_stop_frame = 13
		self.jump_forward = 0
		self.jump_air_power = 3 #sideways power in jump
		self.jump_speed = 5
		
		self.fall_speed = 5
		self.fall_tolerance = 3
		
		self.walking_speed = 5
		self.running_speed = 8
	
	def handle_event(self, event):
		if self.state != self.jumping_state:
			self.check_if_falling()
			
		if event.type == pygame.KEYDOWN:
			self.action = self.state.handle_event(event)
		else:
			self.action = self.state.no_event()		
		
	def handle_animation(self):
		self.check_bounds()	
		self.area = pygame.rect.Rect(self.actions[self.action])
		
	def check_if_falling(self):
		for solid in self.world.solids:
			if (self.rect.x >= solid[0] and self.rect.x <= solid[1] and 
				solid[2] > (self.rect.y - self.fall_tolerance) and solid[2] < (self.rect.y + self.fall_tolerance)):	
				self.rect.y = solid[2]
				return False
		
		self.state = self.falling_state
		return True
		
	def check_bounds(self):
		if self.rect.x < -10:
			 self.rect.x = 335
			
		if self.rect.x > 335:
			self.rect.x = -5
			
		if self.rect.y > 432:
			self.rect.y = 0												