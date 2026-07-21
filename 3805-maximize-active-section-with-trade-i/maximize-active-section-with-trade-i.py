class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        total_active = s.count('1')
        s = "1" + s + '1'
        n = len(s)
        max_active = total_active
        i = 0
        while i < n and s[i] == '1':
            i += 1

        #left zeroes 
        left_zero_count = 0
        while i < n and s[i] == '0':
            left_zero_count += 1
            i += 1
        
        while i < n:

            middle_ones = 0
            while i < n and s[i] == '1':
                middle_ones += 1
                i += 1
            
            if middle_ones == 0:
                break

            right_zero_count = 0
            while i < n and s[i] == '0':
                i += 1
                right_zero_count += 1
            
            if right_zero_count == 0:
                break
            
            max_active = max(max_active, left_zero_count + right_zero_count + total_active)
            
            left_zero_count = right_zero_count
        return max_active