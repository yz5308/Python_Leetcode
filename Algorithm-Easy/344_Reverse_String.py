class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i],s[-i-1]=s[-i-1],s[i]






    """
        Time Complexity = O(n)
        Space Complexity = O(n)

        Write a function that takes a string as input and returns the string reversed.

        Example:
        Input: "A man, a plan, a canal: Panama"
        Output: "amanaP :lanac a ,nalp a ,nam A"
    """
