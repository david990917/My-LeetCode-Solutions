| [English](README_EN.md) | 简体中文 |

# [1018. 可被 5 整除的二进制前缀](https://leetcode-cn.com/problems/binary-prefix-divisible-by-5)
<p>给定由若干&nbsp;<code>0</code>&nbsp;和&nbsp;<code>1</code>&nbsp;组成的数组 <code>A</code>。我们定义&nbsp;<code>N_i</code>：从&nbsp;<code>A[0]</code> 到&nbsp;<code>A[i]</code>&nbsp;的第 <code>i</code>&nbsp;个子数组被解释为一个二进制数（从最高有效位到最低有效位）。</p>

<p>返回布尔值列表&nbsp;<code>answer</code>，只有当&nbsp;<code>N_i</code>&nbsp;可以被 <code>5</code>&nbsp;整除时，答案&nbsp;<code>answer[i]</code> 为&nbsp;<code>true</code>，否则为 <code>false</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[0,1,1]
<strong>输出：</strong>[true,false,false]
<strong>解释：</strong>
输入数字为 0, 01, 011；也就是十进制中的 0, 1, 3 。只有第一个数可以被 5 整除，因此 answer[0] 为真。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[1,1,1]
<strong>输出：</strong>[false,false,false]
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>[0,1,1,1,1,1]
<strong>输出：</strong>[true,false,false,false,true,false]
</pre>

<p><strong>示例&nbsp;4：</strong></p>

<pre><strong>输入：</strong>[1,1,1,0,1]
<strong>输出：</strong>[false,false,false,false,false]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 30000</code></li>
	<li><code>A[i]</code> 为&nbsp;<code>0</code>&nbsp;或&nbsp;<code>1</code></li>
</ol>

**标签:**  [数组](https://leetcode-cn.com/tag/array) 
# 解题思路 √

### Python

1. 按照题目意思翻译成代码即可

   我使用二进制的添加位数是乘法的方法快速计算。

   或许可以通过只保留模数更加简便计算，避免溢出。

```python
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        result=[]
        number=0
        length=len(A)
        
        for i in range(length):
            number=number*2+A[i]
            result.append(True if number%5==0 else False)
        return result
```


```python

```

### C++

```cpp

```

---



# 整理与总结

1. 