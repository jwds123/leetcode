# 504. Base 7
进制转换

```python
def convertToBase7(num):
        """
        :type num: int
        :rtype: str
        """
        res = ''
        if num == 0:
            return '0'
        Num = abs(num)
        while Num:
            n = Num % 7
            Num = int(Num / 7)
            res = str(n) + res
        
        if num < 0:
            return '-' + res
        else:
            return res
    

```

# 20 Valid Parentheses
括号匹配
## 只有符号
"()[]{}"
```python
def isValid(s):
    if len(s)==0:
        return True
    if len(s)%2==1:
        return False
    match={'(':')','[':']','{':'}'}
    tmp=[]
    for i in s:
        if i in match:
        #tmp中的都是左边的符号
            tmp.append(i)
        #后进先出的左边符号和剩下的右边的符号是否匹配；tmp非空
        if not tmp or match[tmp.pop()]!=i:
            return False
    return tmp==[]
```

```python
def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    ops = {"]": "[", ")": "(", "}":"{"}
    stack = []
    for c in s:
        if c not in ops:
            stack.append(c)
            continue
        if not stack or stack.pop() != ops[c]:
            return False
    return False if stack else True        
```
## 678.Valid Parenthesis String
有字符串的符号匹配
只包含三种字符的字符串：（ ，） 和 \*，\* 可以被视为单个右括号 ) ，或单个左括号 ( ，或一个空字符串

```python
class Stack:  
    """模拟栈"""  
    def __init__(self):  
        self.items = []  
          
    def isEmpty(self):  
        return len(self.items)==0   
      
    def push(self, item):  
        self.items.append(item)  
    
    def pop(self):  
        return self.items.pop()   
      
    def top(self):  
        if not self.isEmpty():  
            return self.items[len(self.items)-1]  
          
    def size(self):  
        return len(self.items)   
    
class Solution:
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        '''
        ((())*)*)
        1.两个栈：左括号和*
        2.先是右括号与两个栈匹配，之前的左括号够用，就pop出来；不够用就将*pop出来，作为(
        3.右括号没有了，就拿左括号和*匹配,但左括号序数必须在*前面；左括号empty就OK了,左括号没有empty就是false
        '''
        leftP=Stack()
        starP=Stack()
        for i in range(len(s)):
            if s[i]=='(':
                leftP.push({'(':i})
            elif s[i]=='*':
                starP.push({'*':i})
            else:
                if leftP.size()>0:
                    leftP.pop()
                elif starP.size()>0:
                    starP.pop()
                else:
                    return False
        while leftP.isEmpty()==False and starP.isEmpty()==False:
            if leftP.top()["("]>starP.top()["*"]:
                return False
            leftP.pop()
            starP.pop()
        return leftP.isEmpty()
            
        
```

## 224.Basic caculator
基本计算器
实现一个基本的计算器来计算一个简单的字符串表达式的值。

字符串表达式可以包含左括号 ( ，右括号 )，加号 + ，减号 -，非负整数和空格 


```python
class Solution:
    def calculate(self,s):
        """
        :type s: str
        :rtype: int
        """
        '''
        括号、运算符、数字
        1.先运算
        2.栈：遇到(就将之前运算的数字结果以及最后一个运算符压入栈，遇到)就

        '''
        res,num,sign=0,0,1
        opS=[]
        for i in s:  
            #num:一个完整的数；res:括号内或者没遇到括号的完整的计算结果
            if i.isdigit():

                num=10*num+(int)(i)

                #print(num)
            elif i=='+' or i=='-':

                res=res+sign*num 
                num=0                
                sign=1 if i=='+' else -1
            elif i=='(':  
                opS.append(res)
                opS.append(sign)
                res=0
                sign=1
            elif i==')': 
                #res:括号里面的结果
                res=res+sign*num
                num=0
                #sign=1
                res*=opS.pop()
                res+=opS.pop()
            #print(res)
            elif i==' ':
                continue
        #print(res)        
        res=res+sign*num   

        return res

```
## Basic calculator2
基础计算器2
字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。


```python
class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=[]
        num=0
        pre_op='+'
        for i,each in enumerate(s):

            if each.isdigit():
                num=10*num+(int)(each)
                
            if each in '+-*/' or i==len(s)-1 :
                #sign=1 if i=='+' else -1
                if pre_op=='+':
                    res.append(num)
                elif pre_op=='-':
                    res.append(-num)
                elif pre_op=='*':
                    res.append(res.pop()*num)
                elif pre_op=='/':
                    n=res.pop()
                    if n>=0:
                        res.append(n//num)
                    else:
                        res.append(int(n/num))
                
                pre_op=each
                num=0             
        return sum(res)
```
