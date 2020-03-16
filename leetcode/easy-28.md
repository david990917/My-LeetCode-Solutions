---
title: easy-28
tags:
  - LeetCode
description: '实现 strStr()'
urlname: easy-28
date: 2020-03-16 12:39:45
---

# 题目

https://leetcode-cn.com/problems/implement-strstr

实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

**示例 1:**

```
输入: haystack = "hello", needle = "ll"
输出: 2
```


**示例 2:**

```
输入: haystack = "aaaaa", needle = "bba"
输出: -1
```


**说明:**

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。

# 解题思路 √

### Python

1. ![fig](easy-28/match.png)

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length,L=len(haystack),len(needle)
        if L==0:return 0
        i,currL=0,0
        while i<length:
            if haystack[i]==needle[currL]:
                currL+=1
                if currL==L:return i-L+1
                i+=1
                
            else:
                i=i-currL+1
                currL=0

        return -1
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

