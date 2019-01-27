'''
给定一组唯一的单词， 找出所有不同 的索引对(i, j)，
使得列表中的两个单词， words[i] + words[j] ，可拼接成回文串。
'''


class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        wmap={}
        for i,word in enumerate(words):
            wmap[word[::-1]]=i
        res=[]
        for i, word in enumerate(words):
            #将长度设成len(word)+1 就可以包含空值的情况了
            for x in range(len(word)+1):
                l,r=word[:x],word[x:]
                #print(l,r)
                if l in wmap and wmap[l]!=i and r==r[::-1]:
                    res.append([wmap[l],i])
                if x>0 and r in wmap and wmap[r]!=i and l==l[::-1]:
                    res.append([i,wmap[r]])
        return res


    def palindromePairs2(self, words):
        '''
        1176ms 时间复杂度 O(k*n^2) 空间 O(k*n)
        '''
        wmap = {w: i for i, w in enumerate(words)}
        def isPalindrome(word):
            _len = len(word)
            for x in range(int(_len / 2)):
                if word[x] != word[_len - x - 1]:
                    return False
            return True

        res = set()
        for idx, word in enumerate(words):
            if word and isPalindrome(word) and "" in wmap:
                nidx = wmap[""]
                res.add((idx, nidx))
                res.add((nidx, idx))

            rword = word[::-1]
            if word and rword in wmap:
                nidx = wmap[rword]
                if idx != nidx:
                    res.add((idx, nidx))
                    res.add((nidx, idx))
            '''
            ll--left Palidrome
            lls--word
            slls--rright--s
            ss
            sssll
            lls{[ss]sll}--需要lls
            '''
            for x in range(1, len(word)):
                left, right = word[:x], word[x:]
                rleft, rright = left[::-1], right[::-1]

                if isPalindrome(left) and rright in wmap:
                    res.add((wmap[rright], idx))
                if isPalindrome(right) and rleft in wmap:
                    res.add((idx, wmap[rleft]))
        return list(res)
    '''
    超出时间限制
    '''
    #     res = []
    #     for i in range(len(words)-1):
    #         for j in range(i+1, len(words)):
    #             if self.Pairs(words[i], words[j]):
    #                 res.append([i, j])
    #             if self.Pairs(words[j], words[i]):
    #                 res.append([j, i])
    #     return res
    #
    # def Pairs(self, w1, w2):
    #     w = w1 + w2
    #     wordlist=[]
    #     for i in w:
    #         wordlist.append(i)
    #     j = len(wordlist)
    #     k = int(0.5 * j)
    #     if j>1 and j%2==0:
    #         return wordlist[:k] == wordlist[k:][::-1]
    #     elif j > 1 and j % 2 ==1:
    #         return wordlist[:k] == wordlist[k+1:][::-1]
    #     elif j==0:
    #         return True
    #     return False

def main():
    sol=Solution()

    #words=["bat", "tab", "cat"]
    words=["abcd","dcba","lls","s","sssll"]
    res=sol.palindromePairs(words)
    print(res)

if __name__ == '__main__':
    main()