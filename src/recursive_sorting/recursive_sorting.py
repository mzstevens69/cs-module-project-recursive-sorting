# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    #pre allocates memory [0,0,0,0,0,0]
    merged_arr = [0] * elements
    #the 2 pointers
    ptrA = 0
    ptrB = 0
    
    #loop over elements in the range
    
    for element in range(elements):
        
        #if A pointer reaches end of list
        if ptrA >= len(arrA):
            merged_arr[element] = arrB[ptrB]
            ptrB +=1
        #if ptrB reaches the end of list
        elif ptrB >= len(arrB):
            merged_arr[element] = arrA[ptrA]
            ptrA += 1
            
        #compare the start of arrA[ptrA] to the start of ArrB[ptrB]
        #the one that is smaller gets added to merged arr
        elif arrA[ptrA] < arrB[ptrB]:
            merged_arr[element] = arrA[ptrA]
            ptrA += 1
            
        else:
            merged_arr[element] = arrB[ptrB]
            ptrB += 1


    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
#RULES FOR RECURSION
#1. Must have a base case.
#2. Must change state toward the base case.
#3. Must call itself, recursively.
def merge_sort(arr):
    #base case If array is empty or length of 1
    if len(arr) <= 1:
        return arr
    
    #divide arr in half 
    
    split = len(arr) //2
    
    go_left = merge_sort(arr[:split])
    
    go_right = merge_sort(arr[split:])


    return merge(go_left, go_right)


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    L = arr[start:mid]
    R = arr[mid:end]
    
    i = 0
    j = 0
    

    
    for l in range(start, end):
        if j >= len(R) or (i < len(L) and L[i] < R[j]):
            arr[l] = L[i]
            i = i + 1
            print("Left side",L, "right side", R)
        else:
            arr[l] = R[j]
            j = j + 1
            print("Left side2",l, "right side2", R[j])
    # return arr


def merge_sort_in_place(arr, l, r):
    if r - l > 1:
        
        mid = int((l + r)/2)
        merge_sort_in_place(arr, l, mid)
        merge_sort_in_place(arr, mid, r)
        merge_in_place(arr, l, mid, r)
    
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt

    # Python3 program to perform TimSort.  
RUN = 32 
    
# This function sorts array from left index to  
# to right index which is of size atmost RUN  
def insertionSort(arr, left, right):  
   
    for i in range(left + 1, right+1):  
       
        temp = arr[i]  
        j = i - 1 
        while j >= left and arr[j] > temp :  
           
            arr[j+1] = arr[j]  
            j -= 1
           
        arr[j+1] = temp  
    
# merge function merges the sorted runs  
def merge2(arr, l, m, r): 
   
    # original array is broken in two parts  
    # left and right array  
    len1, len2 =  m - l + 1, r - m  
    left, right = [], []  
    for i in range(0, len1):  
        left.append(arr[l + i])  
    for i in range(0, len2):  
        right.append(arr[m + 1 + i])  
    
    i, j, k = 0, 0, l 
    # after comparing, we merge those two array  
    # in larger sub array  
    while i < len1 and j < len2:  
       
        if left[i] <= right[j]:  
            arr[k] = left[i]  
            i += 1 
           
        else: 
            arr[k] = right[j]  
            j += 1 
           
        k += 1
       
    # copy remaining elements of left, if any  
    while i < len1:  
       
        arr[k] = left[i]  
        k += 1 
        i += 1
    
    # copy remaining element of right, if any  
    while j < len2:  
        arr[k] = right[j]  
        k += 1
        j += 1
      
# iterative Timsort function to sort the  
# array[0...n-1] (similar to merge sort)  
def timSort(arr, n):  
   
    # Sort individual subarrays of size RUN  
    for i in range(0, n, RUN):  
        insertionSort(arr, i, min((i+31), (n-1)))  
    
    # start merging from size RUN (or 32). It will merge  
    # to form size 64, then 128, 256 and so on ....  
    size = RUN 
    while size < n:  
       
        # pick starting point of left sub array. We  
        # are going to merge arr[left..left+size-1]  
        # and arr[left+size, left+2*size-1]  
        # After every merge, we increase left by 2*size  
        for left in range(0, n, 2*size):  
           
            # find ending point of left sub array  
            # mid+1 is starting point of right sub array  
            mid = left + size - 1 
            right = min((left + 2*size - 1), (n-1))  
    
            # merge sub array arr[left.....mid] &  
            # arr[mid+1....right]  
            merge2(arr, left, mid, right)  
          
        size = 2*size


# Divide and Conquer

#when writing a recursive algo

# 1. what's our base case
# 2. if we aren't in the base case how are we moving towards the base case
# def partition(data):
#     pivot = data[0]
#     left = []
#     right = []
    
#     for x in data[1:]:
#         if x <= pivot:
#             left.append(x)
#         else:
#             right.append(x)
#     return left, pivot, right

# def quicksort(data):
    
    #base case
    # if len(data) == 0:
    #     return data
    # partition hadles picking the pivot element
    #partitioning the data around  the pivot
    # left is the left sublist and right right sublist
    # left, pivot, right = partition(data)
    
    # return quicksort(left) + [pivot] + quicksort(right)

#in place quick sort -- better on memory
def ip_partition(data, start, end):
    pivot = data[start]
    
    i = start + 1
    j = start + 1
    
    #partitioning step moves elements around the pivot
    while j <= end:
        if data[j] <= pivot:
            data[j], data[i -1 ] = data[i - 1], data[start]
            i += 1
        j += 1
    data[start], data[i - 1] = data[i - 1], data[start]
    #return the index of the pivot
    return i - 1


def in_place_qs(data, start=0, end=None):
    if end is None:
        end = len(data) -1
    #base case    
    if start >= end:
        return data
    
    #returns index of the pivot
    #partitions the data around the pivot
    
    index = ip_partition(data, start, end)
    # qs call everything to the left
    in_place_qs(data, start, index - 1)
    #qs call for everything to the right of the pivot
    in_place_qs(data, index + 1, end)