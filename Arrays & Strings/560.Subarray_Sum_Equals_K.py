class Solution:
    # Time: O(N), Space: O(N)
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1
        count = total = 0
        
        for num in nums:
            total += num
            count += prefix_sums[total - k]
            prefix_sums[total] += 1

        return count

