import pygame

pygame.init()

screen = pygame.display.set_mode((500, 300))

running = True
while running:
    screen.fill((255, 255, 255))  # white background

    pygame.draw.rect(screen, (0, 0, 255), (100, 100, 200, 80))  # rectangle

    font = pygame.font.SysFont(None, 30)
    text = font.render("Hi", True, (0, 0, 0))
    screen.blit(text, (220, 50))  # text

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()