
# Problem Statement

"""
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
"""


# Solution


class Solution:
    def containsDuplicate(self, nums):
        # Create an empty set to store unique numbers
        seen = set()

        # Iterate through each number in the input list
        for num in nums:
            # If the number is already in the set, a duplicate exists
            if num in seen:
                return True  # Return True immediately

            # Otherwise, add the number to the set
            seen.add(num)

        # If no duplicates were found, return False
        return False


if __name__ == "__main__":
    # Example input list
    nums = [1, 2, 3, 1]

    # Create an instance of the Solution class
    sol = Solution()

    # Call the containsDuplicate method and store the result
    result = sol.containsDuplicate(nums)

    # Print the result
    print(result)
