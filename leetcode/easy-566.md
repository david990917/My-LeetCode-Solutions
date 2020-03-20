---
title: easy-566
tags:
  - LeetCode
description: '重塑矩阵'
urlname: easy-566
date: 2020-03-20 21:20:11
---

# 题目

https://leetcode-cn.com/problems/reshape-the-matrix/

在MATLAB中，有一个非常有用的函数 `reshape`，它可以将一个矩阵重塑为另一个大小不同的新矩阵，但保留其原始数据。

给出一个由二维数组表示的矩阵，以及两个正整数`r`和`c`，分别表示想要的重构的矩阵的行数和列数。

重构后的矩阵需要将原始矩阵的所有元素以相同的**行遍历顺序**填充。

如果具有给定参数的`reshape`操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。

**示例 1:**

```
输入: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
输出: 
[[1,2,3,4]]
解释:
行遍历nums的结果是 [1,2,3,4]。新的矩阵是 1 * 4 矩阵, 用之前的元素值一行一行填充新矩阵。
```

**示例 2:**

```
输入: 
nums = 
[[1,2],
 [3,4]]
r = 2, c = 4
输出: 
[[1,2],
 [3,4]]
解释:
没有办法将 2 * 2 矩阵转化为 2 * 4 矩阵。 所以输出原矩阵。
```

**注意：**

1. 给定矩阵的宽和高范围在 [1, 100]。
2. 给定的 r 和 c 都是正数。



# 解题思路 √

### Python

1. 一种是利用我自己的计算index的方法 

```python
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if not nums:return []
        if not nums[0]:return []

        m,n=len(nums),len(nums[0])
        if r*c!=m*n:return nums
        result=[]
        for row in range(r):
            curr=[]
            for col in range(c):
                row_raw,col_raw=divmod(row*c+col,n)
                curr.append(nums[row_raw][col_raw])
            result.append(curr)
        return result
```

2. 也可以使用index自己增加的方法


```python
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if not nums:return []
        if not nums[0]:return []

        m,n=len(nums),len(nums[0])
        if r*c!=m*n:return nums
        result=[]
        index=0
        for row in range(r):
            curr=[]
            for col in range(c):
                row_raw,col_raw=divmod(index,n)
                curr.append(nums[row_raw][col_raw])
                index+=1
            result.append(curr)
        return result
```



### C++

```cpp

```

---



# 整理与总结

1. 

