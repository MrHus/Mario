import pygame
import state

class Falling(state.State):
	def __init__(self, mario):
		super(Falling, self).__init__(mario)
		self.left_fall = "left-fall"
		self.right_fall = "right-fall"
	
	def handle_event(self, event):
		if event.key == pygame.K_a:
			self.mario.jump_forward = 0
			self.mario.rect.move_ip(-self.mario.jump_air_power, 0)
		elif event.key == pygame.K_d:
			self.mario.jump_forward = 0
			self.mario.rect.move_ip(self.mario.jump_air_power, 0)	
		return self.fall()
	
	def no_event(self):
		return self.fall()
		
	def fall(self):
		self.mario.rect.move_ip(self.mario.jump_forward, self.mario.fall_speed)
		
		if not self.mario.check_if_falling():
			self.mario.jump_frame = 0
			self.mario.jump_forward = 0
			return self.stand()
		
		if self.mario.direction == "left":
			return self.left_fall
		else:
			return self.right_fall	
			
	def __str__(self):
		return "falling"