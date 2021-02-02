class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod, summ = 1, 0
        n = str(n)
        for i in n:
            prod *= int(i)
            summ += int(i)
        return(prod - summ)