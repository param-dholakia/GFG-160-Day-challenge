#User function Template for python3

#Complete this function
#Function to find maximum circular subarray sum.
def circularSubarraySum(arr):
    ##Your code here
    n=len(arr)
    ss=arr[n-1]
    
    maxS=[0]*(n+1)
    maxS[n-1]=arr[n-1]
    
    for i in range(n-2,-1,-1):
        ss+=arr[i]
        maxS[i]=max(maxS[i+1],ss)
        
    cs,ns=arr[0],arr[0]
    currsum,prefix=0,0
    
    for i in range(n):
        currsum=max(currsum+arr[i],arr[i])
        ns=max(ns,currsum)
        prefix+=arr[i]
        cs=max(cs,prefix+maxS[i+1])
        
    return max(ns,cs)
    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
import sys

if __name__ == "__main__":
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        print(circularSubarraySum(arr))

        T -= 1

# } Driver Code Ends