| [English](README_EN.md) | 简体中文 |

# [189. 旋转数组](https://leetcode-cn.com/problems/rotate-array)
<p>给定一个数组，将数组中的元素向右移动&nbsp;<em>k&nbsp;</em>个位置，其中&nbsp;<em>k&nbsp;</em>是非负数。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> <code>[1,2,3,4,5,6,7]</code> 和 <em>k</em> = 3
<strong>输出:</strong> <code>[5,6,7,1,2,3,4]</code>
<strong>解释:</strong>
向右旋转 1 步: <code>[7,1,2,3,4,5,6]</code>
向右旋转 2 步: <code>[6,7,1,2,3,4,5]
</code>向右旋转 3 步: <code>[5,6,7,1,2,3,4]</code>
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> <code>[-1,-100,3,99]</code> 和 <em>k</em> = 2
<strong>输出:</strong> [3,99,-1,-100]
<strong>解释:</strong> 
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]</pre>

<p><strong>说明:</strong></p>

<ul>
	<li>尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。</li>
	<li>要求使用空间复杂度为&nbsp;O(1) 的&nbsp;<strong>原地&nbsp;</strong>算法。</li>
</ul>

**标签:**  [数组](https://leetcode-cn.com/tag/array) 
 ### 相似题目
- 中等:	[旋转链表](https://leetcode-cn.com/problems/rotate-list) 
- 中等:	[翻转字符串里的单词 II](https://leetcode-cn.com/problems/reverse-words-in-a-string-ii) 

# 解题思路 √

### Python

1. 最直白的方法

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        length=len(nums)
        nums[:]=nums[length-k:]+nums[:length-k]
```


```python

```

### C++

```cpp

```

---



# 整理与总结

1. 