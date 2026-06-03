class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1count={}
        windowcount={}
        for ch in s1:
            s1count[ch]=1+s1count.get(ch,0)
        left=0
        for right in range(len(s2)):
            windowcount[s2[right]]=1+windowcount.get(s2[right],0)
            if right-left+1>len(s1):
                windowcount[s2[left]]-=1
                if windowcount[s2[left]]==0:
                    del windowcount[s2[left]]
                left+=1
            if windowcount==s1count:
                return True
        return False
