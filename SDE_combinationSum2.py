class Solution:
    def combinationSum2(self, candidates, target):
        ans = []
        
        candidates.sort()
        
        def backtrack(idx, target, current_combination):
            
            if target == 0:
                ans.append(list(current_combination))
                return
            
            if target < 0:
                return
                
            for i in range(idx, len(candidates)):
                # Duplicate check: Agar is level par same element pehle le chuke hain, toh skip karo
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
               
                if candidates[i] > target:
                    break
                
                current_combination.append(candidates[i])
                
                backtrack(i + 1, target - candidates[i], current_combination)
                
                current_combination.pop()
                
        backtrack(0, target, [])
        return ans