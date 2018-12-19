# 二分查找
优点是比较次数少，查找速度快，平均性能好；其缺点是要求待查表为有序表，且插入删除困难。
## 递归
```python
def binary_chop(alist, data):
    n=len(alist)
    if n<1:
        return False
    mid=n//2#整数部分 math.floor
    if alist[mid]>data:
        return binary_chop(alist[0:mid],data)
    elif alist[mid] < data:
        return binary_chop(alist[mid:],data)
    else:#相等
        return True
    
```
## 非递归
定义两个指针，first,last

```python
def binary_chop(alist, data):
    n=len(alist)
    first=0
    last=n-1
    #非退化
    while fist<last:
        mid=(first+last)/2
        if alist[mid] > data:
            last = mid - 1
        elif alist[mid] < data:
            first = mid + 1
        else:
            return True
    return False
```
# 二分查找改进
## version A
对middle point采用不同策略：
对于任意A[0,n],分成kn与(1-k)n。
需要看数列差，均匀非均匀，如fib数列
