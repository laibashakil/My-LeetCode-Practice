class Solution:
    def repeatedCharacter(self, s: str) -> str:
        myset = set()
        for x in s:
            if x in myset:
                return x
            myset.add(x)