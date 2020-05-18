| [English](README_EN.md) | 简体中文 |

# [152. 乘积最大子数组](https://leetcode-cn.com/problems/maximum-product-subarray)
<p>给你一个整数数组 <code>nums</code>&nbsp;，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> [2,3,-2,4]
<strong>输出:</strong> <code>6</code>
<strong>解释:</strong>&nbsp;子数组 [2,3] 有最大乘积 6。
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> [-2,0,-1]
<strong>输出:</strong> 0
<strong>解释:</strong>&nbsp;结果不能为 2, 因为 [-2,-1] 不是子数组。</pre>

**标签:**  [数组](https://leetcode-cn.com/tag/array) [动态规划](https://leetcode-cn.com/tag/dynamic-programming) 
 ### 相似题目
- 简单:	[最大子序和](https://leetcode-cn.com/problems/maximum-subarray) 
- 简单:	[打家劫舍](https://leetcode-cn.com/problems/house-robber) 
- 中等:	[除自身以外数组的乘积](https://leetcode-cn.com/problems/product-of-array-except-self) 
- 简单:	[三个数的最大乘积](https://leetcode-cn.com/problems/maximum-product-of-three-numbers) 
- 中等:	[乘积小于K的子数组](https://leetcode-cn.com/problems/subarray-product-less-than-k) 

# 解题思路 √

### Python

1. 

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix, suffix, res = 0, 0, -float('inf')
        for i in range(len(nums)):
            prefix = nums[i] if not prefix else nums[i]*prefix
            suffix = nums[-i - 1] if not suffix else nums[-i - 1]*suffix
            res = max(res, prefix, suffix)
        return res
```


```python

```

### C++

```cpp

```

---



# 整理与总结

1. 