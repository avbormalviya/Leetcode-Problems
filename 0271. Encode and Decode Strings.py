
# Problem Statement

"""
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back
to the original list of strings.

Please implement encode and decode
"""


# Solution


class Solution:

    def encode(self, strs) -> str:
        """Encodes a list of strings into a single string."""
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str):
        """Decodes a single string back into a list of strings."""
        result = []
        i = 0

        while i < len(s):
            # Find the next occurrence of '#' to determine the length prefix
            j = i
            while s[j] != "#":
                j += 1  # Move j to find '#'

            length = int(s[i:j])  # Extract length of the string
            word = s[j + 1: j + 1 + length]  # Extract the actual string
            result.append(word)

            i = j + 1 + length  # Move i to the next encoded part

        return result


if __name__ == "__main__":
    solution = Solution()
    strs = ["lint", "code", "love", "you"]
    encoded = solution.encode(strs)
    print(encoded)  # Output: "4#lint1#code1#love1#you"
    decoded = solution.decode(encoded)
    print(decoded)  # Output: ["lint", "code", "love", "you"]
