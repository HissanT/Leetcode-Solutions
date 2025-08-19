class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        s = ''
        c = 0
        for i in range(low, high+1):
            sum1, sum2 = 0, 0
            arrF, arrE = [], []
            s = str(i)
            l = len(s)
            if l % 2 == 0:
                arrF = list(s[:l//2])
                arrE = list(s[l//2:])
                for k in range(l//2):
                    sum1 += int(arrF[k])
                    sum2 += int(arrE[k])
                if sum1 == sum2:
                    c += 1
        return c