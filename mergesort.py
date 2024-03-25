from colorama import Fore, Back, Style
from playsound import playsound
import matplotlib.pyplot as plt
import numpy as np
import time

#playsound("C:/Users/keena/Music/default.mp3")

def mergeSort(array, depth=0):
    # 1. Check if array length is greater than 1
    if len(array) > 1:
        # 2. If array length > 1, split the array into left subarray and right subarray
        # Find middle index of array
        mid = len(array) // 2 
        #print("Array length:", len(array))
        #print("Middle index:", mid)
        
        # Split array into left and right
        left = array[:mid] # Start of array to middle index
        right = array[mid:] # Middle index to end of array

        print("Depth:", str(depth) + "." + " Splitting " + str(array))
        time.sleep(1)
        
        # Call function on left half
        mergeSort(left, depth + 1)
            # 1. Check if left subarray greater than 1
            # 2. Split into left and right
            # 3. Call function on left
        # Call function on right half
        mergeSort(right, depth + 1)
        
            # 1. Check if left subarray greater than 1
            # 2. Split into left and right
            # 3. Call function on left

        i = 0 # Current index of left subarray
        j = 0 # Current index of right subarray
        k = 0 # Current index of full array
        
        # Merge elements from left subarray and right subarray into full array sorted lowest to highest
     
        count = 0
        print("\n Depth: " + str(depth) + "." + " Merging " + str(left) + " and " + str(right))    
        time.sleep(1)
        while i < len(left) and j < len(right):
            count += 1 # Count steps
            # While loop: 
            # while left subarray index (i) is within the length of the left subarray 
            # AND right subarray index (j) is within the length of the right subarray, run code in loop
            #print("Element:", k)
            
            if left[i] < right[j]: 
                print(str(count)+".", Back.RED + "No change:" + Style.RESET_ALL, "Left element", left[i], "is less than right element", right[j])
                # Compare element at i in left subarray with element at j in right subarray
                # If the element in the left half is smaller than the element in the right half, the left element goes before the element in the right half in the array
                array[k] = left[i]
                i += 1 # Move to next element in left subarray
                time.sleep(1)
            else: 
                playsound("C:/Users/keena/Music/default.mp3")
                print(str(count)+".", Back.GREEN + "SWAP:" + Style.RESET_ALL, "Right element", right[j], "is less than / equal to left element", left[i])
                # Compare element at j in right subarray with element at i in left subarray
                # If the element in the right half is smaller or equal to the element in the left half, the right element goes before the element in the left half of the array
                array[k] = right[j]
                time.sleep(1)
                j += 1 # Move to next element in right subarray
            k += 1 # Move to next element in the final array
            
        # Place any remaining elements in the left or right subarray into the final array
        # If the size of the left and right subarray is not equal, there may be a remaining element that has not been placed into the final array
        while i < len(left):
            # While loop: 
            # If i is less than the length of the left subarray, there are elements remaining in the left subarray to be merged with the right subarray
            # while left subarray index (i) is within the length of the left subarray, run code in loop
            
            array[k] = left[i] # Assign element at index i of left subarray to index k of final array
            
            i += 1 # Move to next element in left subarray
            k += 1 # Move to next element in final array

        while j < len(right):
            # While loop: 
            # If j is less than the length of the right subarray, there are elements remaining in the right subarray to be merged with the left subarray
            # while right subarray index (j) is within the length of the right subarray, run code in loop

            array[k] = right[j] # Assign element at index j of right subarray to index k of final array
            j += 1 # Move to next element in right subarray
            k += 1 # Move to next element in final array
        print("Merged array: ", array)
        print("-"*30)
        time.sleep(2)
    elif len(arr) <= 1: # If the length of the array is less than/equal to 1, do not split it
        print("No split")

#arr = [38, 27, 43, 3, 9, 82, 10]
arr = [11, 1, 30, 2, 51, 6, 29, 7, 67, 15, 118, 4, 89, 23]
mergeSort(arr)
print("Sorted array:", arr)
