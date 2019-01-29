'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=len(nums)
        max_sum=nums[0]
        onesum=0
        for i in range(k):
            onesum+=nums[i]#当前和
            max_sum=max(max_sum,onesum)
            if onesum<0:#那加上onesum必然比之前的max_sum小
                onesum=0
        return max_sum

if __name__ == '__main__':
    sol = Solution()
    nums=[-2,1,-3,4,-1,2,1,-5,4]
    res=sol.maxSubArray(nums)
    print(res)
