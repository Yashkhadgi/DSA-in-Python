class Solution:
    def combinationSum(self, candidates, target):
        ans = [] 
        n = len(candidates)

        
        def backtrack(idx, target, current_combination):
            if target == 0:
                ans.append(list(current_combination))
                return
            if target < 0 or idx == n:
                return

            
            current_combination.append(candidates[idx])

            
            backtrack(idx, target - candidates[idx], current_combination)

            current_combination.pop()

            backtrack(idx + 1, target, current_combination)

        backtrack(0, target, [])
        return ans
    