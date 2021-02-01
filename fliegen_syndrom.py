import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import math
import copy
import optparse

pygame.init()
width = height = 600

def get_angle(b1, b2):
    dx = b2[0] - b1[0]
    dy = b2[1] - b1[1]
    return (360 - math.degrees(math.atan2(dy, dx)) - 90) % 360

def update(f, angle):
    x = f[0] - math.sin(math.radians(angle)) * speed
    y = f[1] - math.cos(math.radians(angle)) * speed
    return [x, y, angle, f[3]]

def draw(b, color, screen):
    x1 = math.sin(math.radians(b[2])) * top
    y1 = math.cos(math.radians(b[2])) * top
    x2 = math.sin(math.radians(b[2]+150)) * side
    y2 = math.cos(math.radians(b[2]+150)) * side
    x3 = math.sin(math.radians(b[2]-150)) * side
    y3 = math.cos(math.radians(b[2]-150)) * side

    pygame.draw.polygon(screen, color, ((b[0]-x1, b[1]-y1), (b[0]-x2, b[1]-y2), (b[0]-x3, b[1]-y3)))

def draw_path(track, current, color, screen):
    pygame.draw.lines(screen, color, False, track+[current[:2]])

parser = optparse.OptionParser("%prog " + "-f <fps> -s <speed> -p -b", version="%prog 1.0")
parser.add_option("-f", "--fps", dest="fps", type="int", default=30, help="Frames per second (recommended: 25 - 60)")
parser.add_option("-s", "--speed", dest="sp", type="int", default="2", help="Move x pixels per frame")
parser.add_option("-p", "--path", dest="path", default=False, action="store_true", help="Show path of flies")
parser.add_option("-b", "--border", dest="border", default=False, action="store_true", help="Show start point of flies")

options, args = parser.parse_args()

gap = 100
top = side = 15
speed = options.sp

pygame.display.set_caption("Fliegen Syndrom")
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

fly = [[gap, gap, 270, (255,255,0)],
        [width-gap, gap, 180, (255,0,0)],
        [height-gap, width-gap, 90, (0,255,0)],
        [gap, height-gap, 0, (0,0,255)]]
track = [[], [], [], []]

running = True

while running:
    clock.tick(options.fps)

    screen.fill((255, 255, 255))

    if options.border:
        pygame.draw.line(screen, (0,0,0), [0,gap], [width, gap])
        pygame.draw.line(screen, (0,0,0), [gap, 0], [gap, height])
        pygame.draw.line(screen, (0,0,0), [width-gap, 0], [width-gap, height])
        pygame.draw.line(screen, (0,0,0), [0,height-gap], [width, height-gap])

    fly_copy = copy.deepcopy(fly)

    for i in range(len(fly)):
        angle = get_angle(fly_copy[i], fly_copy[i+1] if i < len(fly_copy)-1 else fly_copy[0])
        track[i].append(fly[i][:2])
        fly[i] = update(fly[i], angle)
        draw(fly[i], fly[i][3], screen)
        if options.path: draw_path(track[i], fly[i], fly[i][3],screen)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
