import pygame

pygame.init()

WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20
ERASER_SIZE = 40
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
ERASER_COLOR = (200, 200, 200)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Canvas with Eraser")

def draw_grid():
    for y in range(0, HEIGHT, CELL_SIZE):
        for x in range(0, WIDTH, CELL_SIZE):
            pygame.draw.rect(screen, BLUE, (x, y, CELL_SIZE, CELL_SIZE))

def erase(x, y):
    grid_x = (x // CELL_SIZE) * CELL_SIZE
    grid_y = (y // CELL_SIZE) * CELL_SIZE
    pygame.draw.rect(screen, WHITE, (grid_x, grid_y, CELL_SIZE, CELL_SIZE))

def main():
    running = True
    erasing = False
    clock = pygame.time.Clock()

    while running:
        screen.fill(WHITE)
        draw_grid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    erasing = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    erasing = False

        if erasing:
            x, y = pygame.mouse.get_pos()
            erase(x, y)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
