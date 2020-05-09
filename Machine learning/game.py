import pygame; from pygame.locals import *;
def main():
	clock =pygame.time.Clock()
	instance = pygame.display.set_mode((800, 450))#,pygame.FULLSCREEN|pygame.HWSURFACE);

	running = True;

	flappyFloor =pygame.transform.scale2x(pygame.image.load("flappy floor.png"));
	flappyBall = (pygame.image.load("flappy orb.png"));
	flappyPole = (pygame.image.load("flappy pole.png"));
	flappyPoleInv = (flappyPole, True, False);
	flappyBlast =(pygame.image.load("flappy blast.png"));
	floorX, ballX, blastX = 0, 0, 0
	ballY = 185
	gravAccel = 0
	startchecker = False
	spacepressed = False
	gravApplier = 1

	
	pygame.init();
	while running:
		pygame.Surface.fill(instance, (230, 240, 230))
		drawFlappyFloor = instance.blit(flappyFloor, (floorX, 370));
		drawFlappyFloorV2 = instance.blit(flappyFloor, (800 + floorX, 370))
		ball = instance.blit(flappyBall, (30, ballY))
		if floorX == -800:
			floorX = 0
		ballY =  ballY + gravAccel

		if startchecker:
			if gravApplier != 2:
				gravApplier += 1;
			else:
				
				gravAccel += 1
				gravApplier = 1;
				
		if spacepressed:
			gravAccel = -9

		floorX, ballX, blastX = floorX - 2, ballX - 2, blastX - 2
		#print(ballY, gravAccel, startchecker, spacepressed)
		spacepressed = False
		for event in pygame.event.get():
			if event.type == QUIT or event.key == pygame.K_ESCAPE:
				running = False;
			elif event.key == pygame.K_SPACE and event.type == pygame.KEYDOWN:
				startchecker = True
				spacepressed = True

	
		
		pygame.display.update()
		clock.tick(60)
if __name__ == '__main__':
	main()

