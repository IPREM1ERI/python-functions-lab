def sum_to(n):
  total = 0
  for n in range(1, n + 1):
    total += n
  return total

print(sum_to(6))

def largest(nums):
  nums.sort()
  return nums[-1]

print(largest([10,4,2,231,91,54]))

# def occurrences(str1, str2):\


def product(*args):
  total = 1
  for arg in args:
    total *= arg
  return total

print(product(2,5,5))


