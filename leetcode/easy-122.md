---
title: easy-122
tags:
  - LeetCode
description: 'Best Time to Buy and Sell Stock II'
urlname: easy-122
date: 2019-08-31 16:12:53
---

# 题目

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

Say you have an array for which the *i*th element is the price of a given stock on day *i*.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

**Note:** You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

**Example 1:**

```
Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
```

**Example 2:**

```
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
```

**Example 3:**

```
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
```

# 解题思路 √

由于我们是想获取到最大的利润，我们的策略应该是低点买入，高点卖出。

由于题目对于交易次数没有限制，因此只要能够赚钱的机会我们都不应该放过。

> 如下图，我们只需要求出加粗部分的总和即可

用图表示的话就是这样：

[![122.best-time-to-buy-and-sell-stock-ii](easy-122/122.best-time-to-buy-and-sell-stock-ii.png)](https://github.com/azl397985856/leetcode/blob/master/assets/problems/122.best-time-to-buy-and-sell-stock-ii.png)

## 关键点解析

- 这类题只要你在心中（或者别的地方）画出上面这种图就很容易解决

# Python

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:        
        gains=[max(prices[i]-prices[i-1],0) for i in range(1,len(prices))] 
        return sum(gains)
```

同样的，速度能更快一点。

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        gains=[prices[i]-prices[i-1]  for i in range(1,len(prices)) if prices[i]> prices[i-1]]
        return sum(gains)
```

# 整理与总结

1. 只要后一天价格比前一天高，就有利可图
