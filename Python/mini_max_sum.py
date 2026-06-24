
# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.
# 
# Example
# The minimum sum is and the maximum sum is . The function prints
# 16 24


def miniMaxSum(arr):
    index = 0  #O(1)
    sum_arr = [] #O(1)
    
    for element in range(len(arr)): #=(n)
        new_list = arr[:index] + arr[index + 1:] # O(n)
        total = sum(new_list) # O(n)
        sum_arr.append(total) # O(1)
        
        index += 1 # O(n)
              
    print(min(sum_arr), max(sum_arr))
    



miniMaxSum([1, 2, 3, 4, 5]) # 10 14   ---> O(n^2) because of the nested loops and sum function. The overall time complexity is O(n^2)
miniMaxSum([7, 69, 2, 221, 8974]) # 299 9271   ---> O(n^2) because of the nested loops and sum function. The overall time complexity is O(n^2)