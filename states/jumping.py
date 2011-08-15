import pygame
import state

class Jumping(state.State):
	def __init__(self, mario):
		super(Jumping, self).__init__(mario)
		self.left_jump = "left-jump"
		self.right_jump = "right-jump"
	
	def handle_event(self, event):
		if event.key == pygame.K_a:
			self.mario.jump_forward = 0
			self.mario.rect.move_ip(-self.mario.jump_air_power, 0)
		elif event.key == pygame.K_d:
			self.mario.jump_forward = 0
			self.mario.rect.move_ip(self.mario.jump_air_power, 0)
		return self.jump()	
	
	def no_event(self):
		return self.jump()
		
	def jump(self):
		self.mario.jump_frame += 1
		self.mario.rect.move_ip(self.mario.jump_forward, -self.mario.jump_speed)
		
		if self.mario.jump_frame > self.mario.jump_stop_frame:
			if self.mario.jump_forward != 0:
				if self.mario.direction == "left":
					self.mario.jump_forward = -4
				else:
					self.mario.jump_forward = 4
			return self.fall()			
		
		if self.mario.direction == "left" :
			return self.left_jump
		else:
			return self.right_jump
			
	def __str__(self):
		return "jumping"	