| [English](README_EN.md) | 简体中文 |

# [121. 买卖股票的最佳时机](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock)
<p>给定一个数组，它的第&nbsp;<em>i</em> 个元素是一支给定股票第 <em>i</em> 天的价格。</p>

<p>如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。</p>

<p>注意：你不能在买入股票前卖出股票。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> [7,1,5,3,6,4]
<strong>输出:</strong> 5
<strong>解释: </strong>在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> [7,6,4,3,1]
<strong>输出:</strong> 0
<strong>解释: </strong>在这种情况下, 没有交易完成, 所以最大利润为 0。
</pre>

**标签:**  [数组](https://leetcode-cn.com/tag/array) [动态规划](https://leetcode-cn.com/tag/dynamic-programming) 
 ### 相似题目
- 简单:	[最大子序和](https://leetcode-cn.com/problems/maximum-subarray) 
- 简单:	[买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii) 
- 困难:	[买卖股票的最佳时机 III](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii) 
- 困难:	[买卖股票的最佳时机 IV](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv) 
- 中等:	[最佳买卖股票时机含冷冻期](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown) 

# 解题思路 √

### Python

1. 正常思路：

   找到最小的值，然后找到之后的最大值（最大利润）。

   怎么判断？就是使用 if 条件语句的先后来判断

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:return 0

        minPrice=float('inf')
        maxProfit=0

        for price in prices:
            if price<minPrice:minPrice=price
            elif maxProfit<price-minPrice:maxProfit=price-minPrice
        return maxProfit
```

2. 动态规划


```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:return 0
        minPrice,maxProfit=prices[0],0
        for i in range(1,len(prices)):
            minPrice=min(minPrice,prices[i])
            maxProfit=max(maxProfit,prices[i]-minPrice)
        return maxProfit
```

### C++

```cpp

```

---



# 整理与总结

1. 