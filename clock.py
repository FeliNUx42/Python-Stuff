import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import math
import datetime

pygame.init()
width = height = 300

def draw_clock(dt, screen):
    for i in range(0, 360, int(360/12)):
        sx = math.sin(math.radians(i)) * (radius - 10)
        sy = math.cos(math.radians(i)) * (radius - 10)
        ex = math.sin(math.radians(i)) * radius
        ey = math.cos(math.radians(i)) * radius

        pygame.draw.line(screen, (255,255,255), (sx+width, sy+height), (ex+width, ey+height), 5)

    pygame.draw.circle(screen, (0,255,0), (width, height), radius+5, 8)

    s_angle = 360 / 60 * dt.second - 90
    sx = math.cos(math.radians(s_angle)) * sec[0]
    sy = math.sin(math.radians(s_angle)) * sec[0]

    m_angle = 360 / 60 * dt.minute - 90
    mx = math.cos(math.radians(m_angle)) * min[0]
    my = math.sin(math.radians(m_angle)) * min[0]

    h_angle = 360 / 12 * (dt.hour%12+dt.minute/60) - 90
    hx = math.cos(math.radians(h_angle)) * hour[0]
    hy = math.sin(math.radians(h_angle)) * hour[0]

    pygame.draw.line(screen, sec[2], (width, height), (sx+width, sy+height), sec[1])
    pygame.draw.line(screen, min[2], (width, height), (mx+width, my+height), min[1])
    pygame.draw.line(screen, hour[2], (width, height), (hx+width, hy+height), hour[1])

    pygame.draw.circle(screen, (0,255,0), (width, height), inner_radius)



radius = 200
inner_radius = 12
hour = [75, 10, (0,0,255), ]
min = [125, 5, (255,255,0)]
sec = [150, 2, (255,0,0)]

pygame.display.set_caption("Clock")
screen = pygame.display.set_mode((width*2, height*2))
clock = pygame.time.Clock()

running = True

while running:
    clock.tick(30)

    screen.fill((0,0,0))

    draw_clock(datetime.datetime.now(), screen)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
