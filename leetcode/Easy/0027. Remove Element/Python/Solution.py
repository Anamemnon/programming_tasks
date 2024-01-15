from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        >>> Solution().removeElement([0,1,2,2,3,0,4,2], val = 2)
        5
        """
        p1 = 0
        p2 = len(nums) - 1
        k = 0
        while p1 <= p2:
            if nums[p1] != val:
                p1 += 1
                k += 1
            else:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p2 -= 1

        return k


if __name__ == '__main__':
    import doctest
    doctest.testmod()

