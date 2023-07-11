# User function Template for python3
class Solution:

    def print2largest(self, arr, n):
        # code here
        max_ = arr[0]
        second_max = -1

        for i in arr[1:]:
            if i > max_:
                second_max = max_
                max_ = i
            elif i > second_max and i != max_:
                second_max = i
        return second_max


# {
# Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends