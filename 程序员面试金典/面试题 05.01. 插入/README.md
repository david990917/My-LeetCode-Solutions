| [English](README_EN.md) | 简体中文 |

# [面试题 05.01. 插入](https://leetcode-cn.com/problems/insert-into-bits-lcci)
<p>插入。给定两个32位的整数<code>N</code>与<code>M</code>，以及表示比特位置的<code>i</code>与<code>j</code>。编写一种方法，将<code>M</code>插入<code>N</code>，使得M从N的第j位开始，到第<code>i</code>位结束。假定从<code>j</code>位到<code>i</code>位足以容纳<code>M</code>，也即若M = 10 011，那么j和i之间至少可容纳5个位。例如，不可能出现j = 3和i = 2的情况，因为第3位和第2位之间放不下M。</p>

<p> <strong>示例1:</strong></p>

<pre>
<strong> 输入</strong>：N = 10000000000, M = 10011, i = 2, j = 6
<strong> 输出</strong>：N = 10001001100
</pre>

<p> <strong>示例2:</strong></p>

<pre>
<strong> 输入</strong>： N = 0, M = 11111, i = 0, j = 4
<strong> 输出</strong>：N = 11111
</pre>

**标签:**  [位运算](https://leetcode-cn.com/tag/bit-manipulation) 
# 解题思路 √

### Python

1. 位运算

```python
class Solution:
    def insertBits(self, N: int, M: int, i: int, j: int) -> int:
        # Step1 创建一个 j - i 位是 0 其他位都是 1 的掩码
        one = ~0
        left = one << (j + 1)
        right = (1 << i) - 1
        mask = left | right
        # Step2 将 N 的 j - i 位清零
        n = mask & N
        # Step3 将 M 移动到合适的位置
        m = M << i
        return n | m

```


```python

```

### C++

```cpp

```

---



# 整理与总结

1. 