
# Problem Statement

"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""


# Solution


class Solution:
    def longestCommonPrefix(self, strs):
        # Edge case: If the input list is empty, return an empty string
        if not strs:
            return ""

        # Iterate through each character index of the first word in the list
        for i in range(len(strs[0])):
            # Compare the character at index 'i' with every other word in 'strs'
            for word in strs[1:]:  # Skipping the first word since we're comparing against it
                # If 'i' exceeds the current word's length OR there's a mismatch in characters
                if len(word) == i or word[i] != strs[0][i]:
                    # Return the prefix found so far (substring from 0 to i)
                    return strs[0][:i]

        # If no mismatch is found, return the entire first word (it is the common prefix)
        return strs[0]


# Driver code to test the function
if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]  # Example input
    print(Solution().longestCommonPrefix(strs))  # Expected output:
