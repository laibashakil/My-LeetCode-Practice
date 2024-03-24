class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            num = str(num)
            ans += int(max(num) * len(num))
        return ans