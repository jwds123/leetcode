'''
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。
'''


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        左下角
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False

        i = m - 1
        j = 0
        while i >= 0 and j < n:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j = j + 1
            else:
                i = i - 1
        return False
    # def searchMatrix(self, matrix, target):
    #     """
    #     :type matrix: List[List[int]]
    #     :type target: int
    #     :rtype: bool
    #     """
    #     rows = len(matrix)
    #     cols = len(matrix[0])
    #     if rows == 0 or cols==0:
    #         return False
    #     if target<matrix[0][0] or target>matrix[rows-1][cols-1]:
    #         return False
    #     i,j=0,0
    #     while i<=rows-1 and j<=cols-1:
    #         if target>matrix[i][j]:
    #             i+=1
    #             j+=1
    #         elif target<matrix[i][j]:
    #             if self.search([matrix[m][j] for m in range(i)],target)!=-1 or self.search(matrix[i][:j],target)!=-1:
    #                 return True
    #             else:
    #                 return False
    #         else:
    #             return True
    #     return False
    #
    #
    # def search(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: int
    #     """
    #     low = 0
    #     high = len(nums) - 1
    #     while low < high:
    #         mid = (low + high) // 2
    #         if target == nums[mid]:
    #             return mid
    #         elif target > nums[mid]:
    #             low = mid + 1
    #         else:
    #             high = mid - 1
    #     return low if nums[low] == target else -1

if __name__ == '__main__':
    sol = Solution()
    matrix=[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
    m=[[]]
    res=sol.searchMatrix(m,8)
    print(res)