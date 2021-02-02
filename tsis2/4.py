class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        v = []
        x = 0
        v += [x]
        for i in gain:
            v += [x + i]
            x = x + i
        mx = -999
        for i in v:
            if i > mx:
                mx = i
        return(mx)