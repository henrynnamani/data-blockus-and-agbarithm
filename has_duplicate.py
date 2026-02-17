class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        present = {};

        for num in nums:
            if num not in present:
                present[num] = 1
            else:
                return True

        return False
