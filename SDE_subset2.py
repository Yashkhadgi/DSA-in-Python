class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        
        ans = []
        nums.sort()
        
        def backtrack(idx: int, current_subset: list[int]):
            ans.append(list(current_subset))
            
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue

                current_subset.append(nums[i])
                backtrack(i + 1, current_subset)
                current_subset.pop()

        backtrack(0, [])
        return ans