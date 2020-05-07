class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, (len(s) - 1)
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

if __name__ == "__main__":
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))






    """
            The isalnum() method checks whether the string consists of alphanumeric characters.

            Time Complexity = O(n)
            Space Complexity = O(1)


            Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
            Note: For the purpose of this problem, we define empty string as valid palindrome.

            Example:
            Input: "A man, a plan, a canal: Panama"
            Output: true
    """
