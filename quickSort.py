def partition(array, begin, end):
  pivot = array[end]
  i = begin - 1
  j = end + 1
  while(True):
    j -= 1
    while(array[j] > pivot):
      j -= 1
    i += 1
    while(array[i] < pivot):
      i += 1
    if (i >= j):
      return j
    array[i], array[j] = array[j], array[i]

def quickSort(array, begin, pivot):
  if (begin < pivot):
    newPivot = partition(array, begin, pivot)
    quickSort(array, begin, newPivot-1)
    quickSort(array, newPivot+1, pivot)
  return array

arr = [1,5,9,7,3,5,-2]
print(f"{arr} -> {quickSort(arr, 0, 6)}")