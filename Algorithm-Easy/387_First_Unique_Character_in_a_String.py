from collections import defaultdict

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup = dict()
        for i in s:
            if i in lookup:
                lookup[i] += 1
            else:
                lookup[i] = 1

        for i in s:
            if lookup[i] == 1:
                return s.index(i)

        return -1

class Solution2:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        lookup=Counter(s)

        for i,c in enumerate(s):
            if lookup[c]==1:
                return i

        return -1


    """
        Time Complexity = O(n)
        Space Complexity = O(n)

        Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

        Example:
        s = "leetcode"
        return 0.

        s = "loveleetcode",
        return 2.
    """
