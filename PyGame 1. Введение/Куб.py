import sys
import pygame


def draw_cube(screen, w, h):
    nx = 130 - (w / 2)
    ny = 180 - (w / 2)
    k2 = w / 2

    color = pygame.Color(255, 255, 255)
    hsv = color.hsva
    color2 = pygame.Color(255, 255, 255)
    hsv2 = color2.hsva
    color3 = pygame.Color(255, 255, 255)
    hsv3 = color3.hsva

    color.hsva = (h, hsv[1] + 100, hsv[2] - 25, hsv[3])
    color2.hsva = (h, hsv2[1] + 100, hsv2[2], hsv[3])
    color3.hsva = (h, hsv3[1] + 100, hsv3[2] - 50, hsv[3])

    pygame.draw.polygon(screen, color, ((nx, ny), (nx + w, ny),
                                        (nx + w, ny + w), (nx, ny + w)))

    pygame.draw.polygon(screen, color2, ((nx + k2, ny - k2), (nx + k2 + w, ny - k2),
                                         (nx + w, ny), (nx, ny)))

    pygame.draw.polygon(screen, color3,
                        ((nx + w, ny), (nx + k2 + w, ny - k2),
                         (nx + k2 + w, ny + k2), (nx + w, ny + w)))


def main():
    pygame.init()

    try:
        w, h = [int(i) for i in input().split()]
    except ValueError:
        print('Неправильный формат ввода')
        return -1
    if w % 4 != 0 or w > 100:
        print('Неправильный формат ввода')
        return -1

    screen = pygame.display.set_mode((400, 400))
    draw_cube(screen, w, h)
    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    sys.exit(main())