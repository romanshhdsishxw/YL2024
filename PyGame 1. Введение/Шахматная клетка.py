import sys
import pygame


def main():
    pygame.init()

    try:
        a, n = [int(i) for i in input().split()]
    except ValueError:
        print('Неправильный формат ввода')
        return -1
    if a % n != 0:
        print('Неправильный формат ввода')
        return -1

    screen = pygame.display.set_mode((a, a))
    screen.fill((255, 255, 255))

    kvardrat(screen, a, n)

    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()
    pygame.quit()


def kvardrat(screen, a, n):
    storona = a // n
    if n % 2 == 0:
        for i in range(n):
            for j in range(n):
                if (i + j) % 2 != 0:
                    color = (0, 0, 0)
                    pygame.draw.rect(screen, color, (j * storona, i * storona, storona, storona))
                    pygame.display.flip()
    else:
        for i in range(n):
            for j in range(n):
                if (i + j) % 2 == 0:
                    color = (0, 0, 0)
                    pygame.draw.rect(screen, color, (j * storona, i * storona, storona, storona))
                    pygame.display.flip()


if __name__ == '__main__':
    sys.exit(main())
