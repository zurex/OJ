class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        length = 0
        current = ''
        for char in s:
            index = current.find(char)
            if index >= 0:
                if length > max_len:
                    max_len = length
                length -= index
                current = current[index+1:]+char
            else:
                length += 1
                current += char
        if length > max_len:
            max_len = length
        return max_len

def main():
    s = Solution()
    print s.lengthOfLongestSubstring("bpfbhmipx")

if __name__ == '__main__':
    main()