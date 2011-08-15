import pygame
import mario
import world

screen = pygame.display.set_mode((336, 432))
pygame.display.set_caption("Mario Mayhem")
clock = pygame.time.Clock()

world = world.World()
mario = mario.Mario((250, 355), world)

running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	mario.handle_event(event)
	mario.handle_animation()
			
	screen.fill(pygame.Color('black'))	
	screen.blit(world.image, world.rect)
	screen.blit(mario.image, mario.rect, mario.area)

	pygame.display.flip()		
	clock.tick(15)