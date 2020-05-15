| [English](README_EN.md) | 简体中文 |

# [476. 数字的补数](https://leetcode-cn.com/problems/number-complement)
<p>给定一个正整数，输出它的补数。补数是对该数的二进制表示取反。</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> 5
<strong>输出:</strong> 2
<strong>解释:</strong> 5 的二进制表示为 101（没有前导零位），其补数为 010。所以你需要输出 2 。
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> 1
<strong>输出:</strong> 0
<strong>解释:</strong> 1 的二进制表示为 1（没有前导零位），其补数为 0。所以你需要输出 0 。
</pre>

<p>&nbsp;</p>

<p><strong>注意:</strong></p>

<ol>
	<li>给定的整数保证在 32 位带符号整数的范围内。</li>
	<li>你可以假定二进制数不包含前导零位。</li>
	<li>本题与 1009 <a href="https://leetcode-cn.com/problems/complement-of-base-10-integer/">https://leetcode-cn.com/problems/complement-of-base-10-integer/</a> 相同</li>
</ol>

**标签:**  [位运算](https://leetcode-cn.com/tag/bit-manipulation) 
# 解题思路 √

### Python

1. 原码 + 补码 -> 把所有的 1 占满

```python
class Solution:
    def findComplement(self, num: int) -> int:
        tmp=2
        while num>=tmp:
            tmp<<=1
        return tmp-1 - num
```


```python

```

### C++

```cpp

```

---



# 整理与总结

1. 实际上是对 `0/1/2` 进行特殊判断了，确定的 tmp 的值