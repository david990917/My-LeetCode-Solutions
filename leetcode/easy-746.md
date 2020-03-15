---
title: easy-746
tags:
  - LeetCode
description: 'Min Cost Climbing Stairs'
urlname: easy-746
date: 2019-09-29 18:27:04
---

# 题目

https://leetcode.com/problems/min-cost-climbing-stairs/	

On a staircase, the `i`-th step has some non-negative cost `cost[i]` assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

**Example 1:**

```
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
```



**Example 2:**

```
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
```



**Note:**

1. `cost` will have a length in the range `[2, 1000]`.
2. Every `cost[i]` will be an integer in the range `[0, 999]`.

# 解题思路 √

### 动态规划

从第二级阶梯开始，都是从前一级或者是前两级阶梯跳上来的，所以有动态转移方程：

```python
dp[i] = min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
```

初始情况：

```python
dp[0] = 0
dp[1] = 0
```

得嘞，齐活儿！

# Python

### 动态规划解法

```python
class Solution:
    def minCostClimbingStairs(self, cost):
        dp=[0 for i in range(len(cost)+1)]
        for i in range(2,len(cost)+1):
            dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
        return dp[len(cost)]
```



```python
class Solution:
    def minCostClimbingStairs(self, cost):
        a, b = cost[0], cost[1]
        for i in range(2, len(cost)):
            a, b = b, min(a, b) + cost[i]
        return min(a, b)
```



# 整理与总结

1. 

