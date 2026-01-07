import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Ball properties
BALL_RADIUS = 10
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = 5
ball_dy = 5

# Paddle properties
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20
paddle_x = WIDTH // 2 - PADDLE_WIDTH // 2
paddle_y = HEIGHT - PADDLE_HEIGHT - 20
paddle_speed = 10

# Brick properties
BRICK_WIDTH = 80
BRICK_HEIGHT = 30
NUM_ROWS = 2
NUM_BRICKS_PER_ROW = 9
bricks = []

# Clock for controlling the frame rate
clock = pygame.time.Clock()

def draw_ball():
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), BALL_RADIUS)

def draw_paddle():
    pygame.draw.rect(screen, WHITE, (paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))

def draw_brick(color, x, y):
    pygame.draw.rect(screen, color, (x, y, BRICK_WIDTH, BRICK_HEIGHT))

def move_ball():
    global ball_x, ball_y, ball_dx, ball_dy

    ball_x += ball_dx
    ball_y += ball_dy

    # Ball collision with walls
    if ball_x <= 0 or ball_x >= WIDTH:
        ball_dx *= -1
    if ball_y <= 0:
        ball_dy *= -1

    # Ball collision with paddle
    if ball_y >= paddle_y - BALL_RADIUS and paddle_x <= ball_x <= paddle_x + PADDLE_WIDTH:
        ball_dy *= -1

def move_paddle(keys):
    global paddle_x

    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - PADDLE_WIDTH:
        paddle_x += paddle_speed

def create_bricks():
    global bricks

    bricks.clear()
    for row in range(NUM_ROWS):
        for col in range(NUM_BRICKS_PER_ROW):
            brick_color = random.choice([RED, GREEN, BLUE, YELLOW])
            brick_x = col * (BRICK_WIDTH + 5) + 30
            brick_y = row * (BRICK_HEIGHT + 5) + 50
            bricks.append(pygame.Rect(brick_x, brick_y, BRICK_WIDTH, BRICK_HEIGHT))

def check_collision():
    global ball_dx, ball_dy

    for brick in bricks:
        if brick.colliderect(pygame.Rect(ball_x - BALL_RADIUS, ball_y - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)):
            bricks.remove(brick)
            ball_dy *= -1

def game_loop():
    global ball_x, ball_y, paddle_x

    create_bricks()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        move_paddle(keys)
        move_ball()
        check_collision()

        # Check if the ball falls below the paddle
        if ball_y >= HEIGHT:
            print("Game Over!")
            pygame.quit()
            sys.exit()

        screen.fill(BLACK)
        draw_ball()
        draw_paddle()
        for brick in bricks:
            draw_brick(WHITE, brick.x, brick.y)
        pygame.display.flip()
        clock.tick(60)

# Main function
def main():
    game_loop()

if __name__ == "__main__":
    main()
