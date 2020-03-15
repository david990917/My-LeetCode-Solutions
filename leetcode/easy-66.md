---
title: easy-66
tags:
  - LeetCode
description: ''
urlname: easy-66
date: 2020-03-06 16:51:19
---

# 题目

https://leetcode-cn.com/problems/plus-one/

> 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
>
> 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
>
> 你可以假设除了整数 0 之外，这个整数不会以零开头。
>

# 解题思路 √

### Python

1. 直接转换的操作

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)): digits[i]=str(digits[i])
        digits = str(int(''.join(digits))+1)

        result=[]
        for i in range(len(digits)): result.append(int(digits[i]))
        return result
```

2. 正常操作：判断情况
   - 正常情况最后一位+1
   - 尾数是9，循环进位
   - 全是9，长度增加一位 `10000000`


```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length=len(digits)
        for i in range(length-1,0,-1):
            digits[i]= (digits[i]+1)%10
            if digits[i]: return digits
        
        return [1]+[0]*length
```



### C++

```cpp

```

---



# 整理与总结

1. `Python`的`for-range `对于`0`取值有点不友好，可以进一步放缩到`-1`

