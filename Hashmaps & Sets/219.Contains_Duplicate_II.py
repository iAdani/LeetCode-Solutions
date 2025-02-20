# O(N)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen = {}

        for idx in range(len(nums)):
            if nums[idx] in last_seen:
                if idx - last_seen[nums[idx]] <= k:
                    return True
            last_seen[nums[idx]] = idx
        
        return False
        