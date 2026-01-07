import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Survival Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player properties
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
player_x = WIDTH // 2 - PLAYER_WIDTH // 2
player_y = HEIGHT - PLAYER_HEIGHT - 20
player_speed = 5

# Obstacle properties
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 50
obstacle_speed = 3
obstacles = []

# Clock for controlling the frame rate
clock = pygame.time.Clock()

def draw_player():
    pygame.draw.rect(screen, WHITE, (player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT))

def draw_obstacles():
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, obstacle)

def move_player(keys):
    global player_x

    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - PLAYER_WIDTH:
        player_x += player_speed

def generate_obstacle():
    obstacle_x = random.randint(0, WIDTH - OBSTACLE_WIDTH)
    obstacle_y = -OBSTACLE_HEIGHT
    obstacles.append(pygame.Rect(obstacle_x, obstacle_y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

def move_obstacles():
    global obstacles

    for obstacle in obstacles:
        obstacle.y += obstacle_speed
        if obstacle.y > HEIGHT:
            obstacles.remove(obstacle)

def check_collision():
    player_rect = pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)
    for obstacle in obstacles:
        if player_rect.colliderect(obstacle):
            return True
    return False

def game_loop():
    global player_x

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        move_player(keys)

        screen.fill(BLACK)

        # Generate obstacles
        if random.randint(1, 100) < 5:
            generate_obstacle()

        # Move obstacles
        move_obstacles()

        # Check collision
        if check_collision():
            print("Game Over!")
            pygame.quit()
            sys.exit()

        # Draw player and obstacles
        draw_player()
        draw_obstacles()

        pygame.display.flip()
        clock.tick(60)

# Main function
def main():
    game_loop()

if __name__ == "__main__":
    main()
