import random

def bubble(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                _swap(arr, j, j+1)
           
def selection(arr):
    for i in range(len(arr)):
        curMaxVal = arr[0]
        curMaxInd = 0
        for j in range(len(arr) - i):
            if arr[j] > curMaxVal:
                curMaxVal = arr[j]
                curMaxInd = j

        _swap(arr, curMaxInd, len(arr) - i - 1)

def insertion(arr):
    for i in range(1, len(arr)):
        curVal = arr[i]
        curInd = i
        prevVal = arr[i-1]
        
        while curVal < prevVal:
            _swap(arr, curInd, curInd - 1)
            
            curInd -= 1
            if curInd >= 1:
                prevVal = arr[curInd-1]   
            else:
                break

def merge(arr):
    if len(arr) <= 1:
        return
    
    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    merge(left)
    merge(right)
    
    left_cur = 0
    right_cur = 0
    arrInd = 0
    while left_cur < len(left) and right_cur < len(right):
        left_val = left[left_cur]
        right_val = right[right_cur]
   
        if left_val < right_val:
            left_cur += 1

            arr[arrInd] = left_val
        else:
            right_cur += 1
            
            arr[arrInd] = right_val

        arrInd += 1

    while left_cur < len(left):
        arr[arrInd] = left[left_cur]
        arrInd += 1
        left_cur += 1

    while right_cur < len(right):
        arr[arrInd] = right[right_cur]
        arrInd += 1
        right_cur += 1

def quick(arr):
    _quick_help(arr, 0, len(arr))    

def _quick_help(arr, start, end):
    '''
        End is not inclusive
    '''
    if start == end or start == end - 1:
        return

    leftPivotInd = start
    rightPivotInd = start
    pivotVal = arr[start]

    for i in range(start + 1, end):
        curVal = arr[i]
        if curVal <= pivotVal:
            _swap_down(arr, leftPivotInd, i)

            rightPivotInd += 1
            if curVal != pivotVal:
                leftPivotInd += 1

    _quick_help(arr, start, leftPivotInd)
    _quick_help(arr, rightPivotInd + 1, end)
 
def _swap_down(arr, i, j):
    '''
        Swaps the value at j down until it swaps with the value at i
    '''

    while j > i:
        _swap(arr, j, j-1)
        j -= 1

def _swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]: return False

    return True

def main():
    for i in range(10):
        arr = []
        for j in range(10):
            arr.append(random.randint(-100,100))

        merge(arr)
        print(is_sorted(arr))
        

if __name__ == "__main__":
    main()
