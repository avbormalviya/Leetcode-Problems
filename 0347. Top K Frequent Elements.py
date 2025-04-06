
# Problem Statement

"""
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.
"""


# Solution


from collections import defaultdict


class Solution:
    def topKFrequent(self, nums, k):
        # Step 1: Count frequency of each number
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        # Step 2: Create a bucket array where index represents frequency
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            bucket[count].append(num)

        # Step 3: Collect top k elements from the highest frequency buckets
        result = []
        for i in range(len(nums), 0, -1):  # Loop from highest frequency to lowest
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result  # Stop early when we have k elements

        return result  # Edge case: If k == len(freq), return everything


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    solution = Solution()
    result = solution.topKFrequent(nums, k)
    print(result)
