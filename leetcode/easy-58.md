---
title: easy-58
tags:
  - LeetCode
description: ''
urlname: easy-58
date: 2020-03-24 13:31:37
---

# 题目

[最后一个单词的长度](https://leetcode-cn.com/problems/length-of-last-word/)

给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指仅由字母组成、不包含任何空格字符的 最大子字符串。 

示例:

```
输入: "Hello World"
输出: 5
```



# 解题思路 √

### Python

1. 注意"a "的最后一个单词是a

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        print(len(s))
        if len(s)==0 or s[-1]==' ':return 0
        s=s.split()
        return len(s[-1])
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

