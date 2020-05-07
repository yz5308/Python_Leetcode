class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lookup = {}

        for i in s:
            if i not in lookup:
                lookup[i] = 1
            else:
                lookup[i]+=1

        for j in t:
            if j not in lookup:
                return False
            else:
                lookup[j]-=1

        for k in lookup:
            if lookup[k]>0:return False
        return True

if __name__ == '__main__':
    print(Solution().isAnagram('anagram','nagaram'))



    """
        Time Complexity = O(N)
        Space Complexity = O(N)

        Given two strings s and t , write a function to determine if t is an anagram of s.

        Example:
        Input: s = "anagram", t = "nagaram"
        Output: true
    """
