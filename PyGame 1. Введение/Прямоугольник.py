import pygame
import sys


def main():
    pygame.init()
    screen = pygame.display.set_caption('Прямоугольник')

    try:
        w, l = [int(i) for i in input().split()]
    except ValueError:
        print('Неправильный формат ввода')
        return -1

    size = (w, l)

    screen = pygame.display.set_mode(size)

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, pygame.Color('red'), (0, 0, w, l))
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, w, l), 1)


    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    sys.exit(main())