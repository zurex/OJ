Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


这道题主要考点就是边界条件判断
记住一点, 之前的字符串都是判断过的,所以如果有重复,就从重复的那个字符那边继续算

最好情况下算法复杂度为O(N)
此时输入序列全部重复
最坏情况下算法复杂度为O(N^2)
此时输入序列全部不重复

算法复杂度取决于最长不重复序列的长度M, 该算法是不稳定的
