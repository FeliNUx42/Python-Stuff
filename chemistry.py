import re
from sympy import Matrix, lcm


def to_dict(string):
  res = re.findall("([A-Z][a-z]?)([0-9]?)", string)
  dic = {}
  for i in res:
    dic[i[0]] = int(i[1] or "1")
  return dic

def get_elements(lst):
  elem = []
  for i in lst:
    for v in i.keys():
      if not v in elem:
        elem.append(v)
  return elem

def to_list(dct, elem, multiplier):
  lst = []
  for e in elem:
    lst.append(dct.get(e, 0) * multiplier)
  return lst

def main(inp):
  prod, res = inp.strip().split(" -> ")

  prod = [to_dict(i) for i in prod.split(" + ")]
  res = [to_dict(i) for i in res.split(" + ")]

  elem = get_elements(prod)

  prod = [to_list(i, elem, 1) for i in prod]
  res = [to_list(i, elem, -1) for i in res]

  matrix = prod + res

  elementMatrix = Matrix(matrix)
  elementMatrix = elementMatrix.transpose()
  solution=elementMatrix.nullspace()[0]

  multiple = lcm([val.q for val in solution])
  solution = (multiple*solution).tolist()

  return [i[0] for i in solution]

if __name__ == '__main__':
  inp = "HNO3 + CH2O -> N2 + CO2 + H2O"
  res = main(inp)
  print(res)

