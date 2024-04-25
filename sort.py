def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        while j >=0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            arr[j+1]=key
        
#example usage
arr = [8,25,65,9,7,21,5,9,1,14,18]
insertion_sort(arr)
print("sorted array is:",arr)



