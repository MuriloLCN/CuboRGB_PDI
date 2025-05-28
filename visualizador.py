from edudraw import EduDraw
import numpy as np
import pygame

matriz_cubo = None
pagina = 0

width, height = 500, 500
s = EduDraw(width, height)

def setup():
    global matriz_cubo
    matriz_cubo = np.load("matriz.npy")
    s.change_default_font('Times new roman', 18, bold=True)

def draw():
    global matriz_cubo
    global pagina

    s.background(0)

    img = pygame.surfarray.make_surface(matriz_cubo[pagina])

    s.rect_mode('CENTER')
    s.image(img, width // 2, height // 2)

    s.stroke((255,255,255))
    s.fill((255,255,255))

    s.rect_mode('TOP_LEFT')
    s.text(f"Página: {pagina}/255", 0, 0)

    pagina += 1
    pagina = pagina % 256
    
s.start(setup, draw, "Cubo RGB")