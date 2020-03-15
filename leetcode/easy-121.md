---
title: easy-121
tags:
  - LeetCode
description: 'Best Time to Buy and Sell Stock'
urlname: easy-131
date: 2019-08-31 15:44:21
---

# 题目

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

Say you have an array for which the *i*th element is the price of a given stock on day *i*.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

**Example 1:**

```
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
```

**Example 2:**

```
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
```

# 解题思路 √

### 正常思路

找到最小的值，然后找到之后的最大值（最大利润）。

怎么判断？就是使用 if 条件语句的先后来判断

### 动态规划

我就是想用动态规划，看看试一下能不能行。	

其实就是一样的，和上面的思路。都是双指针

- 最低价格
- 之后的最大利润

# Python

正常思路

```python
class Solution:
    def maxProfit(self, prices: 'List[int]') -> int:
        if not prices: return 0

        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif max_profit < price - min_price:
                max_profit = price - min_price
        return max_profit
```

动态规划

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        
        minPrice=prices[0]
        maxProfit=0
        for i in range(1,len(prices)):
            minPrice=min(minPrice,prices[i])
            maxProfit=max(maxProfit,prices[i]-minPrice)
        return maxProfit
```

# C++

```c++
class Solution {
public:
	int maxProfit(vector<int>& prices) {
		if (prices.empty()) { return 0; }
		int p = prices[0];
		int maxp = 0;
		for (int i = 1; i < prices.size(); i++) {
			p = min(p, prices[i]);
			maxp = max(maxp, prices[i] - p);
		}
		return maxp;
	}
};
```



# 整理与总结

1. 注意原来给定的变量名
2. 注意对空变量输入的判断
3. CPP来之不易的正确：
   - 其实就是将Python翻译成C++，注意语法
   - 注意库的使用

