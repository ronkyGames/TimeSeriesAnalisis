import numpy as np
import pygame
import sys

# initialize pygame
pygame.init()

# set up display
WIDTH, HEIGHT = 800, 400
FPS = 30

# set up colors
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# functions
# function to generate casual movements
def generate_casual_movements(num_ticks):
    movements = np.random.choice([-1, 1], size =num_ticks)
    prices = np.zeros(num_ticks)
    for i in range(1, num_ticks):
        prices[i] = prices[i-1] + movements[i]
    return prices

# function to draw the graph
def draw_graph(prices):
    # set up display
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Stock Price Simulation")

    # set up clock
    clock = pygame.time.Clock()

    # set up variables
    num_ticks = len(prices)
    max_price = max(prices)
    min_price = min(prices)
    price_range = max_price - min_price

    # draw the graph
    screen.fill(WHITE)
    for i in range(1, num_ticks):
        x1 = int((i-1) / num_ticks * WIDTH)
        x2 = int(i / num_ticks * WIDTH)
        y1 = int((max_price - prices[i-1]) / price_range * HEIGHT)
        y2 = int((max_price - prices[i]) / price_range * HEIGHT)
        pygame.draw.line(screen, BLUE, (x1, y1), (x2, y2), 2)

    # update the display
    pygame.display.flip()

    # wait for the user to close the window
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(FPS)

# main program
if __name__ == "__main__":
    num_ticks = 100
    prices = generate_casual_movements(num_ticks)
    draw_graph(prices)
    pygame.quit()
    sys.exit()