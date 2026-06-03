class Solution:
    def getPermutation(self, n, k):
        # Step 1: Pre-calculate factorials from 0! to 9!
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i
            
        # Step 2: Create a list of available numbers [1, 2, 3, ..., n]
        numbers = []
        for i in range(1, n + 1):
            numbers.append(i)
            
        # Step 3: Convert k to 0-based index
        k = k - 1
        ans = ""
        
        # Step 4: Core loop to find each position's digit
        for i in range(n, 0, -1):
            # Block size for the remaining characters
            # Agar 4 chars bache hain, to partition size 3! hota hai
            block_size = fact[i - 1]
            
            # Find the index of the number to pick
            index = k // block_size
            
            # Append the number to our answer string
            ans += str(numbers[index])
            
            # Remove that number from our available pool
            numbers.pop(index)
            
            # Update k for the next iteration
            k = k % block_size
            
        return ans