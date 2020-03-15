---
title: medium-3
tags:
  - LeetCode
description: ''
urlname: medium-3
date: 2020-03-09 11:30:55
---

# 题目

https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

> 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
>
> 示例 1:
>
> 输入: "abcabcbb"
> 输出: 3 
> 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
> 示例 2:
>
> 输入: "bbbbb"
> 输出: 1
> 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
> 示例 3:
>
> 输入: "pwwkew"
> 输出: 3
> 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
>      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。



# 解题思路 √

### Python

1. 使用滑动窗口

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap=set()
        left,currLength,maxLength=0,0,0
        for i in range(len(s)):
            currLength+=1
            while s[i] in hashmap:
                hashmap.remove(s[left])
                left+=1
                currLength-=1
            hashmap.add(s[i])
            maxLength=max(maxLength,currLength)
        return maxLength
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. Python中使用字典和集合：

   - Dict
     - key  in  dict

   - set()
     - 不存储元素的具体的值
     - set.add()
     - set.remove()
     - key in set

