class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people_dict = {}
        for p in people:
            h,k = p[0], p[1]
            people_dict.setdefault(h, [])
            people_dict[h].append(k)

        result = []

        for h in sorted(people_dict.keys(), reverse=True):
            people_dict[h].sort()
            for k in people_dict[h]:
                result.insert(k, [h,k])

        return result

# [[7,0]] (insert [7,0] at index 0)
# [[7,0],[7,1]] (insert [7,1] at index 1)
# [[7,0],[6,1],[7,1]] (insert [6,1] at index 1)
# [[5,0],[7,0],[6,1],[7,1]] (insert [5,0] at index 0)
# [[5,0],[7,0],[5,2],[6,1],[7,1]] (insert [5,2] at index 2)
# [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] (insert [4,4] at index 4)







    """
        Time Complexity = O(n^2)
        Space Complexity = O(n)

        Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

        Note:
        The number of people is less than 1,100.


        Example

        Input:
        [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

        Output:
        [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

    """
