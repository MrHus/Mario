class State(object):
	"""This is the template for all the other states"""
	
	def __init__(self, mario):
		self.mario = mario
	
	def jump(self):
		self.mario.state = self.mario.jumping_state
		return self.mario.state.jump()	
	
	def fall(self):
		self.mario.state = self.mario.falling_state
		return self.mario.state.fall()
		
	def walk(self):
		self.mario.state = self.mario.walking_state
		return self.mario.state.walk()
		
	def run(self):
		self.mario.state = self.mario.running_state
		return self.mario.state.run()
	
	def stand(self):
		self.mario.state = self.mario.standing_state
		return self.mario.state.stand()
		
	def get_frame(self, frame_set):
		self.frame += 1

		if self.frame > (len(frame_set) - 1):
			self.frame = 0

		return frame_set[self.frame]			
		
	def __str__(self):
		return "Default state"	