import pygame

def main():

    # initialize pygame
    pygame.init()

    # logo = pygame.image.load("image.extension")
    # pygame.display.set_icon(logo)
    # set caption
    pygame.display.set_caption("Runner")

    # create an empty window of size 800X400
    screen = pygame.display.set_mode((800, 400))

    # setup font
    test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

    clock = pygame.time.Clock()

    sky_surface = pygame.image.load("graphics/sky.png")
    ground_surface = pygame.image.load("graphics/ground.png")
    text_surface = test_font.render("My game", False, "black")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0, 300))
        screen.blit(text_surface, (300, 50))
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()