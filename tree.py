def get_line(line):
  running = True
  index = 0
  result = []
  while running:
    type = line[index]
    i = index+1
    for i in range(index+1, len(line)):
      if line[i] != type:
        break
    else:
      running = False
      if line[-2:] == [1, 1]: i += 1
    result.extend([i-index, type])
    index = i
  return result

prev = [1]
print(prev)

for _ in range(10):
  prev = get_line(prev)
  print(prev)
