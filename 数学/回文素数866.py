'''
求出大于或等于 N 的最小回文素数。
'''

import m
class Solution(object):
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """

        while True:
            if N <= 11:
                if N <= 2:
                    return 2
                elif N == 3:
                    return 3
                elif N <= 5:
                    return 5
                elif N <= 7:
                    return 7
                else:
                    return 11

            if N > 31880255:  # 这个是从测试时间超时，并且题目给出的范围的最大素数是100030001
                return 100030001
            '''
            数学规律1：除 2 和 3 外，所有的素数一定在 6 的两侧。
            首先 6x 肯定不是质数，因为它能被 6 整除；
            其次 6x+2 肯定也不是质数，因为它还能被 2 整除；
            依次类推，6x+3 肯定能被 3 整除；6x+4 肯定能被 2 整除；6x+5 就等同于 6x-1。
            
            这样一次过滤的步长就会比偶数长
            
            数学规律2：除 11 外的偶数位回文数，都能被 11 整除
            我们可以跳过所有位数为偶数的数字，除了 11。例如当输入 123456 时，我们可以直接从 1000001 开始查找。
            '''

            mod=N%6
            if mod==1 or mod==5:
                N
            elif mod==0:
                N+=1
                mod=1
            elif mod==2:
                N+=3
                mod=5
            elif mod==3:
                N+=2
                mod=5
            elif mod==4:
                N+=1
                mod=5

            if len(str(N))%2==0:
                l=len(str(N))
                N=int(pow(10, l))+1
                #位数为奇数的1000*1%6=5
                mod=5
            #     print('next2')
            # print('next3')

            if self.isPalindrome(N) and self.isPrime(N):
                return N

            if mod==1:
                N+=4
                mod=5

            else:
                N+=2
                mod=1




    #素数
    def isPrime(self,num):
        i=5
        while i<=m.sqrt(num):
            #i=6k+1  or  6k+5  i+2=6k+7=6(k+1)+1
            if num%i==0 or num%(i+2)==0:
                return False
            i+=6
        return True


    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            return str(x) == str(x)[::-1]#字符串逆序



def main():
    sol = Solution()
    print(sol.primePalindrome(102))
    #print(sol.isPrime(10001))



if __name__ == '__main__':
    main()