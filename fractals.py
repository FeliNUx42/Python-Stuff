import pygame
import math

pygame.init()


dimensions = (1000, 1000)
white = (255,255,255)
black = (0,0,0)

screen = pygame.display.set_mode(dimensions)
pygame.display.set_caption(__file__)

def fractal(pos, length, d_length, angle, d_angle, iteration=0, max_iter=14):
  if iteration >= max_iter: return

  x, y = pos
  nx = x - math.sin(angle) * length
  ny = y - math.cos(angle) * length

  n_pos = (nx, ny)

  pygame.draw.line(screen, white, pos, n_pos, 1)

  for i in (1, -1):
    fractal(n_pos, length/d_length, d_length, angle+d_angle*i, d_angle, iteration+1)


angle = 0
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  try:
    angle = float(input(f"{angle} - Angle: ") or angle + 1)
  except ValueError:
    pass

  angle %= 360

  screen.fill(black)

  fractal((500, 800), 180, 1.35, 0, math.radians(angle))

  pygame.display.update()