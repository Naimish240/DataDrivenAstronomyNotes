# Write your mean_datasets function here
import numpy as np

def mean_datasets(arr):
  data = np.loadtxt(arr[0], delimiter=',')
  for dataset in arr[1:]:
    data += np.loadtxt(dataset, delimiter=',')
  return np.round_(data / len(arr), 1)


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with the first example from the question:
  print(mean_datasets(['data1.csv', 'data2.csv', 'data3.csv']))

  # Run your function with the second example from the question:
  print(mean_datasets(['data4.csv', 'data5.csv', 'data6.csv']))
