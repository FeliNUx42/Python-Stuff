import re
import sys


class Term:
  def __init__(self, val:str = "", koef:int = 0, exp:int = 0) -> None:
      self.koef = koef
      self.exp = exp

      if val:
        self._set(val)
  
  def __repr__(self) -> str:
    return f"<Term (koef={self.koef}, exp={self.exp})>"
  
  def __add__(self, other):
    if self.exp != other.exp:
      raise TypeError(f"unsupported operand for exponent: {self.exp} and {other.exp}")
      
    koef = self.koef + other.koef
    exp = self.exp

    return Term(koef=koef, exp=exp)
  
  def __sub__(self, other):
    if self.exp != other.exp:
      raise TypeError(f"unsupported operand for exponent: {self.exp} and {other.exp}")
      
    koef = self.koef - other.koef
    exp = self.exp

    return Term(koef=koef, exp=exp)
  
  def __mul__(self, other):
    koef = self.koef * other.koef
    exp = self.exp + other.exp

    return Term(koef=koef, exp=exp)

  def __floordiv__(self, other):
    koef = self.koef // other.koef
    exp = self.exp - other.exp

    return Term(koef=koef, exp=exp)
  
  def _set(self, value:str) -> None:
    pattern = "^(-?\d*)([a-z]?)(\^(-?\d+))?$"
    _koef, _var, _, _exp = list(re.findall(pattern, value)[0])
    
    koef = _koef or "1"
    if not _var: exp = "0"
    elif not _exp: exp = "1"
    else: exp = _exp

    self.koef = int(koef)
    self.exp = int(exp)


def normalize(pol:list) -> list:
  pol.sort(key=lambda x: x.exp, reverse=True)
  last = pol[0].exp
  ind = 1
  while ind < len(pol):
    while (last - pol[ind].exp) != 1:
      t = Term(koef=0, exp=last-1)
      last -= 1
      pol.insert(ind, t)
      ind += 1
    last = pol[ind].exp
    ind += 1
  return pol

def formatting(terms:list) -> str:
  res = []
  for t in terms:
    if t.koef == 0: continue
    t_str = f"{t.koef}x^{t.exp}"
    t_str = t_str.replace("x^0", "").replace("^1", "")
    res.append(t_str)
  
  return " + ".join(res).replace(" + -", " - ")


def main(pol:str) -> None:
  a, b = re.findall("^\((.*)\) : \((.*)\)$", pol)[0]
  a = a.replace(" + ", " ").replace(" - ", " -").split()
  b = b.replace(" + ", " ").replace(" - ", " -").split()

  a = [Term(val=val) for val in a]
  b = [Term(val=val) for val in b]

  a = normalize(a)
  b = normalize(b)

  #print(a)
  #print(b)

  res = []

  for i in range(len(a)):
    div = a[i] // b[0]
    res.append(div)

    for j in range(len(b)):
      a[j+i] -= (b[j] * div)
    
    if i + j == len(a) -1: break
    
  print("Result: ", formatting(res))
  print("Remeinder: ", formatting(a))


if __name__ == '__main__':
  pol = sys.argv[1]
  main(pol)