import pygame

# Initialize pygame
pygame.init()

# Create window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Background Image and Sound")

# Load background image
background = pygame.image.load("background.jpg")

# Load and play sound
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)  # -1 means loop forever

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Show background
    screen.blit(background, (0, 0))

    pygame.display.update()

# Quit pygame
pygame.quit()