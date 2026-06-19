
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        if dividend == divisor:
            return 1

        # determine sign
        sign = not ((dividend < 0) ^ (divisor < 0))

        # absolute values
        n = abs(dividend)
        d = abs(divisor)

        ans = 0

        while n >= d:
            count = 0

            while n >= (d << (count + 1)):
                count += 1

            ans += (1 << count)
            n -= (d << count)

        # 32-bit integer overflow handling
        if ans == (1 << 31):
            return (2**31 - 1) if sign else -(2**31)

        return ans if sign else -ans
    

obj=Solution();
print(obj.divide(100,25))