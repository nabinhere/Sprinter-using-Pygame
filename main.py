import pygame

def main():

    # initialize pygame
    pygame.init()

    # set caption
    pygame.display.set_caption("Runner")

    # create an empty window of size 800X400
    screen = pygame.display.set_mode((800, 400))

    # setup font
    test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

    # set up clock to use for configuring the frame rate
    clock = pygame.time.Clock()

    sky_surface = pygame.image.load("graphics/sky.png")
    ground_surface = pygame.image.load("graphics/ground.png")
    text_surface = test_font.render("My game", False, "black")
    snail_surface = pygame.image.load("graphics/snail/snail1.png")

    snail_x_pos = 600

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # static part/images on the screen
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0, 300))
        screen.blit(text_surface, (300, 50))

        # dynamic part of the screen
        snail_x_pos -= 4

        if snail_x_pos <=0:
            snail_x_pos = 800
        screen.blit(snail_surface, (snail_x_pos, 250))

        pygame.display.update()
        clock.tick(60)  #sets frame rate to 60, i.e, changes the images/surfaces 60 times per second

if __name__ == "__main__":
    main()