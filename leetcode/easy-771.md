---
title: easy-771
tags:
  - LeetCode
description: 'Jewels and Stones'
urlname: easy-771
date: 2019-09-09 11:25:00
---

# 题目

https://leetcode.com/problems/jewels-and-stones/

You're given strings `J` representing the types of stones that are jewels, and `S` representing the stones you have.  Each character in `S` is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in `J` are guaranteed distinct, and all characters in `J` and `S` are letters. Letters are case sensitive, so `"a"` is considered a different type of stone from `"A"`.

**Example 1:**

```
Input: J = "aA", S = "aAAbbbb"
Output: 3
```

**Example 2:**

```
Input: J = "z", S = "ZZ"
Output: 0
```

**Note:**

- `S` and `J` will consist of letters and have length at most 50.
- The characters in `J` are distinct.

# 解题思路 √

暴力方法直接查找

# Python

```python
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        lenth=len(S)
        count=0
        for i in J:
            for j in range(lenth):
                if S[j]==i:
                    count+=1
        return count
```



# 整理与总结

1. 

