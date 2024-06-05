

SLEIGHT_VALUES = (20,24,30)

# This function calculates the number of solutions for a right triangle given
# the perimeter. This may take some additional time.
def solve(p):
    """ Solve the equation for p = a + b + c """
    cnt = 0
    # for each possible value of a, b and c in left and right triangle
    for a in SLEIGHT_VALUES:
      # check if the perimeter is smaller than or equal to the value of a + b + c
      if p <= a + b:
        # check if the perimeter is larger than or equal to b + c
        if p >= b + c:
          # check if the perimeter is smaller than or equal to a + c
          if p <= a + c:
            # if true, increase the cnt by one
            cnt += 1
    return cnt

# We iterate between the given values of p and calculate the number of
# solutions.
cnt_max = 1
p = 50
print(f'p = {p}')

while p < 1000:
  p += 10
  cnt = solve(p)
  if cnt == 3:
    # if there are exactly three possible solutions, we have the correct answer
    print(f'p = {p}, cnt = {cnt}, p % 1000 = {p%1000}')
    break
  elif cnt > cnt_max:
    # otherwise, we have a new cnt_max
    cnt_max = cnt
    print(f'p = {p}, cnt = {cnt}, p % 1000 = {p%1000}')

"""
ANSWER: 20

"""