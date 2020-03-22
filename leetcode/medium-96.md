---
title: medium-96
tags:
  - LeetCode
description: ''
urlname: medium-96
date: 2020-03-22 08:45:37
---

# 题目

[不同的二叉搜索树](https://leetcode-cn.com/problems/unique-binary-search-trees/)

给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

```
输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```

# 解题思路 √

算法

问题是计算不同二叉搜索树的个数。为此，我们可以定义两个函数：

- G(n): 长度为n的序列的不同二叉搜索树个数。


- F(i, n): 以i为根的不同二叉搜索树个数($1 \leq i \leq n$)。


可见，

G(n)是我们解决问题需要的函数。

稍后我们将看到，G(n)可以从 F(i, n)得到，而 F(i, n) 又会递归的依赖于 G(n)。

首先，根据上一节中的思路，不同的二叉搜索树的总数 G(n)，是对遍历所有 i (1 <= i <= n) 的 F(i, n)之和。换而言之：

$G(n) = \sum_{i=1}^{n} F(i, n) \qquad \qquad$ (1)


特别的，对于边界情况，当序列长度为 1 （只有根）或为 0 （空树）时，只有一种情况。亦即：

$G(0) = 1, \qquad G(1) = 1$


给定序列 1 ... n，我们选出数字 i 作为根，则对于根 i 的不同二叉搜索树数量 F(i, n)，是左右子树个数的笛卡尔积，如下图所示:



举例而言，F(3, 7)，以 3 为根的不同二叉搜索树个数。为了以 3 为根从序列 [1, 2, 3, 4, 5, 6, 7] 构建二叉搜索树，我们需要从左子序列 [1, 2] 构建左子树，从右子序列 [4, 5, 6, 7] 构建右子树，然后将它们组合(即笛卡尔积)。

巧妙之处在于，我们可以将 [1,2] 构建不同左子树的数量表示为 G(2) 从 [4, 5, 6, 7]` 构建不同右子树的数量表示为 G(4)。这是由于 G(n)G(n) 和序列的内容无关，只和序列的长度有关。于是，$F(3,7) = G(2) \cdot G(4) $。 概括而言，我们可以得到以下公式：

$F(i, n) = G(i-1) \cdot G(n-i) \qquad \qquad$ (2)

将公式 (1)，(2) 结合，可以得到 G(n)的递归表达公式：

$G(n) = \sum_{i=1}^{n}G(i-1) \cdot G(n-i) \qquad \qquad $(3)

为了计算函数结果，我们从小到大计算，因为 `G(n)` 的值依赖于 `G(0)…G(n−1)`。



### Python

1. 动态规划

```python
class Solution:
    def numTrees(self, n: int) -> int:
        if n<=2:return n
        result=[0 for i in range(n+1)]
        result[0],result[1]=1,1
        for idx in range(2,n+1):
            for i in range(1,idx+1):
                result[idx]+=result[i-1]*result[idx-i]
        return result[-1]
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

