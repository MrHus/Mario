import pygame
import state

class Running(state.State):
	def __init__(self, mario):
		super(Running, self).__init__(mario)
		self.left_running_frames = ["left-run1", "left-run2", "left-run3"]
		self.right_running_frames = ["right-run1", "right-run2", "right-run3"]
		self.frame = 0
	
	def handle_event(self, event):
		if event.key == pygame.K_a:
			self.mario.direction = "left"
			return self.run()
		elif event.key == pygame.K_d:
			self.mario.direction = "right"
			return self.run()
		elif event.key == pygame.K_SPACE:
			if self.mario.direction == "left":
				self.mario.jump_forward = -8
			else:
				self.mario.jump_forward = 8
			return self.jump()
		elif event.key == pygame.K_j:
			return self.run()
		else:
			return self.no_event()	
		
	def no_event(self):
		return self.walk()	
		
	def run(self):
		if self.mario.direction == "left":
			self.mario.rect.move_ip(-self.mario.running_speed, 0)
			return self.get_frame(self.left_running_frames)
		else:
			self.mario.rect.move_ip(self.mario.running_speed, 0)
			return self.get_frame(self.right_running_frames)
			
	def __str__(self):
		return "running"