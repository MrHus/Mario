import pygame
import state

class Standing(state.State):
	def __init__(self, mario):
		super(Standing, self).__init__(mario)
		self.left_stand = "left"
		self.right_stand = "right"

	def handle_event(self, event):
		if event.key == pygame.K_a:
			self.mario.direction = "left"
			return self.walk()
		elif event.key == pygame.K_d:
			self.mario.direction = "right"
			return self.walk()
		elif event.key == pygame.K_SPACE:
			return self.jump()
		elif event.key == pygame.K_j:
			return self.run()
		else:
			return self.no_event()
					
	def no_event(self):
		return self.stand()
			
	def stand(self):
		if self.mario.direction == "left":
			return self.left_stand
		else:
			return self.right_stand
			
	def __str__(self):
		return "standing"