class Compiler:
  def __init__(self, *, length=100, ascii=True, overflow=256):
      self.chars = "<>+-[].,"
      self.length = length
      self.array = [0 for _ in range(length)]
      self.index = 0
      self.ascii = ascii
      self.overflow = overflow
  
  def compile(self, script):
    ind = 0
    while True:
      if ind == len(script): break
      i = script[ind]

      if not i in self.chars: continue

      if i == "+": self._add(1)
      if i == "-": self._add(-1)
      if i == ">": self._move(1)
      if i == "<": self._move(-1)

      if i == ".": self._print()
      if i == ",": self._read()

      if i == "[":
        if not self.array[self.index]:
          ind = self._endLoop(ind, script)
      if i == "]":
        ind = self._startLoop(ind, script)
        continue

      ind += 1
  
  def _add(self, val):
    self.array[self.index] = (self.array[self.index] + val) % self.overflow

  def _move(self, val):
    self.index = (self.index + val) % self.length
  
  def _print(self):
    if self.ascii:
      print(chr(self.array[self.index]), end="")
    else:
      print(self.array[self.index], end="")
  
  def _read(self):
    char = input()[0]

    if self.ascii: char = ord(char)
    else: char = int(char)
    self.array[self.index] = char % self.overflow
  
  def _endLoop(self, ind, script):
    brackets = 0
    for num, i in enumerate(script[ind+1:]):
      if i == "[": brackets += 1
      if i == "]": brackets -= 1

      if brackets < 0:
        break

    return num + ind + 1
  
  def _startLoop(self, ind, script):
    brackets = 0
    for num, i in enumerate(script[ind-1::-1]):
      if i == "[": brackets -= 1
      if i == "]": brackets += 1

      if brackets < 0:
        break

    return ind - num - 1

if __name__ == '__main__':
  c = Compiler(length=20, ascii=False, overflow=1024)
  while True:
    #script = "+++[>+++[>+++<-]<-]>>."
    script = input("\nCode: ")
    c.compile(script)

