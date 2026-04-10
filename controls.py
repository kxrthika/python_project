import pygame
pygame.init()

screen = pygame.display.set_mode((500, 300))

x, y = 50, 50   # moving rectangle

run = True
while run:
    screen.fill((255, 255, 255))

    # two rectangles
    pygame.draw.rect(screen, (0, 0, 255), (x, y, 80, 60))   # moving
    pygame.draw.rect(screen, (255, 0, 0), (300, 120, 80, 60))  # fixed

    # controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: x -= 5
    if keys[pygame.K_RIGHT]: x += 5
    if keys[pygame.K_UP]: y -= 5
    if keys[pygame.K_DOWN]: y += 5

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()