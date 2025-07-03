class Solution:
    # O(N)
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1, nums2 = set(nums1), set(nums2)
        return [list(nums1 - nums2), list(nums2 - nums1)]


    # O(N)
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1, nums2 = set(nums1), set(nums2)
        diff = []
        for num in nums1:
            if num in nums2:
                nums2.remove(num)
            else:
                diff.append(num)
                
        return [diff, list(nums2)]
