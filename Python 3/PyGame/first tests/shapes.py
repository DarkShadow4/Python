import pygame

pygame.init()

canvas = pygame.display.set_mode([500, 250])

#rect(surface, color, (x, y, width, height) [, line width])
pygame.draw.rect(canvas, (255, 255, 255), (225, 100, 50, 50), 1)
#circle(surface, color, center (x, y), radio [, line width])
pygame.draw.circle(canvas, (0, 255, 0), (250, 125), 50, 1)
# ellipses are defined like rectangles
#
#line(surface, color, start (x, y), end (x, y) [, line width])
pygame.draw.line(canvas, (0, 0, 255), (0, 0), (500, 250))
pygame.draw.line(canvas, (0, 0, 255), (500, 0), (0, 250))

# a general polygon needs a list of points
triangle = [[300, 150], [250, 100], [200, 150]]
#for a triangle it might be given 3 points
pygame.draw.polygon(canvas, (255, 0, 0), triangle, 1)


pygame.display.flip()
