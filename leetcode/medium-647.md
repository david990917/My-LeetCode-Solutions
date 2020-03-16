---
title: medium-647
tags:
  - LeetCode
description: '回文子串'
urlname: medium-647
date: 2020-03-16 21:28:01
---

# 题目

https://leetcode-cn.com/problems/palindromic-substrings

给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。

**示例 1:**

```
输入: "abc"
输出: 3
解释: 三个回文子串: "a", "b", "c".
```

**示例 2:**

```
输入: "aaa"
输出: 6
说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
```


注意:

输入的字符串长度不会超过1000。

# 解题思路 √

### Python

1. 回文-取中心然后扩展。需要注意奇偶就可以了。

```python
class Solution:
    count=0
    def countSubstrings(self, s: str) -> int:
        length,count=len(s),0

        def helper(s,start,end):
            count=0
            while start>=0 and end<len(s):
                if s[start]==s[end]:
                    start-=1
                    end+=1
                    count+=1
                else: break
            return count

        for i in range(length):
            count+=helper(s,i,i)
            count+=helper(s,i,i+1)
        return count

```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

