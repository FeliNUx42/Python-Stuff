import random
import pygame

pygame.init()
width = height = 900

class Game:
  def __init__(self):
    self.size = 1
    self.set_up = False
    self.last = None
    self.corners = []

  def clicked(self, pos, screen):
    self.corners.append(pos)

    pygame.draw.circle(screen, (255, 255, 255), pos, self.size)

    if len(self.corners) == 3:
      self.set_up = True
      self.last = random.choice(self.corners)

  def update(self, screen):
    c = random.choice(self.corners)
    x = int((c[0] + self.last[0]) / 2)
    y = int((c[1] + self.last[1]) / 2)

    self.last = (x, y)

    pygame.draw.circle(screen, (255, 255, 255), self.last, self.size)


def main():
  pygame.display.set_caption("Math")
  screen = pygame.display.set_mode((width, height))

  game = Game()

  screen.fill((0, 0, 0))

  while True:
    if game.set_up:
      game.update(screen)

    pygame.display.update()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        return
      if event.type == pygame.MOUSEBUTTONUP:
        game.clicked(event.pos, screen)
      if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
        screen.fill((0,0,0))
        game = Game()


if __name__ == '__main__':
  main()
