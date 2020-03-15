---
title: easy-276
tags:
  - LeetCode
description: ''
urlname: easy-276
date: 2020-03-07 15:12:47
---

# 题目

https://leetcode-cn.com/problems/paint-fence/

> 有 k 种颜色的涂料和一个包含 n 个栅栏柱的栅栏，每个栅栏柱可以用其中一种颜色进行上色。
>
> 你需要给所有栅栏柱上色，并且保证其中相邻的栅栏柱 最多连续两个 颜色相同。然后，返回所有有效涂色的方案数。
>
> 注意:
> n 和 k 均为非负的整数。



# 解题思路 √

> 前栅栏的涂色方案有两种
>
> 1. 和前一个颜色相同，此时说明前一个的栅栏的颜色应与更前面一个栅栏的颜色不同，更前一个栅栏的涂色方法有 F(n - 2) 种，前一个栅栏的涂色方式有 (k - 1) 种，所以此时情况应为 F(n - 2) * (k - 1)
> 2. 和前一个颜色不同，前一个栅栏的涂色方法有 F(n - 1) 种，当前栅栏的涂色方式有 (k - 1) 种，此时情况应为 F(n - 1) * (k - 1)
>
> 所以递推公式应为 F(n) = F(n - 2) * (k - 1) + F(n - 1) * (k - 1)

### Python

1. 动态规划计算递推公式。

```python
class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n==0 or k==0:return 0
        if n==1:return k
        a,b=k*k,k
        for i in range(2,n):
            a,b=(b+a)*(k-1),a
        return a
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 找情况，然后不断传递我们要研究的量。
2. 对于`range`的下标，总是有点迷惑：我们明确`a/b`的含义，然后我们画出一个长格，然后计算就好啦。

