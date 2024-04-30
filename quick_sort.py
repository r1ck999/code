def quickSort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot = arr[0]

        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x >= pivot]

        sorted_arr = quickSort(less_than_pivot) + [pivot] + quickSort(greater_than_pivot)
        return sorted_arr

def input_array():
    
    size = int(input("Enter size of the array: "))
    array = []
    for i in range(size):
        element = int(input(f"Enter {i}th element: "))
        array.append(element)
    return array


array = input_array()

print("original array: ")
print(array)
print("sorted array: ")
print(quickSort(array))

