
class Solution:
    def rotateArr(self, arr, d):
        n=len(arr)
        d=d%n
        a=list(arr)
        a.reverse()
        a1=a[0:len(arr)-d]
        a1.reverse()
        a2=a[len(arr)-1:len(arr)-d-1:-1]
        arr.clear()
        arr.extend(a1)
        arr.extend(a2)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())

    while (T > 0):
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ob.rotateArr(A, D)

        for i in A:
            print(i, end=" ")

        print()

        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends