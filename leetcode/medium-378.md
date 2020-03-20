---
title: medium-378
tags:
  - LeetCode
description: '有序矩阵中第K小的元素'
urlname: medium-378
date: 2020-03-20 21:44:14
---

# 题目

https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/

给定一个 *n x n* 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第k小的元素。
请注意，它是排序后的第k小元素，而不是第k个元素。

**示例:**

```
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

返回 13。
```

**说明:**
你可以假设 k 的值永远是有效的, 1 ≤ k ≤ n2 。

# 解题思路 √

### Python

1. Python自带的小顶堆

```python
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix:return False
        if not matrix[0]:return False
        n=len(matrix)
        import heapq
        heap=[]

        for i in range(n):
            for j in range(n):
                heapq.heappush(heap,matrix[i][j])
        
        for i in range(k):
            result=heapq.heappop(heap)
        return result
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. #### [有序矩阵中第K小的元素](https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/)

