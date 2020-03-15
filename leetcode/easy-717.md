---
title: easy-717
tags:
  - LeetCode
description: ''
urlname: easy-717
date: 2020-03-05 23:01:50
---

# 题目

https://leetcode-cn.com/problems/1-bit-and-2-bit-characters/

> 有两种特殊字符。第一种字符可以用一比特0来表示。第二种字符可以用两比特(10 或 11)来表示。
>
> 现给一个由若干比特组成的字符串。问最后一个字符是否必定为一个一比特字符。给定的字符串总是由0结束。
>
> 示例 1:
>
> > 输入: 
> > bits = [1, 0, 0]
> > 输出: True
> > 解释: 
> > 唯一的编码方式是一个两比特字符和一个一比特字符。所以最后一个字符是一比特字符。
>
> 示例 2:
>
> > 输入: 
> > bits = [1, 1, 1, 0]
> > 输出: False
> >
> > 解释: 
> >
> > 唯一的编码方式是两比特字符和两比特字符。所以最后一个字符不是一比特字符。
>
> 注意:
>
> > 1 <= len(bits) <= 1000.
> > bits[i] 总是0 或 1.



# 解题思路 √

## 线性扫描

当前位是1，移动两位；当前位是0，移动一位。

如果是双字符做结尾，移动完成之后就会超出去；检测到单字符的时候，可以提前检测结尾 `length-1`

***复杂度分析***

- 时间复杂度：$O(n)$
- 空间复杂度：$O(1)$

## 贪心算法

`0` & `10` & `11`

那么 $\mathrm{bits}$ 数组中出现的所有 `0` 都表示一个字符的结束位置（无论其为一比特还是两比特）。因此最后一位是否为一比特字符，只和他左侧出现的连续的 1 的个数（即它与倒数第二个 0 出现的位置之间的 1 的个数，如果 $\mathrm{bits}$ 数组中只有 1 个 0，那么就是整个数组的长度减一）有关。如果 1 的个数为偶数个，那么最后一位是一比特字符，如果 1 的个数为奇数个，那么最后一位不是一比特字符。



***复杂度分析***

- 时间复杂度：$O(n)$
- 空间复杂度：$O(1)$

# Python

线性扫描简洁代码

```python
class Solution(object):
    def isOneBitCharacter(self, bits):
        i = 0
        while i < len(bits) - 1:
            i += bits[i] + 1
        return i == len(bits) - 1
```

贪心

```python
class Solution(object):
    def isOneBitCharacter(self, bits):
        parity = bits.pop()
        while bits and bits.pop(): parity ^= 1
        return parity == 0
```



# C++

```cpp

```

---

# 官方解答建议



# 整理与总结

1. 数组位置的时候就用位置，最好不要混淆位置和个数。

2. 我的线性扫描代码就不够简洁

   ```python
   class Solution:
       def isOneBitCharacter(self, bits: List[int]) -> bool:
           if bits[-1] ==1:
               return False
   
           length=len(bits)
           i=0
           while i < length:
               if bits[i]==1:i+=2
               else:
                   if i==length-1:
                       return True
                   i+=1
   ```

   总结一下差距：

   - 还有边界条件`lenth-1`和`lenth`。差别原来就是检测和移动是否分开呀，小问题。

   - 优化的代码通常可以利用自身的结构（本题中是自身的0/1）

   - 功能分开，不要用太多`if - else`