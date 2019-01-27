class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            return str(x) == str(x)[::-1]#字符串逆序

        # if x < 0:
        #     return False
        # y = 0
        # z = x
        # while z:
        #     # y从后往前
        #     y = y * 10 + z % 10
        #     z = z / 10
        # if y == x:
        #     return True
        # return False
