class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        addends = []
        addendsSum = 0

        def backtrack(i, *, processed = set()):
            nonlocal addendsSum
            if addendsSum == target:
                result.append(addends.copy())
                return
            elif addendsSum > target:
                return
            elif i >= len(candidates):
                return
            
            if candidates[i] not in processed:
                addendsSum += candidates[i]
                addends.append(candidates[i])

                backtrack(i + 1, processed=processed)

                addendsSum -= candidates[i]
                addends.pop()

            copy_ = processed.copy()
            copy_.add(candidates[i])
            backtrack(i + 1, processed=copy_)


        backtrack(0)
        return result