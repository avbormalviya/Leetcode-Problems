
# problem Statement

"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
"""

# Solution


from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        # Dictionary to store anagram groups, using a tuple of letter counts as keys
        dic = defaultdict(list)

        for word in strs:
            # Create a frequency array for 26 lowercase English letters
            count = [0] * 26

            # Update frequency array based on character occurrences in the word
            for char in word:
                count[ord(char) - ord('a')] += 1  # Convert char to index and increment count

            # Convert list to tuple (hashable) and use it as a key in the dictionary
            dic[tuple(count)].append(word)

        # Return all values (lists of anagram groups) from the dictionary
        return list(dic.values())


if __name__ == "__main__":
    # Test case 1: Standard case with multiple anagram groups
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

    # Test case 2: Edge case with an empty string
    print(Solution().groupAnagrams([""]))
