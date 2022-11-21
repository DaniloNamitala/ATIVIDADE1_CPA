def bubbleSort(array):
  last = len(array) - 1
  for end in range(last, 0, -1):
    for i in range(0, end):
      if (array[i] > array[i+1]):
       array[i], array[i+1] = array[i+1], array[i]
  return array

arr = [1,5,9,7,3,5,-2]
print(f"{arr} -> {bubbleSort(arr)}")