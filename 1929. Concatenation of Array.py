
# Problem Statement

"""
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and
ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.
Return the array ans.
"""


# Solution


class Solution:
    def getConcatenation(self, nums):
        # Returns a new list that is a concatenation of nums with itself
        return nums * 2  # Equivalent to nums + nums


# This ensures the code runs only when executed directly
if __name__ == "__main__":
    # Example input list
    nums = [1, 2, 1]

    # Create an instance of the Solution class
    sol = Solution()

    # Call the getConcatenation method and store the result
    ans = sol.getConcatenation(nums)

    # Print the output list
    print(ans)  # Expected output: [1, 2, 1, 1, 2, 1]
