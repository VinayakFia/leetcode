from typing import List
from unicodedata import digit


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[len(digits) - 1] += 1
        
        if digits[len(digits) - 1] >= 10:
            for i in range(len(digits) - 1, -1, -1):
                if digits[i] >= 10:                  
                    digits[i] = digits[i] % 10
                    if i == 0:
                        digits.insert(0, 1)
                    else:
                        digits[i - 1] += 1
        
        return digits

print(Solution().plusOne([9, 9, 9]))