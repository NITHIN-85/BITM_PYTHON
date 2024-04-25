#bubble sort
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        #last i elements are already in place
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                #swap if the elements found is greater than the next element
                arr[j],arr[j+1] = arr[j+1],arr[j]
                
#example usage:
arr = [64,34,25,12,22,11,90,86,100]
bubble_sort(arr)
print("sorted array is:",arr)
            