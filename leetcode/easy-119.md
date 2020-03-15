---
title: easy-119
tags:
  - LeetCode
description: ''
urlname: easy-119
date: 2020-03-06 21:29:40
---

# 题目

https://leetcode-cn.com/problems/pascals-triangle-ii/

> 给定一个非负索引 *k*，其中 *k* ≤ 33，返回杨辉三角的第 *k* 行。
>
> ![img](easy-119/PascalTriangleAnimated2.gif)



# 解题思路 √

### Python

1. 运算

```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res=[0]*(rowIndex+1)
        for i in range(rowIndex+1):
            res[i]=1
            for j in range(i-1,0,-1):
                res[j]+=res[j-1]
        return res
```

2. 如果要$O(n)$，那么必然是动态规划。

   $C_m^{n} = C_m^{n-1} * (m-n+1) / n$

   - `n=idx`
   - `m=rowIndex`


```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:return [1]
        result=[1]*(rowIndex+1)
        for idx in range(rowIndex+1):
            if idx==0:result[idx]=1
            elif idx==1:result[idx]=rowIndex
            elif idx<=(rowIndex//2):
                result[idx]=result[idx-1]*(rowIndex-idx+1)//idx
            else:
                result[idx]=result[rowIndex-idx]
        return result
```



### C++

```cpp

```

---



# 整理与总结

1. 静下心来，不要怕

