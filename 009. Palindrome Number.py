
# Problem Statement

# Given an integer x, return true if x is a palindrome, and false otherwise.


# Solution

import sys

import sys  # Import sys for fast input handling


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Checks if an integer is a palindrome without converting it to a string.
        Uses a mathematical approach to compare the reversed half of the number.
        """
        # Negative numbers and numbers ending in 0 (except 0) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10  # Extract and build reversed half
            x //= 10  # Reduce original number by removing last digit

        # Compare first half and reversed half (handles odd & even digit cases)
        return x == reversed_half or x == reversed_half // 10


if __name__ == "__main__":
    x = int(sys.stdin.readline().strip())  # Read input and remove newline

    # Creating an instance of Solution class
    sol = Solution()

    # Calling the isPalindrome function and printing the result
    ans = sol.isPalindrome(x)
    print(ans)
