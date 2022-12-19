"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.
"""

class Solution(object):
    def canConstruct(self, s, t):
        ss = set(s)
        st = set(t)

        if len(ss) != len

        for l in ss:
            if s.count(l) == t.count(l):
                pass
            else:
                return False
        return True


    