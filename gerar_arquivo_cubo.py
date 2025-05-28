import numpy as np

# def calcular_cantos(pagina: int) -> list[tuple]:
#     canto_se: tuple = (pagina, 0, 255)
#     canto_sd: tuple = (pagina, 255, 255)
#     canto_id: tuple = (pagina, 255, 0)
#     canto_ie: tuple = (pagina, 0, 0)

#     return [canto_se, canto_sd, canto_id, canto_ie]

if __name__ == "__main__":
    
    # 'Pagina': valor R muda com páginas
    # X: Valor G
    # Y: Valor B

    g, b = np.mgrid[0:256, 0:256]  # Ambos com shape (256, 256)

    cubo_rgb = []

    for r in range(256):
        plano = np.stack((np.full_like(g, r), g, b), axis=-1)
        cubo_rgb.append(plano)

    cubo_rgb = np.array(cubo_rgb, dtype=np.uint8)

    np.save('matriz.npy', cubo_rgb)
