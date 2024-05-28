import pygame
import sys
import random

# Screen set up
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Colours
WHITE = (255, 255, 255)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PONG🏓")
clock = pygame.time.Clock()

class Ball:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.velocity_x = 6  # Velocity in the x-direction
        self.velocity_y =  0 # Velocity in the y-direction
        self.radius = 12.5

    def draw(self):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.radius)

    def update(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

    def bounce(self):
        d = [0,-1,1,-2,2]
        direction = random.choice(d)
        self.velocity_x = -6
        self.velocity_y = direction
    
    def bounce2(self):
        d = [0,-1,1,-2,2]
        direction = random.choice(d)
        self.velocity_x = 6
        self.velocity_y = direction


class Paddle:
    def __init__(self, x):
        self.x = x
        self.y = SCREEN_HEIGHT // 2
        self.width = 10
        self.height = 50
        self.velocity_y = 0  # Velocity in the y-direction
        self.paddle = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        self.paddle.y = self.y
        pygame.draw.rect(screen, WHITE, self.paddle)

    def on_screen(self):
        if self.y > SCREEN_HEIGHT:
            self.y -= SCREEN_HEIGHT
        if self.y < -50:
            self.y += SCREEN_HEIGHT
# Create ball and paddle objects
ball = Ball()
paddle = Paddle(SCREEN_WIDTH - 30)
paddle2 = Paddle(20)

def game_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Handle user input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            paddle.y -= 6
        if keys[pygame.K_DOWN]:
            paddle.y += 6
        if keys[pygame.K_w]:
            paddle2.y -= 6
        if keys[pygame.K_s]:
            paddle2.y += 6

        # Check for collisions with paddles
        if ball.x + ball.radius >= paddle.x and \
            ball.x - ball.radius <= paddle.x + paddle.width and \
            ball.y >= paddle.y and \
            ball.y <= paddle.y + paddle.height:
            ball.bounce()
        if ball.x - ball.radius <= paddle2.x and \
            ball.x + ball.radius >= paddle2.x - paddle2.width and \
            ball.y >= paddle2.y and \
            ball.y <= paddle2.y + paddle2.height:
            ball.bounce2()

        #Sets walls
        if ball.y < 0:
            ball.velocity_y = 4
        if ball.y > SCREEN_HEIGHT:
            ball.velocity_y = -4

        # Update ball and paddle positions
        ball.update()
        paddle.on_screen()
        paddle2.on_screen()

        #Ends game
        if ball.x < paddle2.x - 10:
            running = False
        if ball.x > paddle.x + 10:
            running = False

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw the ball and paddle
        ball.draw()
        paddle.draw()
        paddle2.draw()

        # Update the display
        pygame.display.update()

        # Cap the frame rate
        clock.tick(60)
game_loop()

