---
title: easy-392
tags:
  - LeetCode
description: 'Is Subsequence'
urlname: easy-392
date: 2019-09-29 18:49:09
---

# 题目

https://leetcode-cn.com/problems/is-subsequence/

> 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
>
> 你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。
>
> 字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。



> 后续挑战 :
>
> 如果有大量输入的 S，称作S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？
>



# 解题思路 √



# Python

啥也没用的朴实方法

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        length=len(s)
        match_count=0
        for j in t:
            if match_count==length:return True
            if j==s[match_count]: match_count+=1
        return match_count==length
```



# 整理与总结

1. 

