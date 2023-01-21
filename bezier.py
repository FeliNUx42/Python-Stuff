import pygame

pygame.init()

size = (1000,1000)
colors = [
  (255,0,0),
  (0,255,0),
  (0,0,255)
]

screen = pygame.display.set_mode(size)
pygame.display.set_caption(__file__)


class Bezier:
  def __init__(self):
    self.iter = 2500
    self.points = []
    self.curve = []
  
  def _interpolate(self, p0, p1, t):
    dx = (p1[0] - p0[0]) * t
    dy = (p1[1] - p0[1]) * t

    return (p0[0] + dx, p0[1] + dy)
  
  def _parse(self, curve, t):
    new_curve = []

    for i in range(1, len(curve)):
      p = self._interpolate(curve[i-1], curve[i], t)
      new_curve.append(p)
    
    if len(new_curve) == 1:
      return new_curve
    
    return self._parse(new_curve, t)
    
  def parse(self):
    if len(self.points) < 2: return

    self.curve = []

    for i in range(0, self.iter + 1):
      t = i / self.iter
      p = self._parse(self.points, t)
      self.curve.append(p[0])

  def draw(self, screen):
    for n, i in enumerate(self.points):
      pygame.draw.circle(screen, colors[n%3], i, 3)
    
    for i in self.curve:
      pygame.draw.rect(screen, (255,255,255), pygame.Rect(i[0], i[1], 1, 1))
  
  def clear(self):
    self.curve = []
    self.points = []


def main():
  b = Bezier()

  while True:
    screen.fill((0,0,0))
    b.draw(screen)

    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        b.points.append(event.pos)
        b.parse()
      if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
        b.clear()
      if event.type == pygame.QUIT:
        pygame.quit()
        return
    
    pygame.display.update()

if __name__ == '__main__':
  main()