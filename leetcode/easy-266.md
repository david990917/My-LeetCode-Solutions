---
title: easy-266
tags:
  - LeetCode
description: ''
urlname: easy-266
date: 2020-03-24 12:35:19
---

# 题目

[回文排列](https://leetcode-cn.com/problems/palindrome-permutation/)

给定一个字符串，判断该字符串中是否可以通过重新排列组合，形成一个回文字符串。

示例 1：

```
输入: "code"
输出: false
```


示例 2：

```
输入: "aab"
输出: true
```


示例 3：

```
输入: "carerac"
输出: true
```



# 解题思路 √

### Python

1. 重点是排列组合

```python
#判断回文代码
if len(s)<=1:return True
    return s[0]==s[-1] and self.canPermutePalindrome(s[1:-1])
```


```python
#真实的代码
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        hashmap={}
        for char in s:
            if char in hashmap:hashmap[char]+=1
            else:hashmap[char]=1
        odd=0
        for char in hashmap:
            if hashmap[char]%2==1:
                odd+=1
        return odd<=1
```



### C++

```cpp

```

---



# 整理与总结

1. 

