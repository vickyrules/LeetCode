# class Solution:
#     def isPowerOfFour(self, n: int) -> bool:
#         return n > 0 and log(n, 4).is_integer()
    
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and not(n & (n - 1)) and n & 1431655765 == n