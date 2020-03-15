---
title: medium-338
tags:
  - LeetCode
description: 'Counting Bits'
urlname: medium-338
date: 2019-09-30 05:48:22
---

# 题目

https://leetcode.com/problems/counting-bits/

Given a non negative integer number **num**. For every numbers **i** in the range **0 ≤ i ≤ num** calculate the number of 1's in their binary representation and return them as an array.

**Example 1:**

```
Input: 2
Output: [0,1,1]
```

**Example 2:**

```
Input: 5
Output: [0,1,1,2,1,2]
```

**Follow up:**

- It is very easy to come up with a solution with run time **O(n\*sizeof(integer))**. But can you do it in linear time **O(n)** /possibly in a single pass?
- Space complexity should be **O(n)**.
- Can you do it like a boss? Do it without using any builtin function like **__builtin_popcount** in c++ or in any other language.

# 解题思路 √

两种思路：

### 1. 动态规划

`res[i>>1]+(i&1)`

### 2. 指数划分

原来的序列+1 



# Python

动态规划

```python
class Solution:
    def countBits(self, num: int) -> List[int]:
        res=[0]
        for i in range(1,num+1):
            res.append(res[i>>1]+(i&1))
        return res
```

指数划分

[为了好理解，使用的是 tmp, comp。实际上不用这么复杂, exp就够了，但是计算效率会下降]

```python
class Solution:
    def countBits(self, num: int) -> List[int]:
        exp=0
        comp,tmp=2**exp,0
        res=[0]
        for i in range(1,num+1):
            if i==comp:
                res.append(1)
                exp+=1
                tmp,comp=comp,2*comp
            elif i<comp:
                res.append(res[i-tmp]+1)
        return res
        
```



# C++

```cpp

```



# 整理与总结

1. 

