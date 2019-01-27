# bubble

```python
def bubble_sort(nums):
    for i in range(1,len(nums)):
        for j in range(1,len(nums)-i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums        
```

# selection

```python
def selection_sort(nums):
    for i in range(len(nums)-1):
        minIndex=i#前i个最小值
        for j in range(i,len(nums)-1):
            if nums[j]<nums[minIndex]:
                minIndex=j
        if i!=minIndex:
            nums[i],nums[minIndex]=nums[minIndex],nums[i]
    return nums
```

# insert

```python
def insert_sort(nums):
    for i in range(len(nums)):
        preIndex=i-1
        current=nums[i]
        '''只要前面序列中的数大于current，就向后一位'''
        while preIndex>0 and nums[preIndex]>current:
            nums[preIndex+1]=nums[preIndex]
            preIndex-=1
        nums[preIndex+1]=current
    return nums    
```
# shell

```

```

# merge

```python
'''
申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列；
设定两个指针，最初位置分别为两个已经排序序列的起始位置；
比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置；
重复步骤 3 直到某一指针达到序列尾；
将另一序列剩下的所有元素直接复制到合并序列尾。
'''

def merge_sort(nums):
    if len(nums)<2:
        return nums
    #1.序列一分为二
    mid=len(nums)//2
    left,right=nums[0:mid],nums[mid:]
    #2.子序列递归排序：分成最小的单元2-3个，有序合并
    #3.合并子序列
    return merge(merge_sort(left),merge_sort(right))
   '''
    merge_sort先，也就是先把左边（左边右边），2-3个为最小单位，各指向分好的左右边的初始位置，选择相对小的放入合并空间；
    左边，左边，右边，左边，右边；右边，左边，右边，左边，右边；
    每一个（左边，右边）一合并
    '''    
def merge(left,right):
    result=[]
    if left[0]>right[0]:
        result.append(left.pop(0))
    else:
        result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result
    
```

# quick
从数列中挑出一个元素，称为 “基准”（pivot）；
重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。

## 左右指针法

```python
'''
① 选择最左边的数为基准数key
② 设立两个游标 low 和 high , 分别指向数组的最低位和最高位
③ 然后high先动, 如果high位上的数比key大, 则向前走, 如果high-1位上的数比key大, 继续向前走, 直到该位上的数<=key
④ 此时比较low位, 如果<=key, low向后走, 变为low+1, 依次类推, 直到该位上的数比key大
⑤ 交换high和low位上的数
'''
def quick_sort(nums,l=None,r=None):
    l = 0 if not isinstance(l,(int, float)) else l
    r = len(array)-1 if not isinstance(r,(int, float)) else r
    if l<r:
        keyIndex=partition1(nums,l,r)
        #先左后右
        quick_sort(nums,l,keyIndex)
        quick_sort(nums,keyIndex+1,r)
    return nums
    
#左右指针  
def partition1(arr,l,r):
    keyIndex=r
    key=arr[r]
    while l<r:
        while l<r and arr[l]<=key:
            l+=1
        while l<r and arr[r]>key:
            r-=1
        #此时，arr[l]>key arr[r]<key-->交换
        arr[l],arr[r]=arr[r],arr[l]
    #l的位置就是大于和小于基准的分界线        
    arr[l+1],arr[keyIndex]=arr[keyIndex],arr[l+1]
    return l

#挖坑法
def partition2(arr,l,r):
#代表比基准小的index
    Index=l-1
    key=arr[r]
    for j in range(l,r):
    #arr[j]<=key那么index（代表比基准小的）可以向前走了,同时将小的数放到Index位置上
        if arr[j]<=key:
            Index+=1
            arr[Index],arr[j]=arr[j],arr[Index]
    #Index以后的数就是大于key的数了，交换
    arr[Index+1],arr[r]=arr[r],arr[Index]
```
## 快排简洁版

```
quick_sort = lambda array: array if len(array) <= 1 else quick_sort([item for item in array[1:] if item <= array[0]]) + [array[0]] + quick_sort([item for item in array[1:] if item > array[0]])
    

```
