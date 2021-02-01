import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import random
import optparse

pygame.init()
width = height = depth = 300

class Star():
    def __init__(self, mouse, speed):
        self.x = random.randint(-width, width)
        self.y = random.randint(-height, height)
        self.z = random.randint(0, depth)
        self.mouse = mouse
        self.speed = speed
        self.sx = None
        self.sy = None
        self.px = None
        self.py = None

    def update(self):
        if self.mouse: self.z -= pygame.mouse.get_pos()[0] / 30
        else: self.z -= self.speed
        if self.z <= 0:
            self.z = depth
            self.x = random.randint(-width, width)
            self.y = random.randint(-height, height)
            self.sx = self.sy = None

    def draw(self, screen):
        self.px = self.sx
        self.py = self.sy

        self.sx = map(self.x / self.z, 0, 1, 0, width)
        self.sy = map(self.y / self.z, 0, 1, 0, height)
        size = map(self.z, depth, 0, 0, 6)
        weigth = map(self.z, depth, 0, 1, 3) - 0.4

        if self.px == None and self.py == None:
            self.px = self.sx
            self.py = self.sy

        pygame.draw.circle(screen, (255, 255, 255), (self.sx+width, self.sy+height), size)
        pygame.draw.line(screen, (255, 255, 255), (self.px+width, self.py+height), (self.sx+width, self.sy+height), int(weigth))

def map(val, s1, e1, s2, e2):
    return (val - s1) * (e2 - s2) / (e1-s1) + s2


parser = optparse.OptionParser("%prog " + "-s <number of stars> -p <speed>", version="%prog 1.0")
parser.add_option("-s", dest="stars", type="int", default=500, help="Set number of Stars")
parser.add_option("-p", dest="speed", type="int", default=7, help="Set speed of spaceship (recommended: 0 - 50)")
parser.add_option("-m", "--mouse", dest="mouse", default=False, action="store_true", help="Controll speed by mouse")

options, args = parser.parse_args()

pygame.display.set_caption("Star Wars")
screen = pygame.display.set_mode((width*2, height*2))
clock = pygame.time.Clock()

stars = [Star(options.mouse, options.speed) for _ in range(options.stars)]

running = True

while running:
    clock.tick(30)

    screen.fill((0, 0, 0))

    for star in stars:
        star.update()
        star.draw(screen)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
