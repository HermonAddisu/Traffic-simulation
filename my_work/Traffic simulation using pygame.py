import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CAR_WIDTH, CAR_HEIGHT = 50, 30
GREEN_DURATION = 3000  # milliseconds
YELLOW_DURATION = 1000  # milliseconds
RED_DURATION = 3000  # milliseconds

# Colors
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Traffic Light Simulation")


# Car class
class Car:
    def __init__(self):
        self.x = 0
        self.y = HEIGHT // 2
        self.color = (0, 0, 255)
        self.speed = 5
        self.stopped = False

    def move(self):
        if not self.stopped:
            self.x += self.speed
            if self.x > WIDTH:
                self.x = -CAR_WIDTH  # Reset car position

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, CAR_WIDTH, CAR_HEIGHT))


# Main function
def main():
    clock = pygame.time.Clock()
    car = Car()

    light_color = GREEN
    light_timer = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update traffic light
        light_timer += clock.get_time()

        if light_color == GREEN and light_timer >= GREEN_DURATION:
            light_color = YELLOW
            light_timer = 0
        elif light_color == YELLOW and light_timer >= YELLOW_DURATION:
            light_color = RED
            light_timer = 0
        elif light_color == RED and light_timer >= RED_DURATION:
            light_color = GREEN
            light_timer = 0

        # Update car behavior
        if light_color == RED:
            car.stopped = True
        elif light_color == YELLOW:
            car.speed = 2  # Slow down
            car.stopped = False
        else:  # GREEN
            car.speed = 5  # Normal speed
            car.stopped = False

        # Move car
        car.move()

        # Draw everything
        screen.fill(BLACK)
        car.draw()

        # Draw traffic light
        pygame.draw.rect(screen, RED if light_color == RED else BLACK, (WIDTH - 100, HEIGHT // 2 - 50, 30, 30))
        pygame.draw.rect(screen, YELLOW if light_color == YELLOW else BLACK, (WIDTH - 100, HEIGHT // 2 - 10, 30, 30))
        pygame.draw.rect(screen, GREEN if light_color == GREEN else BLACK, (WIDTH - 100, HEIGHT // 2 + 30, 30, 30))

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()