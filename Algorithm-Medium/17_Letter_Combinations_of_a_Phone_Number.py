class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []

        digit_map = {
            0:"0",
            1:"1",
            2:"abc",
            3:"def",
            4:"ghi",
            5:"jkl",
            6:"mno",
            7:"pqrs",
            8:"tuv",
            9:"wxyz"
        }

        result = [""]
        for u in digits:
            tmp_list = []
            for ch in digit_map[int(u)]:
                for str in result:
                    tmp_list.append(str + ch)
            result = tmp_list
        return result


"""
    * now leetcode change the graph distribution, may check weeks later.
    Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

    A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

    Example:

    Input: "23"
    Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

    Note:

    Although the above answer is in lexicographical order, your answer could be in any order you want.
"""
