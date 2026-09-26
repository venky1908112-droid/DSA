from collections import defaultdict
class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        res = ""
        map = defaultdict(str)
        for key, val in knowledge:
            map[key] = val
        inside = False
        for ch in s:
            if ch == "(":
                inside = True
                temp = ""
            elif ch == ")":
                inside = False
                if temp in map:
                    res += map[temp]
                else:
                    res += "?"
            elif inside:
                temp += ch
            else:
                res += ch
        return res