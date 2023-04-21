from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set(nums1)
        for num in nums2:
            if num not in res: res.remove(num)
        return list(res)