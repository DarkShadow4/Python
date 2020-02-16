import pygame

pygame.init()

canvas = pygame.display.set_mode([500, 250])

font = pygame.font.SysFont("Arial", 24)

done = False
while not done:

    canvas.fill((0, 0, 0))
    mouse_pos = pygame.mouse.get_pos()
    text = str(mouse_pos)
    antialias = True
    color = (0, 255, 0)
    surface = font.render(text, antialias, color)
    canvas.blit(surface, mouse_pos)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                done = True

    pygame.display.flip()
