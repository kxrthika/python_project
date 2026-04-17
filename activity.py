import pygame
import random

pygame.init()

# Screen
screen = pygame.display.set_mode((600, 400))

# Player
player = pygame.Rect(300, 200, 40, 40)
speed = 1   # slower movement

# Enemies (7 random)
enemies = []
for i in range(7):
    x = random.randint(0, 560)
    y = random.randint(0, 360)
    enemies.append(pygame.Rect(x, y, 40, 40))

# Score
score = 0

# Clock to control speed
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(150)  # lower = slower game

    screen.fill((255, 255, 255))  # white background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed

    # Check collisions
    for enemy in enemies:
        if player.colliderect(enemy):
            score += 1
            enemy.x = random.randint(0, 560)
            enemy.y = random.randint(0, 360)

    # Draw player
    pygame.draw.rect(screen, (0, 0, 255), player)

    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, (255, 0, 0), enemy)

    pygame.display.update()

pygame.quit()