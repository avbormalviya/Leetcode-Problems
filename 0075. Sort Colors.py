
# Problem Statement

"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of
the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""


# Solution


class Solution:
    def sortColors(self, arr):
        # Initialize pointers:
        # 'low' points to the position where the next 0 should go
        # 'mid' is the current element being evaluated
        # 'high' points to the position where the next 2 should go
        low = 0
        mid = 0
        high = len(arr) - 1

        # Loop until 'mid' crosses 'high'
        while mid <= high:
            if arr[mid] == 0:  # If the current element is 0
                # Swap the current element with the element at 'low'
                arr[low], arr[mid] = arr[mid], arr[low]
                # Move both 'low' and 'mid' pointers forward
                low += 1
                mid += 1

            elif arr[mid] == 1:  # If the current element is 1
                # No swap needed; just move the 'mid' pointer forward
                mid += 1

            else:  # If the current element is 2
                # Swap the current element with the element at 'high'
                arr[mid], arr[high] = arr[high], arr[mid]
                # Move the 'high' pointer backward
                high -= 1

        # Return the sorted array
        return arr


if __name__ == "__main__":
    input_arr = [2, 0, 2, 1, 1, 0]
    sol = Solution()
    sorted_arr = sol.sortColors(input_arr)  # Assign the sorted array
    print(sorted_arr)  # Print the sorted array
