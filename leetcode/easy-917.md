---
title: easy-917
tags:
  - LeetCode
description: ''
urlname: easy-917
date: 2020-03-24 11:58:53
---

# 题目

[仅仅反转字母](https://leetcode-cn.com/problems/reverse-only-letters/)

给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。

示例 1：

```
输入："ab-cd"
输出："dc-ba"
```


示例 2：

```
输入："a-bC-dEf-ghIj"
输出："j-Ih-gfE-dCba"
```


示例 3：

```
输入："Test1ng-Leet=code-Q!"
输出："Qedo1ct-eeLg=ntse-T!"
```


提示：

- S.length <= 100
- 33 <= S[i].ASCIIcode <= 122 
- S 中不包含 \ or "



# 解题思路 √

### Python

1. 想清楚就能做出来了-基础双指针

```python
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        result=""
        length=len(S)
        right=length-1
        for left in range(length):
            if not S[left].isalpha():
                result+=S[left]
                continue
            while not S[right].isalpha():
                right-=1
            result+=S[right]
            right-=1
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

