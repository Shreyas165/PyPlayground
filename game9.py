import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Endless Temple Run")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Player properties
player_width = 50
player_height = 50
player_y = HEIGHT - player_height - 50
player_speed = 5

# Coin properties
coin_size = 20
coins = []

# Background properties
background_x = 0
background_speed = 3
background_image = pygame.image.load("background.jpg").convert()
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Points
points = 0
font = pygame.font.SysFont(None, 30)

# Clock for controlling the frame rate
clock = pygame.time.Clock()

def draw_player(player_x):
    pygame.draw.rect(screen, YELLOW, (player_x, player_y, player_width, player_height))

def draw_coin(x, y):
    pygame.draw.circle(screen, WHITE, (x, y), coin_size)

def move_background():
    global background_x

    background_x -= background_speed
    if background_x <= -WIDTH:
        background_x = 0

def generate_coin():
    global coins

    coin_x = random.randint(WIDTH, WIDTH * 2)
    coin_y = random.randint(50, HEIGHT - coin_size - 50)
    coins.append((coin_x, coin_y))

def move_coins():
    global coins

    for i in range(len(coins)):
        coins[i] = (coins[i][0] - player_speed, coins[i][1])

def collect_coins(player_x):
    global coins, points

    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    for coin in coins:
        if player_rect.colliderect(pygame.Rect(coin[0] - coin_size, coin[1] - coin_size, coin_size * 2, coin_size * 2)):
            coins.remove(coin)
            points += 1

def display_points():
    text = font.render(f"Points: {points}", True, RED)
    screen.blit(text, (10, 10))

def game_loop():
    global player_speed, player_y

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        move_background()

        keys = pygame.key.get_pressed()
        player_speed = 5  # Set player speed
        if keys[pygame.K_SPACE]:
            player_speed += 2  # Increase player speed if space key is pressed

        move_coins()

        screen.blit(background_image, (background_x, 0))
        screen.blit(background_image, (background_x + WIDTH, 0))

        player_x = 50  # Set player x-position
        draw_player(player_x)

        generate_coin()
        for coin in coins:
            draw_coin(coin[0], coin[1])

        collect_coins(player_x)

        display_points()

        pygame.display.flip()
        clock.tick(60)

# Main function
def main():
    game_loop()

if __name__ == "__main__":
    main()
