from edudraw import EduDraw
import numpy as np
import pygame

matriz_cubo = None
pagina = 0
face = 0  # 0 = eixo R, 1 = eixo G, 2 = eixo B

width, height = 500, 500
s = EduDraw(width, height)

def setup():
    global matriz_cubo
    matriz_cubo = np.load("matriz.npy")  # matriz.shape == (256, 256, 256, 3)
    s.change_default_font('Times new roman', 18, bold=True)
    s.set_controls(mouse_motion=mudar_pagina, key_down=mudar_face)

def mudar_pagina(data: dict):
    global pagina
    pos_x = data['pos'][0]
    pagina = int((pos_x / width) * 256)
    pagina = max(0, min(255, pagina))

def mudar_face(data: dict):
    global face
    tecla = data['scancode']
    if tecla == 79:
        face = (face + 1) % 3
    elif tecla == 80:
        face = (face - 1) % 3

def draw():
    global matriz_cubo, pagina, face

    s.background(0)

    if face == 0:
        slice_img = matriz_cubo[pagina, :, :]  # fixo R
    elif face == 1:
        slice_img = matriz_cubo[:, pagina, :]  # fixo G
    elif face == 2:
        slice_img = matriz_cubo[:, :, pagina]  # fixo B

    if face == 0:
        img = pygame.surfarray.make_surface(slice_img.swapaxes(0, 1))
    else:
        img = pygame.surfarray.make_surface(slice_img)

    s.rect_mode('CENTER')
    s.image(img, width // 2, height // 2)

    s.stroke((255,255,255))
    s.fill((255,255,255))

    s.rect_mode('TOP_LEFT')
    nomes_faces = ["R (G×B)", "G (R×B)", "B (R×G)"]
    s.text(f"Face: {nomes_faces[face]} | Página: {pagina}/255", 10, 10)

    s.text(f"Controles: Setas direita e esquerda alteram o eixo", 10, height - 40)
    s.text(f"Posição X do mouse na tela altera a página", 10, height - 24)

s.start(setup, draw, "Cubo RGB - Visualizador")