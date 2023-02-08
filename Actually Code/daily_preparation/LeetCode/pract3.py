"""Given two strings s and p, return an array of all the start indices of 
p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a
different word or phrase, typically using all the original letters exactly once.
"""


class Solution:
    def findAnagrams(self, long_string: str, find_string: str) -> list[int]:
        """
        Given two strings s and p, return an array of all the start indices of 
        p's anagrams in s. You may return the answer in any order.

        An Anagram is a word or phrase formed by rearranging the letters of a
        different word or phrase, typically using all the original letters exactly once.

        :param long_string: str
        :param find_string: str
        :return: List[int]
        """
        start_indices = []
        find_string = sorted(find_string)
        find_length = len(find_string)
        for i in range(len(long_string)):
            if i + find_length > len(long_string):
                break
            anagram = sorted(long_string[i:find_length + i])
            if find_string == anagram:
                start_indices.append(i)
        return start_indices

s = "cbaebabacd"
p = "abc"
print(Solution().findAnagrams(s, p))
