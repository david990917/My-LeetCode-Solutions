---
title: easy-168
tags:
  - LeetCode
description: 'Excel表列名称'
urlname: easy-168
date: 2020-03-15 18:15:42
---

# 题目

https://leetcode-cn.com/problems/excel-sheet-column-title/

给定一个正整数，返回它在 Excel 表中相对应的列名称。

例如，

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
**示例 1:**

```
输入: 1
输出: "A"
```

**示例 2:**

```
输入: 28
输出: "AB"
```

**示例 3:**

```
输入: 701
输出: "ZY"
```



# 解题思路 √

### Python

1. 需要借位

   对于正常的进制转换来说2进制中的`2=10b`已经进位了。

   但是对于`26=Z`来说并没有进位呢。

```python
class Solution:
    def convertToTitle(self, n: int) -> str:
        result=''
        while n>0:
            n,y=divmod(n,26)
            if y==0:
                n,y=n-1,26
            result=chr(y+ord('A')-1)+result
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

