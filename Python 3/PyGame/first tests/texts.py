import pygame

pygame.init()

canvas = pygame.display.set_mode([500, 250])

# para crear textos es necesario usar el objeto pygame.font
# SysFont(name, size, bold=False, italic=False)
font = pygame.font.SysFont("Arial", 24)

# render(text, antialias, color, background=None)
antialias = True

text = "Yes"
text_surface = font.render(text, antialias, (255, 255, 255))
canvas.blit(text_surface, (250, 125))

text = "No"
text_surface = font.render(text, antialias, (255, 255, 255))
canvas.blit(text_surface, (300, 125))


pygame.display.flip()
