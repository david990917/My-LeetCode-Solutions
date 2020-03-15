---
title: easy-944
tags:
  - LeetCode
description: 'Delete Columns to Make Sorted'
urlname: easy-944
date: 2019-09-25 17:08:23
---

# 题目

https://leetcode.com/problems/delete-columns-to-make-sorted/

We are given an array `A` of `N` lowercase letter strings, all of the same length.

Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.

For example, if we have an array `A = ["``abcdef``","uvwxyz"]` and deletion indices `{0, 2, 3}`, then the final array after deletions is `["bef", "vyz"]`, and the remaining columns of `A` are `["b"``,"``v"]`, `["e","y"]`, and `["f","z"]`.  (Formally, the `c`-th column is `[A[0][c], A[1][c], ..., A[A.length-1][c]]`.)

Suppose we chose a set of deletion indices `D` such that after deletions, each remaining column in A is in **non-decreasing** sorted order.

Return the minimum possible value of `D.length`.

 

**Example 1:**

```
Input: ["cba","daf","ghi"]
Output: 1
Explanation: 
After choosing D = {1}, each column ["c","d","g"] and ["a","f","i"] are in non-decreasing sorted order.
If we chose D = {}, then a column ["b","a","h"] would not be in non-decreasing sorted order.
```

**Example 2:**

```
Input: ["a","b"]
Output: 0
Explanation: D = {}
```

**Example 3:**

```
Input: ["zyx","wvu","tsr"]
Output: 3
Explanation: D = {0, 1, 2}
```

 

**Note:**

1. `1 <= A.length <= 100`
2. `1 <= A[i].length <= 1000`

Accepted

# 解题思路 √

##### 简洁版思路：

zip()函数实际上可以把列打包，然后就一目了然了。

其实就是数 有几列排序情况和实际情况不符。

##### 正常版本：

看了cpp和java的解法，和python的思路差不多。

# Python

```python
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        res=[]
        for j in range(len(A[0])):
            for i in range(1,len(A)):
                if A[i][j]<A[i-1][j]:
                    print(A[i-1][j],A[i][j])
                    res.append(j)
                    break
        print(res)
        return len(res)
                
```

简洁版：

```python
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
    	return sum([list(i) != sorted(i) for i in list(zip(*A))])
```



# 整理与总结

1. 

