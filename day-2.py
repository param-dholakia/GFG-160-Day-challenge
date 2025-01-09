#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr):
    	z=len(arr)
    	cnt=0
    	
    	for i in arr:
    	    if(i==0):
    	        cnt=cnt+1
    	  
        last = 0
        for i in range(z):
            if arr[i] != 0:
                arr[last], arr[i] = arr[i], arr[last]
                last += 1


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
