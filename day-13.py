#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        #Your code here
        arr=list(set(arr))
        arr.sort()
        n=len(arr)
        while n!=0 and arr[0] < 1:
            arr.pop(0)
            n-=1
        
        k=1
        if n > 0:
            for i in range(0,len(arr)):
                if arr[i]==k:
                   k+=1
                else:
                   break
        
        return k

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.missingNumber(arr))
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends