'''
import sys
n = list(map(int,sys.stdin.readline().split()))
stones = list(map(int, sys.stdin.readline().split()))
dp = []
for i in range(n[0]):
    dp.append(100000000000000)
    
dp[0] = 0
dp[1] = abs(stones[1] - stones[0])

if n[1] > n[0]:
    n[1] = n[0]

if n[0] != 2:
    for x in range(2, n[0]):
        rock = 1000000000000000
        for y in range(n[1], 0, -1):
            if (x - y) >= 0 and rock > (abs(stones[x] - stones[x- y]) + dp[x - y]):
                rock = (abs(stones[x] - stones[x - y]) + dp[x - y])
        dp[x] = rock
    print(dp[n[0] - 1])

else:
    print(dp[1])
'''
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int c = s.nextInt();
        int[] h = new int[n];
        for (int i = 0; i<n; i++){
            h[i]=s.nextInt();
        }
        int[] cost = new int[n];
        cost[0]=0;
        for(int i = 1; i<n; i++){
            int min = Integer.MAX_VALUE;
            for(int j = c; j>0;j--){
                if(i-j>=0)
                    min = Math.min(cost[i-j]+Math.abs(h[i]-h[i-j]),min);
            }
            cost[i]=min;
        }
        System.out.println(cost[n-1]);
    }
}
