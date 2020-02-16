import pygame

pygame.init()

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

canvas = pygame.display.set_mode([500, 250])
done = False
while not done:

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_w:
                canvas.fill(WHITE)
            elif event.key == pygame.K_a:
                canvas.fill(BLUE)
            elif event.key == pygame.K_s:
                canvas.fill(RED)
            elif event.key == pygame.K_d:
                canvas.fill(BLACK)
            elif event.key == pygame.K_e:
                canvas.fill(GREEN)
            elif event.key == pygame.K_q:
                done = True

        pygame.display.flip()
