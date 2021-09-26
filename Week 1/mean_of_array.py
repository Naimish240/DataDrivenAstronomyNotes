# Write your calc_stats function here.
import numpy as np

def calc_stats(fh):
  data = np.loadtxt(fh, delimiter=',')
  mean = np.mean(data)
  median = np.median(data)
  return np.round_(mean, 1), np.round_(median, 1)

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your `calc_stats` function with examples:
  mean = calc_stats('data.csv')
  print(mean)