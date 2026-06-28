class Solution:
    def filterOccupiedIntervals(self, nums: List[List[int]], freeStart: int, freeEnd: int) -> List[List[int]]:
        nums.sort()
        res = []
        p_x, p_y = nums[0]
        for c_x, c_y in nums[1:]:
            if c_x <= p_y + 1:
                p_y = max(p_y, c_y)
            else:
                res.append([p_x, p_y])
                p_x, p_y = c_x, c_y
        if not res or [p_x, p_y] != res[-1]:
            res.append([p_x, p_y])
        #print(res)
        ans = []
        for x, y in res:
            if freeStart <= x and y <= freeEnd:
                continue
            if y < freeStart or x > freeEnd:
                ans.append([x, y])
            elif x < freeStart and freeEnd < y:
                ans.append([x, freeStart - 1])
                ans.append([freeEnd + 1, y])
            else:
                if x < freeStart:
                    ans.append([x, freeStart - 1])
                else:
                    ans.append([freeEnd + 1, y])
        return ans
            