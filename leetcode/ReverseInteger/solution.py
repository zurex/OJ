class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        bit = []
        flag = 1 if x > 0 else -1
        x = abs(x)
        result = 0
        while x > 0:
            result = result * 10 + x % 10
            x = x / 10
        # big than 32-bit singed int
        max_val = 2 ** 31
        return result * flag if result < max_val else 0


def main():
    sol = Solution()
    print sol.reverse(321)

if __name__ == '__main__':
    main()
