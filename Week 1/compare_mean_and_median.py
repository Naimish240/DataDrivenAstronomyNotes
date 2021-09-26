# Write your list_stats function here.
def list_stats(arr):
  arr.sort()
  mid = len(arr)//2
  mean = sum(arr) / len(arr)
  
  if len(arr) % 2: # odd number
    return arr[mid], mean
  
  return (arr[mid-1]+arr[mid])/2, mean



# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with the first example in the question.
  m = list_stats([1.3, 2.4, 20.6, 0.95, 3.1, 2.7])
  print(m)

  # Run your function with the second example in the question
  m = list_stats([1.5])
  print(m)