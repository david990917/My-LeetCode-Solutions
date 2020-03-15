---
title: medium-159
tags:
  - LeetCode
description: '至多包含两个不同字符的最长子串'
urlname: medium-159
date: 2020-03-09 17:24:28
---

# 题目

https://leetcode-cn.com/problems/longest-substring-with-at-most-two-distinct-characters/

> 给定一个字符串 ***s\*** ，找出 **至多** 包含两个不同字符的最长子串 ***t\* 。**
>
> **示例 1:**
>
> ```
> 输入: "eceba"
> 输出: 3
> 解释: t 是 "ece"，长度为3。
> ```
>
> **示例 2:**
>
> ```
> 输入: "ccaabbb"
> 输出: 5
> 解释: t 是 "aabbb"，长度为5。
> ```



# 解题思路 √

### Python

1. 窗口滑动

```python
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        hashmap={}
        left,right,currLength,maxLength=0,0,0,0

        for right in range(len(s)):
            currLength+=1
            target=s[right]
            if target in hashmap:hashmap[target]+=1
            else:
                hashmap[target]=1
                while len(hashmap)>2:
                    hashmap[s[left]]-=1
                    if hashmap[s[left]]==0:hashmap.pop(s[left])
                    left+=1
                    currLength-=1
            maxLength=max(currLength,maxLength)                

        #print(s[left:left+currLength])
        return maxLength
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

