
# Simple solution using stacks for both strings and comparing them at the end
# Time: O(n+m), Space: O(n+m)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s2, t2 = [], []
        
        for c in s:
            if c == '#':  # If backspace
                if s2:
                    s2.pop()
            else:
                s2.append(c)
                
        for c in t:
            if c == '#':  # If backspace
                if t2:
                    t2.pop()
            else:
                t2.append(c)
        
        
        return s2 == t2

# A two pointer solution
class Solution2(object):
    def backspaceCompare(self, s, t):
        i,j = len(s)-1, len(t)-1
        sDelete, tDelete = 0, 0
		
        # Iterate from the end of the string
        while True:
            if i<0 and j<0: # No differences
                return True
				
            checkT, checkS = True, True # Check whether we should compare characters
			
            if i >= 0:
                if s[i] == "#": # Add to the chars to be deleted count
                    sDelete, i, checkS = sDelete+1, i-1, False
                elif sDelete: # Delete the char (decrement pointer)
                    sDelete, i, checkS = sDelete-1, i-1, False
            if j >= 0: # Same as for s
                if t[j] == "#":
                    tDelete, j, checkT = tDelete+1, j-1, False
                elif tDelete:
                    tDelete, j, checkT = tDelete-1, j-1, False
                    
            if checkS and checkT: 
                if i<0 or j<0: # If strings are of unequal length
                    return False
                if s[i] != t[j]: # If chars don't match
                    return False
                i-=1
                j-=1