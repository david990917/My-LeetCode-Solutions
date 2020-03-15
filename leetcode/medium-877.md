---
title: medium-877
tags:
  - LeetCode
description: 'Stone Game'
urlname: medium-877
date: 2019-09-30 06:15:58
---

# 题目

https://leetcode.com/problems/stone-game/

Alex and Lee play a game with piles of stones.  There are an even number of piles **arranged in a row**, and each pile has a positive integer number of stones `piles[i]`.

The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alex and Lee play optimally, return `True` if and only if Alex wins the game.

 

**Example 1:**

```
Input: [5,3,4,5]
Output: true
Explanation: 
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.
```

 

**Note:**

1. `2 <= piles.length <= 500`
2. `piles.length` is even.
3. `1 <= piles[i] <= 500`
4. `sum(piles)` is odd.

# 解题思路 √

### 1. 分析法

我们可以知道 Alex 可以选择一直拿奇数/偶数，lee因而必须一直拿偶数/奇数堆。这种情况下，Alex 只需要判断奇数堆偶数堆谁大就可以了。

### 2. 动态规划

# Python



```python
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
```

动态规划

```python
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n=len(piles)
        dp=piles[:]
        for d in range(1,n):
            for i in range(n-d):
                dp[i]=max(piles[i]-dp[i+1],piles[i+d]-dp[i])
        return dp[0]>0        
```



# C++

```cpp

```



# 整理与总结

1. 

