# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Time Complexity: O(n), Space Complexity: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1: # Can't close parentheses with only one
            return False
        
        # Use a stack because the last parenthesis we open must be the first one we close
        stack = [s[0]] # Get first item
        for i in range(1,len(s)):
            if  s[i] == '{' or s[i] == '(' or s[i] == '[': # Push opening parenthesis to the stack
                stack.append(s[i])
            else: # We have a closing parenthesis
                if stack: 
                    last = stack[-1]
                    if (last == '{' and s[i] == '}') or (last == '[' and s[i] == ']') or (last == '(' and s[i] == ')'): 
                        stack.pop(-1) # If it matches our last opened parenthesis, pop it and move on
                    else:
                        return False # Wrong parenthesis, the string is invalid
                else:
                    return False # Closing before opening, invalid
        
        if stack == []: # We've opened and closed all the parenthesis, good job
            return True
        
        return False
                    