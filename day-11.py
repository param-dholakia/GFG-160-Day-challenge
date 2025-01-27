class Solution:
    def maxProduct(self, arr):
        n = len(arr)
        
        # Initialize the maxProd, minProd, and result with the first element of the array
        maxProd = arr[0]
        minProd = arr[0]
        result = arr[0]
        
        # Traverse the array starting from the second element
        for i in range(1, n):
            # If the current element is negative, swap maxProd and minProd
            if arr[i] < 0:
                maxProd, minProd = minProd, maxProd
            
            # Update maxProd and minProd
            maxProd = max(arr[i], maxProd * arr[i])
            minProd = min(arr[i], minProd * arr[i])
            
            # Update the result with the maximum of result and maxProd
            result = max(result, maxProd)
        
        return result
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends