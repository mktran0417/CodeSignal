def solution(n):
    counter = iter(Count())
    return [[next(counter) for x in range(n)] for x in range(n)]

class Count:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

def solution_2(n):
    return [[(x + 1) * (y + 1) for x in range(n)] for y in range(n)]
