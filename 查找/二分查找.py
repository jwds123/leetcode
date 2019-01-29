'''
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。


示例 1:

输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
'''
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low=0
        high=len(nums)-1
        while low<high:
            mid=(low+high)//2
            if target==nums[mid]:
                return mid
            elif target>nums[mid]:
                low=mid+1
            else:
                high=mid-1
        return low if nums[low]==target else -1

if __name__ == '__main__':
    sol = Solution()
    nums=[-1,0,3,5,9,12]
    res=sol.search(nums,9)
    print(res)