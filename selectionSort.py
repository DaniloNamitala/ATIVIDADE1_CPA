def selectionSort(array):
  size = len(array)
  for i in range(size):
    j = i + 1
    for j in range(i + 1, size):
      if (array[i] > array[j]):
        array[i], array[j] = array[j], array[i]
  return array

arr = [1,5,9,7,3,5,-2]
print(f"{arr} -> {selectionSort(arr)}")