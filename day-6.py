class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        n=len(arr)
        n/=3
        cd1,cd2,cn1,cn2=None,None,0,0
        l=[]
        
        for i in arr:
            if i==cd1:
                cn1+=1
            elif i==cd2:
                cn2+=1
            elif cn1==0:
                cn1=1
                cd1=i
            elif cn2==0:
                cn2=1
                cd2=i
            else:
                cn1-=1
                cn2-=1
            
        cn1,cn2=0,0
        
        for i in arr:
            if i==cd1:
                cn1+=1
            elif i==cd2:
                cn2+=1

        if cn1 > n:
            l.append(cd1)
        if cn2 > n:
            l.append(cd2)
            
        l.sort()
        return l
#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.findMajority(nums)
        if not ans:
            print("[]")
        else:
            print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

# } Driver Code Ends