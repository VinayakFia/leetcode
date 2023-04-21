import math
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = 0
        n2 = 0
        n = len(nums1) + len(nums2)
        cur = 0
        prev = 0
        for i in range(math.ceil(n / 2)):
            prev = cur
            if nums1[n1] > nums2[n2]:
                cur = nums2[n2]
                n2 += 1
            else:
                cur = nums1[n1]
                n1 += 1
        if n % 2 == 1:
            return float(cur)
        else:
            return (cur + prev) / 2


print(Solution().findMedianSortedArrays([1, 2], [3, 4]))
