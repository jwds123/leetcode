class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<=1:
            return [nums]
        #前两个数字组成的全排列
        output = [[nums[0],nums[1]],[nums[1],nums[0]]]
        
        for i in range(2,len(nums)):            
            tmp = nums[i]#第三个及以后数字
            output_new = []
            for j in range(len(output)):
                #将新的数字接在n-1长度全排列的后面,output长度增加1
                output[j].append(tmp)
                #将添加完新元素的排列纳入到output_new中
                output_new.append(output[j])
                #新添加的元素当前都是排在最后的，对于每个排序可以看作一个新元素放在n-1个位置+之前n-1个元素的全排列
                for k in range(len(output[j])-1):
                    line = [n for n in output[j]]
                    #将新元素加入到n-1全排列不同的位置上
                    line[len(line)-1] = line[k]
                    line[k] = tmp
                    #print(line)
                    output_new.append(line)
            output = output_new
            #print(output)
        return output
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()  # 先排序,把相同的数字放到一起
        res = []  # 保留结果 
        def dfs(nums, path, res):
            if len(nums) == 0:  # 选到头，添加到res中，这里是递归出口，可以加return也可以不加，后续一定会结束。
                res.append(path)
                #print(path)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]: continue  # 每一层选择中如果重复，则只进行一次深度搜索
                dfs(nums[0:i] + nums[i+1:], path + [nums[i]], res)
                
        dfs(nums, [], res)
        return res
def main():
    sol=Solution()
    nums=[1,1,2,3]
    print(sol.permuteUnique(nums))

if __name__ == '__main__':
    main()