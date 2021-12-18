from collections import defaultdict

class Solution:
    def decodeString(self, s: str) -> str:
        
        helper_dict = defaultdict(int)
        
        stack = []
        
        for i, val in enumerate(s):
            if val == "[":
                stack.append(i)
            elif val == "]":
                helper_dict[stack.pop()] = i
                
        def helper(l, r):
            new_str = ""
            num = 0
            while l <= r:
                ch = s[l]
                
                if ch.isdigit():
                    num=num*10+int(ch)
                elif ch == "[":
                    new_str += num*helper(l+1, helper_dict[l] -1)
                    num = 0
                    l = helper_dict[l]
                else:
                    new_str += ch
                
                l+=1
                
            return new_str
        
        return helper(0, len(s)-1)
        
        
        