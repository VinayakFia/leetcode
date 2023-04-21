class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        prod = [[] for i in range(len(num1))]
        for i in range(len(num1) - 1, -1, -1):
            carry = 0
            prod[i] += [0] * ((len(num1) - 1) - i)
            for j in range(len(num2) - 1, -1, -1):
                mul = (int(num1[i]) * int(num2[j]) + carry) % 10
                carry = int((int(num1[i]) * int(num2[j]) - mul) / 10)
                prod[i].append(mul)
                print(prod, carry, i, j)  
        prod = [x.reverse() for x in prod]
        return ""
    
print(Solution().multiply("123", "456"))