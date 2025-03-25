
# Problem Statement

"""
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with
the smallest space complexity possible.
"""


# Solution


import random


class Solution:
    def sortArray(self, input_arr):
        if not input_arr:
            return []  # Return an empty list if input is empty

        min_val = min(input_arr)  # Find the smallest value in the array
        max_val = max(input_arr)  # Find the largest value in the array

        # Offset for negative numbers
        offset = -min_val  # Shift negative numbers to positive range

        # Create count array
        count_arr = [0] * (max_val - min_val + 1)  # Initialize count array based on range of values

        # Count occurrences
        for num in input_arr:
            count_arr[num + offset] += 1  # Shift numbers using offset to fit in count array

        # Build sorted array
        output_arr = []
        for i in range(len(count_arr)):
            output_arr.extend([i - offset] * count_arr[i])  # Shift back to original values

        return output_arr  # Return the sorted array


if __name__ == "__main__":
    input_arr = [3, 2, 1, 5, 6, 4, -2, -5, 0]
    sol = Solution()
    sorted_arr = sol.sortArray(input_arr)  # Assign the sorted array
    print(sorted_arr)  # Print the sorted array
