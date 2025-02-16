class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digits = {}
        for num in nums:
            n, s = num, 0
            while n >= 10:
                s += n % 10
                n //= 10
            s += n
            if s in digits:
                digits[s].append(num)
            else:
                digits[s] = [num]
        m = -1
        for num in digits.values():
            if len(num) >= 2:
                num.sort()
                s = num[-1] + num[-2]
                m = max(m, s)
        return m