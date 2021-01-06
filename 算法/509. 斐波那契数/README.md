| [English](README_EN.md) | 简体中文 |

# [509. 斐波那契数](https://leetcode-cn.com/problems/fibonacci-number)
<p><strong>斐波那契数</strong>，通常用&nbsp;<code>F(n)</code> 表示，形成的序列称为<strong>斐波那契数列</strong>。该数列由&nbsp;<code>0</code> 和 <code>1</code> 开始，后面的每一项数字都是前面两项数字的和。也就是：</p>

<pre>F(0) = 0,&nbsp; &nbsp;F(1)&nbsp;= 1
F(N) = F(N - 1) + F(N - 2), 其中 N &gt; 1.
</pre>

<p>给定&nbsp;<code>N</code>，计算&nbsp;<code>F(N)</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>2
<strong>输出：</strong>1
<strong>解释：</strong>F(2) = F(1) + F(0) = 1 + 0 = 1.
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>3
<strong>输出：</strong>2
<strong>解释：</strong>F(3) = F(2) + F(1) = 1 + 1 = 2.
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>4
<strong>输出：</strong>3
<strong>解释：</strong>F(4) = F(3) + F(2) = 2 + 1 = 3.
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>0 &le; <code>N</code> &le; 30</li>
</ul>

**标签:**  [数组](https://leetcode-cn.com/tag/array) 
 ### 相似题目
- 简单:	[爬楼梯](https://leetcode-cn.com/problems/climbing-stairs) 
- 中等:	[将数组拆分成斐波那契序列](https://leetcode-cn.com/problems/split-array-into-fibonacci-sequence) 
- 中等:	[最长的斐波那契子序列的长度](https://leetcode-cn.com/problems/length-of-longest-fibonacci-subsequence) 

# 解题思路 √

### Python

1. 使用 `a,b`的形式可以减少存储使用的空间

```python
class Solution:
    def fib(self, n: int) -> int:
        if n==0:return 0
        a,b=0,1
        for i in range(n-1):
            a,b=b,a+b
        return b
```


```python

```

### C++

```cpp

```

---



# 整理与总结

1. 迭代次数：
   1. `for i in range(n)` 里面是几就执行几次