| [English](README_EN.md) | 简体中文 |

# [136. 只出现一次的数字](https://leetcode-cn.com/problems/single-number)
<p>给定一个<strong>非空</strong>整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。</p>

<p><strong>说明：</strong></p>

<p>你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> [2,2,1]
<strong>输出:</strong> 1
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> [4,1,2,1,2]
<strong>输出:</strong> 4</pre>

**标签:**  [位运算](https://leetcode-cn.com/tag/bit-manipulation) [哈希表](https://leetcode-cn.com/tag/hash-table) 
 ### 相似题目
- 中等:	[只出现一次的数字 II](https://leetcode-cn.com/problems/single-number-ii) 
- 中等:	[只出现一次的数字 III](https://leetcode-cn.com/problems/single-number-iii) 
- 简单:	[缺失数字](https://leetcode-cn.com/problems/missing-number) 
- 中等:	[寻找重复数](https://leetcode-cn.com/problems/find-the-duplicate-number) 
- 简单:	[找不同](https://leetcode-cn.com/problems/find-the-difference) 

# 解题思路 √

### Python

1. 位运算直接操作

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result=0
        for num in nums:
            result^=num
        return result
```

2. 使用集合


```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2*sum(set(nums))-sum(nums)
```

### C++

```cpp

```

---



# 整理与总结

1. 