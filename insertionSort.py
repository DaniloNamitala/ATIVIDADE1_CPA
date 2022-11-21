def insertionSort(array):
  for i in range(1, len(array)):
    j = i
    key = array[j]
    while(j > 0 and array[j-1] > key):
      array[j] = array[j-1]
      j -= 1
    array[j] = key
  return array

arr = [1,5,9,7,3,5,-2]
print(f"{arr} -> {insertionSort(arr)}")