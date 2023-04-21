from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = 0
        p2 = 0
        
        final = []
        
        while p1 < m and p2 < n:
            if nums1[p1] < nums2[p2]:
                final.append(nums1[p1])
                p1 += 1
            else:
                final.append(nums2[p2])
                p2 += 1
        
        if p1 <= m - 1:
            for i in range(p1, m):
                final.append(nums1[i])
        elif p2 <= n - 1:
            for i in range(p2, n):
                final.append(nums2[i])
                
        for i in range(0, len(final)):
            nums1[i] = final[i]