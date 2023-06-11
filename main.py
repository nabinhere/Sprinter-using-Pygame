import pygame

def main():
    pygame.init()

    # logo = pygame.image.load("image.extension")
    # pygame.display.set_icon(logo)
    pygame.display.set_caption("Runner")
    screen = pygame.display.set_mode((560, 400))
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    clock.tick(60)

if __name__ == "__main__":
    main()