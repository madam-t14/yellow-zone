""" Inseration Sort Algorithm
 A simple sorting algorithm that builds the final sorted list one element at a time. It iterates over the input list, removing one element from the input data and inserting it into the correct position in the already-sorted portion of the list.

    Time Complexity: 
 
    Best Case: O(n) - when the list is already sorted.
    Average Case: O(n^2) - when elements are randomly ordered.
    Worst Case: O(n^2) - when elements are sorted in reverse order.

    Space Complexity:
    O(1)
 """


def inseration_sort(nums):
    # Iterate over the nums array
    # Start from second elements
    for currentNum in range(1, nums):
        
        # Choose current number to be inserted in right side of the array 
        number_to_insert  =  nums[currentNum]

        # Compare with the previous number in sub-array
        next_num =  currentNum  -1

        # Continue moving elements to the right until finding the correct position
        while next_num >= 0 and next_num > currentNum:
            
            # Move the elements to the right to make space for the current number
            nums[next_num + 1] =  nums[next_num]
            
            # Move to the previous number for comparison
            next_num -=1
        
        # Insert the current number at its correct position
        nums[next_num] = number_to_insert
    
    return nums