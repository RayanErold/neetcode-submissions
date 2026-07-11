class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Sorted array approach 
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k, target = i + 1, len(nums) - 1, -nums[i]
            while j < k:
                currSum = nums[j] + nums[k]
                if currSum < target:
                    j = j + 1
                elif currSum > target:
                    k = k - 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]: j += 1
                    while j < k and nums[k] == nums[k-1]: k -= 1
                    j = j + 1
                    k = k - 1
        return res