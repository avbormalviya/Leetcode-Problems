
# Problem Statement

"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""


# Solution


class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):  # If lengths differ, they can't be anagrams
            return False

        freq = dict()

        for char_s, char_t in zip(s, t):  # Process both strings together
            freq[char_s] = freq.get(char_s, 0) + 1
            freq[char_t] = freq.get(char_t, 0) - 1

        return all(count == 0 for count in freq.values())  # Check all counts are zero


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"

    # Create an instance of the Solution class
    solution = Solution()

    # Print the result
    print(solution.isAnagram(s, t))
