---
title: easy-172
tags:
  - LeetCode
description: 'Factorial Trailing Zeroes'
urlname: easy-172
date: 2019-08-31 17:24:33
---

# 题目

[阶乘后的零](https://leetcode-cn.com/problems/factorial-trailing-zeroes/)

给定一个整数 *n*，返回 *n*! 结果尾数中零的数量。

**示例 1:**

```
输入: 3
输出: 0
解释: 3! = 6, 尾数中没有零。
```

**示例 2:**

```
输入: 5
输出: 1
解释: 5! = 120, 尾数中有 1 个零.
```

**说明:** 你算法的时间复杂度应为 *O*(log *n*) 。

# 解题思路 √

我们需要求解这n个数字相乘的结果末尾有多少个0，由于题目要求log的复杂度，因此暴力求解是不行的。

通过观察，我们发现如果想要结果末尾是0，必须是分解质因数之后，2 和 5 相乘才行，同时因数分解之后发现5的个数远小于2， 因此我们只需要求解这n数字分解质因数之后一共有多少个5即可.

[![172.factorial-trailing-zeroes-2](easy-172/172.factorial-trailing-zeroes-2.png)](https://github.com/azl397985856/leetcode/blob/master/assets/problems/172.factorial-trailing-zeroes-2.png)

如图如果n为30，那么结果应该是图中红色5的个数，即7。

[![172.factorial-trailing-zeroes-1](easy-172/172.factorial-trailing-zeroes-1.png)](https://github.com/azl397985856/leetcode/blob/master/assets/problems/172.factorial-trailing-zeroes-1.png)

我们的结果并不是直接f(n) = n / 5, 比如n为30， 25中是有两个5的。 类似，n为150，会有7个这样的数字，通过观察我们发现规律`f(n) = n/5 + n/5^2 + n/5^3 + n/5^4 + n/5^5+..`

[![172.factorial-trailing-zeroes-3](easy-172/172.factorial-trailing-zeroes-3.png)](https://github.com/azl397985856/leetcode/blob/master/assets/problems/172.factorial-trailing-zeroes-3.png)

如果可以发现上面的规律，用递归还是循环实现这个算式就显而易见了。

# Python

递归

```python
class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n // 5 == 0:
            return 0
        else:
            return n // 5 + Solution.trailingZeroes(self, n // 5)
```



# 整理与总结

1. 注意 python 的除法
2. 总结规律，0怎么产生的

