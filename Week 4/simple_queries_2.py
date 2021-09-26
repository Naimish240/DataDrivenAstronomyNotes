import numpy as np

# Write your query function here
def query(file):
  data = np.loadtxt(file, delimiter=',')
  res = []
  for idx, temp, rad in data:
    if rad > 1.0:
      res.append([idx, rad])
  res.sort(key = lambda x: x[1])
  return np.array(res)

# You can use this to test your code
# Everything inside this if-statement will be ignored by the automarker
if __name__ == '__main__':
  # Compare your function output to the SQL query
  result = query('stars.csv')
  print(result)