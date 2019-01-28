#给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。
#说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。
'''
输入: [10,2]
输出: 210
'''

from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        num_to_str = [str(i) for i in nums]
        #ab>ba:1 ab<ba:-1 确定a,b的优先级
        num_to_str.sort(key=cmp_to_key(lambda a,b:(int(a+b)>int(b+a))-(int(a+b)<int(b+a))),reverse=True)
        return '0' if num_to_str[0]=='0' else ''.join(num_to_str)

    #python2
    def largestNumber1(self, nums):
        map_nums=map(str,nums)
        comp=lambda a,b:1 if a+b>b+1 else -1
        map_nums.sort(cmp=comp)
        map_nums=''.join(map_nums)
        if map_nums[0]=='0':
            return '0'
        return map_nums

if __name__ == '__main__':
    l=[3,30,34,5,9]
    sol=Solution()
    res=sol.largestNumber(l)
    print(res)