class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total_sum = 0
        
        for num in nums:
            div_sum = 0
            div_count = 0
            
            # We only need to iterate up to the square root of num
            limit = int(math.isqrt(num))
            
            for i in range(1, limit + 1):
                if num % i == 0:
                    # Found a divisor 'i'
                    div_count += 1
                    div_sum += i
                    
                    # Found the pair divisor 'num // i'
                    if i * i != num:
                        div_count += 1
                        div_sum += num // i
                    
                    # Optimization: If count exceeds 4, we can stop early
                    if div_count > 4:
                        break
            
            # Only add to total if exact count is 4
            if div_count == 4:
                total_sum += div_sum
                
        return total_sum
        