# Write your crossmatch function here.
import numpy as np
from time import perf_counter

def angular_dist(r1, d1, r2, d2):
  r1, r2, d1, d2 = np.radians([r1, r2, d1, d2])
  a = np.sin(np.abs(d1-d2)/2) ** 2
  b = np.cos(d1) * np.cos(d2) * np.sin(np.abs(r1-r2)/2) ** 2
  d = 2 * np.arcsin(np.sqrt(a+b))
  return np.degrees(d)

def crossmatch(c1, c2, r_max):
  start = perf_counter()
  r_max = np.radians(r_max)
  matched = []
  unmatched = []
  
  c1 = np.radians(c1)
  c2 = np.radians(c2)
  
  for i, (r1, d1) in enumerate(c1):
    min_dist = 99999
    min_c2 = None
    for j, (r2, d2) in enumerate(c2):
      dist = angular_dist(r1, d1, r2, d2)
      if dist < min_dist:
        min_c2 = j
        min_dist = dist
    
    if min_dist > r_max:
      unmatched.append(i)
    else:
      matched.append((i, min_c2, np.degrees(min_dist)))
  
  return matched, unmatched, perf_counter() - start


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # The example in the question
  cat1 = np.array([[180, 30], [45, 10], [300, -45]])
  cat2 = np.array([[180, 32], [55, 10], [302, -44]])
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)

  # A function to create a random catalogue of size n
  def create_cat(n):
    ras = np.random.uniform(0, 360, size=(n, 1))
    decs = np.random.uniform(-90, 90, size=(n, 1))
    return np.hstack((ras, decs))

  # Test your function on random inputs
  np.random.seed(0)
  cat1 = create_cat(10)
  cat2 = create_cat(20)
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)
