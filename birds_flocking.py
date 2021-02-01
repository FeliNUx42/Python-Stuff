import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import random
import cmath
import math
import copy
import optparse

pygame.init()
width = height = 600

def get_neighbour(birds, i):
    me = birds[i]
    return [b[2] for n, b in enumerate(birds) if ((b[0]-me[0])**2 + (b[1]-me[1])**2)**0.5 <= view and n != i]

def get_mean(degs):
    return math.degrees(cmath.phase(sum(cmath.rect(1, math.radians(d)) for d in degs)/len(degs)))

def collide(d1, d2):
    diff = (d1 - d2)
    if diff > 180: diff = 360 - diff
    elif diff < -180: diff += 360

    return diff

def update(b):
    x = b[0] - math.sin(math.radians(b[2])) * speed
    y = b[1] - math.cos(math.radians(b[2])) * speed

    return [x, y, b[2]]

def draw(b, color, screen):
    x1 = math.sin(math.radians(b[2])) * top
    y1 = math.cos(math.radians(b[2])) * top
    x2 = math.sin(math.radians(b[2]+150)) * side
    y2 = math.cos(math.radians(b[2]+150)) * side
    x3 = math.sin(math.radians(b[2]-150)) * side
    y3 = math.cos(math.radians(b[2]-150)) * side

    pygame.draw.polygon(screen, color, ((b[0]-x1, b[1]-y1), (b[0]-x2, b[1]-y2), (b[0]-x3, b[1]-y3)))
    if options.circle: pygame.draw.circle(screen, (0, 0, 0), b[:2], view, 1)


parser = optparse.OptionParser("%prog " + "-t <total of birds> -s <speed> -v <view width> -g <gap at borders> -b -c", version="%prog 1.0")
parser.add_option("-t", dest="total", type="int", default=100, help="Set number of birds (recommended: 100)")
parser.add_option("-s", dest="speed", type="int", default=4, help="Set speed (recommended: 4)")
parser.add_option("-v", dest="view", type="int", default=150, help="Set how far birds can see (recommended: 150)")
parser.add_option("-g", dest="gap", type="int", default=75, help="Set how big the borders are (recommended: 75)")
parser.add_option("-b", "--border", dest="border", default=False, action="store_true", help="Show borders")
parser.add_option("-c", "--circle", dest="circle", default=False, action="store_true", help="Show how far birds can see (circle)")

options, args = parser.parse_args()

view = options.view
turn = 8
escape = 10
gap = options.gap
speed = options.speed
top = side = 10

pygame.display.set_caption("Flocking Birds")
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

print("Press SPACE to disable/enable birds coordination.")

#[x, y, direction]
birds = [[random.randint(gap, width-gap), random.randint(gap, height-gap), random.randint(0, 360)] for _ in range(100)]

running = True
watching = True

while running:
    clock.tick(25)
    screen.fill((255, 255, 255))

    if options.border:
        pygame.draw.line(screen, (0,0,0), [0,gap], [width, gap], 2)
        pygame.draw.line(screen, (0,0,0), [gap, 0], [gap, height], 2)
        pygame.draw.line(screen, (0,0,0), [width-gap, 0], [width-gap, height], 2)
        pygame.draw.line(screen, (0,0,0), [0,height-gap], [width, height-gap], 2)

    if watching:
        birds_copy = copy.deepcopy(birds)
        for n, me in enumerate(birds):
            neighbour = get_neighbour(birds_copy, n)
            if not len(neighbour): continue
            if x := collide(me[2], get_mean(neighbour)) > 5:
                me[2] += turn
            elif x < -5:
                me[2] -= turn
            me[2] %= 360

    for n, b in enumerate(birds):
        if b[0] + gap > width and 90 <= b[2] < 270: b[2] -= escape               # right
        elif b[0] + gap > width and 0 <= (b[2] + 90) % 360 < 180: b[2] += escape # right
        elif b[0] - gap < 0 and 90 <= b[2] < 270: b[2] += escape                 # left
        elif b[0] - gap < 0 and 0 <= (b[2] + 90) % 360 < 180: b[2] -= escape     # left
        elif b[1] + gap > height and 180 < b[2] <= 360: b[2] += escape           # bottom
        elif b[1] + gap > height and 0 < b[2] <= 180: b[2] -= escape             # bottom
        elif b[1] - gap < 0 and 0 <= b[2] < 180: b[2] += escape                  # top
        elif b[1] - gap < 0 and 180 <= b[2] < 360: b[2] -= escape                # top

        b[2] %= 360

    for n, b in enumerate(birds):
        birds[n] = update(b)
        draw(birds[n], (0, 0, 255), screen)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            watching = not watching
            print("Birds watching for other birds:", "ON" if watching else "OFF")
