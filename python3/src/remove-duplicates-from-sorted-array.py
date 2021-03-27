from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums.pop(i + 1)
            else:
                i += 1

        return len(nums)


print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])) # [0,1,2,3,4]