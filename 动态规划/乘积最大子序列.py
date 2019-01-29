'''
给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
'''
class Solution(object):
    def maxProduct(self, nums):
        """
        one_prod此前为负
        """
        k=len(nums)
        max_prod=nums[0]
        min_prod=nums[0]
        res=nums[0]
        for i in range(1,k):
            one=max_prod*nums[i]#乘上当前数字的结果,需要记得负负得正，最大变最小
            two=min_prod*nums[i]
            max_prod=max(max(one,two),nums[i])
            min_prod=min(min(one,two),nums[i])
            res=max(res,max_prod)
        return res
if __name__ == '__main__':
    sol = Solution()
    nums=[2,3,0,-2,4,-3,0,2]
    res=sol.maxProduct(nums)
    print(res)