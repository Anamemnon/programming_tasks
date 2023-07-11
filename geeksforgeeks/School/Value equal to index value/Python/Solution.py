# User function Template for python3
class Solution:

    def valueEqualToIndex(self, arr, n):
        result = []

        for i, v in enumerate(arr, start=1):
            if v == i:
                result.append(v)

        return result


# {
# Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.valueEqualToIndex(arr, n)
        if len(ans) == 0:
            print("Not Found")
        else:
            for x in ans:
                print(x, end=" ")
            print()
        tc -= 1

# } Driver Code Ends