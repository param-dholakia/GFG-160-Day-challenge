//{ Driver Code Starts
// Initial Template for Java.
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // Reading number of test cases (t)
        int t = Integer.parseInt(br.readLine().trim());

        while (t-- > 0) {
            // Read the line of integers (prices)
            String arr[] = br.readLine().split(" ");
            int prices[] = new int[arr.length];

            for (int i = 0; i < arr.length; i++) {
                prices[i] = Integer.parseInt(arr[i]);
            }

            // Create an instance of the Solution class
            Solution ob = new Solution();

            // Call the stockBuyAndSell method
            int res = ob.maximumProfit(prices);

            // Print the result
            System.out.println(res);

            // Print the "~" symbol to match the original output
            System.out.println("~");
        }
    }
}
// } Driver Code Ends


// User function Template for Java
class Solution {
    public int maximumProfit(int prices[]) {
        // code here
        int profit=0;
        int flag=0;
        //   flag=0-->stock buyed   &   flag=1-->stock sold
        int n=prices.length;
        int i;
        for(i=0;i<n-1;i++)
        {
            if( (prices[i] < prices[i+1]) && (flag==0))
            {
                profit-=prices[i];
                flag=1;
            }
                
            else if( (prices[i] > prices[i+1]) && (flag==1) )
            {
                profit+=prices[i];
                flag=0;
            }
        }
        if(flag==1)
        {
            profit+=prices[n-1];
            flag=0;
        }
        return profit;
    }
}