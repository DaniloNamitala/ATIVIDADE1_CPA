def interpolate(array, begin, end):
  middle = (begin + end) // 2
  size = end - begin + 1
  aux = [0 for i in range(size)]
  i = begin
  j = middle + 1
  for k in range(size):
    if (i <= middle and j <= end):
      if (array[i] <= array[j]):
        aux[k] = array[i]
        i += 1
      else:
        aux[k] = array[j]
        j += 1
    else:
      if (i > middle):
        aux[k] = array[j]
        j += 1
      else:
        aux[k] = array[i]
        i += 1
  for k in range(size):
    array[begin + k] = aux[k]


def mergeSort(array, begin, end):
  if (begin < end):
    middle = (begin + end) // 2
    mergeSort(array, begin, middle)
    mergeSort(array, middle+1, end)
    interpolate(array, begin, end)
  return array

arr = [1,5,9,7,3,5,-2]
print(f"{arr} -> {mergeSort(arr, 0, 6)}")
