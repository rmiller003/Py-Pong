# This is the classic game Pong designed in Python using the Pygame module
# Written by Robert Miller

# constants and variables

import pygame

WHITE = (255,255,255)
BLACK = (0,0,0)

WIDTH = 600
HEIGHT = 600

pygame.init()
game_font = pygame.font.SysFont('Ubuntu', 40)

delay = 30

paddel_speed = 20

paddle_width = 10
paddle_height = 100

p1_x_pos = 10
p1_y_pos = HEIGHT / 2 - paddle_height / 2

p2_x_pos = WIDTH - paddle_width - 10
p2_y_pos = HEIGHT / 2 - paddle_height / 2

p1_score = 0
p2_score = 0

p1_up = False
p1_down = False
p2_up = False
p2_down = False

ball_x_pos = WIDTH / 2
ball_y_pos = HEIGHT / 2
ball_width = 0
ball_x_vel = -10
ball_y_vel = 0




