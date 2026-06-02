class Solution:
    def subsetSums(self, nums: list[int]) -> list[int]:
        ans=[]
        n = len(nums)

        def solve(idx: int, current_sum: int):
            if idx == n:
                ans.append(current_sum)
                return

            solve(idx+1, current_sum + nums[idx])

            solve(idx+1, current_sum)

        solve(0,0)

        return ans