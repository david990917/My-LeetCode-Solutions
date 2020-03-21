---
title: easy-766
tags:
  - LeetCode
description: '托普利茨矩阵'
urlname: easy-766
date: 2020-03-21 09:27:48
---

# 题目

https://leetcode-cn.com/problems/toeplitz-matrix/

如果一个矩阵的每一方向由左上到右下的对角线上具有相同元素，那么这个矩阵是*托普利茨矩阵*。

给定一个 `M x N` 的矩阵，当且仅当它是*托普利茨矩阵*时返回 `True`。

**示例 1:**

```
输入: 
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
输出: True
解释:
在上述矩阵中, 其对角线为:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]"。
各条对角线上的所有元素均相同, 因此答案是True。
```

**示例 2:**

```
输入:
matrix = [
  [1,2],
  [2,2]
]
输出: False
解释: 
对角线"[1, 2]"上的元素不同。
```

**说明:**

1.  `matrix` 是一个包含整数的二维数组。
2. `matrix` 的行数和列数均在 `[1, 20]`范围内。
3. `matrix[i][j]` 包含的整数在 `[0, 99]`范围内。

**进阶:**

1. 如果矩阵存储在磁盘上，并且磁盘内存是有限的，因此一次最多只能将一行矩阵加载到内存中，该怎么办？
2. 如果矩阵太大以至于只能一次将部分行加载到内存中，该怎么办？



# 解题思路 √

### Python

1. 对角线法 - 什么时候是对角线？是r-c相同的时候

```python
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if not matrix:return False
        if not matrix[0]:return False
        hashmap={}
        for r,row in enumerate(matrix):
            for c,val in enumerate(matrix[r]):
                if r-c in hashmap:
                    if val!=hashmap[r-c]:
                        return False
                else:hashmap[r-c]=val
        return True
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. [托普利茨矩阵](https://leetcode-cn.com/problems/toeplitz-matrix/)

