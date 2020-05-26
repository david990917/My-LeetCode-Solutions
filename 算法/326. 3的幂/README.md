| [English](README_EN.md) | 简体中文 |

# [326. 3的幂](https://leetcode-cn.com/problems/power-of-three)
<p>给定一个整数，写一个函数来判断它是否是 3&nbsp;的幂次方。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> 27
<strong>输出:</strong> true
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> 0
<strong>输出:</strong> false</pre>

<p><strong>示例 3:</strong></p>

<pre><strong>输入:</strong> 9
<strong>输出:</strong> true</pre>

<p><strong>示例 4:</strong></p>

<pre><strong>输入:</strong> 45
<strong>输出:</strong> false</pre>

<p><strong>进阶：</strong><br>
你能不使用循环或者递归来完成本题吗？</p>

**标签:**  [数学](https://leetcode-cn.com/tag/math) 
 ### 相似题目
- 简单:	[2的幂](https://leetcode-cn.com/problems/power-of-two) 
- 简单:	[4的幂](https://leetcode-cn.com/problems/power-of-four) 

# 解题思路 √

### Python

1. 简单的循环计算

```python
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:return False
        while n:
            if n==1:return True
            if n%3!=0:return False
            n//=3
```

2. 简单的打表


```python
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return True if(n>0 and 1162261467 % n == 0)else False
```

### C++

```cpp

```

---



# 整理与总结

1. 