import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Kematian - Mario di Kejar Setan")

SKY_BLUE = (135, 206, 235)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (139, 69, 19)

mario_width = 40
mario_height = 60
mario_x = 50
mario_y = HEIGHT - mario_height - 50
mario_speed = 5
mario_jump = False
mario_jump_count = 10

platform_height = 50
platform_y = HEIGHT - platform_height

obstacle_width = 30
obstacle_height = 50
obstacles = []

score = 0
font = pygame.font.Font(None, 36)

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not mario_jump:
                mario_jump = True

    # Move Mario
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and mario_x > 0:
        mario_x -= mario_speed
    if keys[pygame.K_RIGHT] and mario_x < WIDTH - mario_width:
        mario_x += mario_speed

    # Jump mechanics
    if mario_jump:
        if mario_jump_count >= -10:
            neg = 1
            if mario_jump_count < 0:
                neg = -1
            mario_y -= (mario_jump_count ** 2) * 0.5 * neg
            mario_jump_count -= 1
        else:
            mario_jump = False
            mario_jump_count = 10

    # Generate obstacles
    if len(obstacles) == 0 or obstacles[-1][0] < WIDTH - 300:
        x = WIDTH
        y = HEIGHT - platform_height - obstacle_height
        obstacles.append([x, y, obstacle_width, obstacle_height])

    # Move obstacles
    for obstacle in obstacles:
        obstacle[0] -= 5

    # Remove off-screen obstacles
    obstacles = [obs for obs in obstacles if obs[0] > -obstacle_width]

    # Collision detection
    for obstacle in obstacles:
        if (mario_x < obstacle[0] + obstacle[2] and
            mario_x + mario_width > obstacle[0] and
            mario_y < obstacle[1] + obstacle[3] and
            mario_y + mario_height > obstacle[1]):
            running = False

    # Increase score
    score += 1

    # Draw everything
    screen.fill(SKY_BLUE)
    pygame.draw.rect(screen, GREEN, (0, platform_y, WIDTH, platform_height))
    pygame.draw.rect(screen, RED, (mario_x, mario_y, mario_width, mario_height))
    for obstacle in obstacles:
        pygame.draw.rect(screen, BROWN, obstacle)

    # Draw score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    notes = font.render("Lompat ? Tekan Spasi !", True, (0, 0, 0))
    notes2 = font.render("copyright: sofinranger", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    screen.blit(notes,(10,50))
    screen.blit(notes2,(450,10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()