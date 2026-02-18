import pygame
from hand_tracking import HandTracker

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Temple Run Hand Game")

clock = pygame.time.Clock()

player_x = WIDTH // 2
player_y = HEIGHT - 80
speed = 8

tracker = HandTracker()

running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    move = tracker.get_hand_position()

    if move == "LEFT":
        player_x -= speed
    elif move == "RIGHT":
        player_x += speed

    player_x = max(0, min(WIDTH - 50, player_x))

    screen.fill((20, 20, 20))
    pygame.draw.rect(screen, (0, 255, 0), (player_x, player_y, 50, 50))

    pygame.display.update()

pygame.quit()
