from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for idx, n in enumerate(nums):
            complement = target - n
            if complement in hash_map:
                return [hash_map[complement], idx]
            else:
                hash_map[n] = idx



if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    val = solution.twoSum(nums=nums, target=target)
    print(val)
