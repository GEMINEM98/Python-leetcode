
# https://leetcode-cn.com/problems/goal-parser-interpretation/

class Solution:
    def interpret(self, command: str) -> str:
        flag=""
        res=""
        for i in range(len(command)):
            flag+=command[i]
            if flag=="G":
                res+="G"
            elif flag=="()":
                res+="o"
            elif flag=="(al)":
                res+="al"
            else: continue
            flag=""
        return res
