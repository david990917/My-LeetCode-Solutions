| [English](README_EN.md) | 简体中文 |

# [面试题 05.07. 配对交换](https://leetcode-cn.com/problems/exchange-lcci)
<p>配对交换。编写程序，交换某个整数的奇数位和偶数位，尽量使用较少的指令（也就是说，位0与位1交换，位2与位3交换，以此类推）。</p>

<p> <strong>示例1:</strong></p>

<pre>
<strong> 输入</strong>：num = 2（或者0b10）
<strong> 输出</strong> 1 (或者 0b01)
</pre>

<p> <strong>示例2:</strong></p>

<pre>
<strong> 输入</strong>：num = 3
<strong> 输出</strong>：3
</pre>

<p> <strong>提示:</strong></p>

<ol>
<li><code>num</code>的范围在[0, 2^30 - 1]之间，不会发生整数溢出。</li>
</ol>

**标签:**  [位运算](https://leetcode-cn.com/tag/bit-manipulation) 
# 解题思路 √

### Python

1. 使用 `Mask` 来提取 奇数和偶数 bit

```python
class Solution:
    def exchangeBits(self, num: int) -> int:
        oddMask,evenMask=0x55555555,0xaaaaaaaa
        return (num&oddMask)<<1 | (num&evenMask)>>1
```


```python

```

### C++

```cpp

```

---



# 整理与总结

1. 使用 `Mask` 来提取 奇数和偶数 bit - `oddMask,evenMask=0x55555555,0xaaaaaaaa`

2. 同时需要注意 `移位操作` 优先级更高，所以内部需要加括号

   