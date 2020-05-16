| [English](README_EN.md) | 简体中文 |

# [面试题63. 股票的最大利润](https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof)
<p>假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> [7,1,5,3,6,4]
<strong>输出:</strong> 5
<strong>解释: </strong>在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> [7,6,4,3,1]
<strong>输出:</strong> 0
<strong>解释: </strong>在这种情况下, 没有交易完成, 所以最大利润为 0。</pre>

<p>&nbsp;</p>

<p><strong>限制：</strong></p>

<p><code>0 &lt;= 数组长度 &lt;= 10^5</code></p>

<p>&nbsp;</p>

<p><strong>注意：</strong>本题与主站 121 题相同：<a href="https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/">https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/</a></p>

**标签:**  [动态规划](https://leetcode-cn.com/tag/dynamic-programming) 
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

1. 注意原来给定的变量名
2. 注意对空变量输入的判断
3. CPP来之不易的正确：
   - 其实就是将Python翻译成C++，注意语法
   - 注意库的使用