'''
如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为摆动序列。
第一个差（如果存在的话）可能是正数或负数。少于两个元素的序列也是摆动序列。
给定一个整数序列，返回作为摆动序列的最长子序列的长度。
通过从原始序列中删除一些（也可以不删除）元素来获得子序列，剩下的元素保持其原始顺序。

例如， [1,7,4,9,2,5] 是一个摆动序列，因为差值 (6,-3,5,-7,3) 是正负交替出现的。
相反, [1,4,7,2,5] 和 [1,7,4,5,5] 不是摆动序列，
第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。
'''
class Solution(object):
    #时间复杂度是O(N)，空间复杂度是O(N).
    def wiggleMaxLength(self, nums):
        k = len(nums)
        if k < 2:
            return k
        inc,dec=[0]*k,[0]*k
        for i in range(1,k):
            if nums[i]-nums[i-1]>0:
                inc[i]=dec[i-1]+1
                dec[i]=dec[i-1]
            elif nums[i]-nums[i-1]<0:
                inc[i]=inc[i-1]
                dec[i]=inc[i-1]+1
            else:
                inc[i]=inc[i-1]
                dec[i]=dec[i-1]
        return max(inc[-1],dec[-1])

    '''
    简单分析代码就可以看出，每个元素都只和它之前的元素相关，因此，只需要使用两个变量即可。
    时间复杂度是O(N)，空间复杂度是O(1).
    '''
    def wiggleMaxLength1(self, nums):
        k = len(nums)
        if k < 2:
            return k
        inc,dec=1,1
        for i in range(1,k):
            if nums[i]-nums[i-1]>0:
                inc=dec+1
            elif nums[i]-nums[i-1]<0:
                dec=inc+1
        return max(inc,dec)
    # def wiggleMaxLength(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     k=len(nums)
    #     if k<2:
    #         return k
    #
    #     count=k
    #     def judge_sign(i,j):
    #         if j-i> 0:
    #             sign = 1
    #         elif j-i < 0:
    #             sign = -1
    #         else:
    #             sign = 0
    #         return sign
    #
    #     pre=judge_sign(nums[0],nums[1])
    #     if pre == 0:
    #         count -= 1
    #     for i in range(1,k-1):
    #         cur=judge_sign(nums[i],nums[i+1])
    #         if cur==0 or pre*cur==1:
    #             count-=1
    #         pre=cur
    #     return count

if __name__ == '__main__':
    sol = Solution()
    nums=[1,17,5,10,13,15,10,5,16,8]
    n2=[0,0,0,0]
    n3=[1,7,4,9,2,5]
    n4=[3,3,3,2,5,5,5,7,2]
    res=sol.wiggleMaxLength(n4)
    print(res)

