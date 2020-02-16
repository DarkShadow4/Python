import pygame, math, cmath

# Origen de coordenadas
O = (400, 125)
# Foco
f = 50
F = (O[0]-f, O[1])
# Centro de curvatura
r = 2*f
C = (O[0]-r, O[1])


# cosas iniciales
pygame.init()
canvas = pygame.display.set_mode([1000, 250])

# textos

# objeto
object_font = pygame.font.SysFont("Arial", 12)
object_color = (255, 255, 0)

# imagen
image_font = pygame.font.SysFont("Arial", 12)
image_color = (0, 255, 255)
antialias = True

# datos
sit_font = pygame.font.SysFont("Arial", 12)
sit_color = (100, 100, 100)

done = False
while not done:
    mouse_pos = pygame.mouse.get_pos()


    # espejo
    centro = C
    radio = r
    espejo = pygame.draw.circle(canvas, (255, 0, 255), centro, radio, 1)
    tapar_semicirculo = pygame.draw.rect(canvas, (0, 0, 0), (centro[0]-radio, centro[1]-radio, radio, radio*2))

    # eje, foco, origen de coordenadas y centro de curvatura
    eje = pygame.draw.line(canvas, (100, 100, 100), (0, 125), (500, 125)) # linea del eje

    origen = pygame.draw.circle(canvas, (100, 100, 100), O, 3) # punto del origen de coordenadas
    T_origen = "O" # texto del origen de coordenadas
    surface = sit_font.render(T_origen, antialias, sit_color)
    canvas.blit(surface, (O[0]+10, O[1]-20))

    foco = pygame.draw.circle(canvas, (100, 100, 100), F, 3) # punto del foco
    T_foco = "F" # texto del foco
    surface = sit_font.render(T_foco, antialias, sit_color)
    canvas.blit(surface, (F[0], F[1]+10))

    CdC = pygame.draw.circle(canvas, (100, 100, 100), C, 3) # punto del centro de curvatura
    T_CdC = "C"# texto del centro de curvatura
    surface = sit_font.render(T_CdC, antialias, sit_color)
    canvas.blit(surface, (CdC[0], CdC[1]+10))

    # objeto
    y = O[1]-mouse_pos[1]
    s = mouse_pos[0]-O[0]
    object_pos = (O[0]+s, O[1]-y)
    object_text = "y = {0}; s = {1}".format(y, s)
    pygame.draw.line(canvas, object_color, (O[0]+s, O[1]), object_pos) # objeto

    surface = object_font.render(object_text, antialias, object_color) # datos objeto
    canvas.blit(surface, (mouse_pos[0]+15, mouse_pos[1]-15))

    # TODO: rayos
    # rayos
    # Horizontal
    # ray1 = (255, 0, 0)
    # pygame.draw.line(canvas, ray1, )
    # # Hacia F
    # ray2 = (0, 255, 0)
    # pygame.draw.line(canvas, ray2, )
    # Hacia C
    ray3 = (0, 0, 255)
    # obtengo el punto donde cortan el espejo y el rayo
    CObj = (object_pos[0]-C[0], object_pos[1]-C[1])
    i = False
    for x in range(O[0]-C[0]):
        rayo3 = (C[0]+x*CObj[0], C[1]+x*CObj[1])
        r_y = ((r**2-(x-C[0])**2)**(1/2)) + C[1]

        vec_3 = (rayo3[0].real-C[0], rayo3[1].real-C[0])
        d3 = (vec_3[0]**2 + vec_3[1]**2)**(1/2)
        if math.floor(d3) == r:
            i = (x, r_y.real)

    if i != False:
        pygame.draw.line(canvas, ray3, C, object_pos)
        pygame.draw.line(canvas, ray3, object_pos, i)

    # END TODO: rayos



    # imagen
    if s < 0 and ((1/f)+(1/s)) != 0:
        image_font = pygame.font.SysFont("Arial", 12)
        s_i = int(1/((1/f)+(1/s)))
        y_i = int((s_i/s)*y)

        image_text = "y' = {0}; s' = {1}".format(y_i, s_i)
        image_pos = (O[0]+s_i, O[1]-y_i)
        pygame.draw.line(canvas, image_color, (O[0]+s_i, O[1]), image_pos) # imagen

        surface = image_font.render(image_text, antialias, image_color) # datos imagen
        canvas.blit(surface, (image_pos[0]+15, image_pos[1]-15))
    else:
        image_font = pygame.font.SysFont("Arial", 20)
        image_pos = (10, 10)
        image_text = "No hay imagen"
        surface = image_font.render(image_text, antialias, image_color) # datos imagen
        canvas.blit(surface, image_pos)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                done = True

    pygame.display.flip()
    pygame.time.delay(30) # para que no se vuelva loco el display, hago un delay casi inperceptible para la imagen
                          # pero evita el blinking
    canvas.fill((0, 0, 0)) # reset del canvas para que no se superpongan cosas
    pygame.display.flip()
