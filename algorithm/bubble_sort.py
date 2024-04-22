""" Simple algorithm to sort things by swapping position using Bubble Sort Theorm
    Big-O complexity ==> O(n^2)
    What's this Algorith about ?
    - The algorithm is pretty simple: compare two items in an array that are next to each other.
      If they're out of order (that is, the larger one comes first in the array) swap them. 
      Then move forward one index, compare again, swap if needed, and continue to the next item in the array. 
      Once we've reached the end of the array, if we've swapped anything in the previous run through, 
      the array could still be out of order, so we have to pass through again. Once we run through 
      the whole array with no swaps, the array is sorted!
 """


def bubble_sort(nums):

    print('Hello')
    # #? Primary Idea
    # sorted  = False
    # count   =  0
    # n       = len(nums)
    
    # while True :
    #     for i in range(n-1):
    #         if nums[i] > nums[i+1]:
    #             # swap position
    #             nums[i], nums[i+1]  = nums[i+1] ,nums[i]
    #             # Reset the count
    #             count = 0    
    #         else :
    #             count+=1
    #             if count == n:
    #                 break
    #     if count == n:
    #                 break
    

    # More Efficient Way
    n =  len(nums)
    while True:
        swapped =  False

        for i in range(n-1) :
            if (nums[i] > nums[i+1] ):
                # Reorder the pair
                nums[i] , nums[i+1] = nums[i+1] ,nums[i]
                # print(f'Swapped : {nums}')  #DEBUG
                swapped =  True
            
            
        # print(f"Swap Condn: {swapped}")  #DEBUG
        # Once Swapped is False means Sorted break it!
        if not swapped:
            print(nums)
            break   
    return nums


    

nums = [1,2,5,9,7,10,8,3,4,6]
bubble_sort(nums)
print(nums)
