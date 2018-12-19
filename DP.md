# LCS最长公共序列
## 递归

长度
```python
def recursive_lcs(str_a, str_b):
    if len(str_a) == 0 or len(str_b) == 0:
        return 0
    if str_a[0] == str_b[0]:
        return recursive_lcs(str_a[1:], str_b[1:]) + 1
    else:
        return max([recursive_lcs(str_a[1:], str_b), recursive_lcs(str_a, str_b[1:])])
```

序列
```python
def lcs(A,B):
    if A=='' or B=='':
        return ''
    if A[-1]==B[-1]:
        return lcs(A[:-1],B[:-1])+A[-1]
    else:
        sol_a=lcs(A[:-1],B)
        sol_b=lcs(A,B[:-1])
        if len(sol_a)>len(sol_b):
            return sol_a
        return sol_b
```

## 迭代

长度
```python
def lcs_dp(A,B):
    '''
    做个列表，A是行，B是列
    '''
    dp=[[0]*len(B)+1 for i in range(len(A)+1)]
    for i in range(1,len(A)+1):
        for j in range(1,len(B)+1):
            #子问题：前一行和列有相等的，那么行与列都加一，划掉
            if A[i-1]==B[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            #子问题：前一行和列不相等，那么行与列选择上一行和上一列更大的
            else:
                dp[i][j]=max(dp[i-1,j],dp[i,j-1])
    for dp_line in dp:
        print(dp_line)
    return dp[-1][-1]
```
长度与序列

```python
class LCS:
    def lcs_dp(self, input_x, input_y):
        # input_y as column, input_x as row
        dp = [([0] * (len(input_y)+1)) for i in range(len(input_x)+1)]
        maxlen =  0
        res=''
        for i in range(1, len(input_x)+1):
            for j in range(1, len(input_y)+1):

                if input_x[i-1] == input_y[j-1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:  # 不相等
                    dp[i][j] = max(dp[i - 1][j], dp[i][j -1])
        for dp_line in dp:
            print(dp_line)
            
        for i in range(1,dp[-1][-1]+1):
            for j in range(1,len(input_x)+1):
                #最后一列
                if dp[j][-1]==i:
                    res+=input_x[j-1]
                    break
        return dp[-1][-1], res

def main():
    A="bdhkbef"
    B="bbkdfghkw"
    lcs = LCS()
    #res=lcs_dp(A,B)
    print(lcs.lcs_dp(A,B))
```

# 最长公共子字符串


```python
class LCS1:
    def lcs1_dp(self, input_x, input_y):
        # input_y as column, input_x as row
        dp = [([0] * (len(input_y)+1)) for i in range(len(input_x)+1)]
        maxlen =maxIndex= 0
        res=''
        for i in range(1, len(input_x)+1):
            for j in range(1, len(input_y)+1):

                if input_x[i-1] == input_y[j-1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                '''不同：只有下一个行与列同时递增，才可以'''
                    if dp[i][j]>maxlen:
                        maxlen=dp[i][j]
                        maxIndex=i-maxlen 
                        #current position-maxlen:初始的位置
        for dp_line in dp:
            print(dp_line)
    
        return maxlen,input_x[maxIndex:maxIndex+maxlen] 
```
