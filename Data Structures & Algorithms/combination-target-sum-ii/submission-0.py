class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(i,target,temp,ans):
            if target==0:
                ans.append(temp[:])
                return
            if i == len(candidates):
                return
            if target<0:
                return 
            for ind in range(i,len(candidates)):
                if ind>i and candidates[ind]==candidates[ind-1]:
                    continue
                temp.append(candidates[ind])
                dfs(ind+1,target-candidates[ind],temp,ans)
                temp.pop()
            
        candidates.sort()
        ans=[]
        dfs(0,target,[],ans)

        return ans        