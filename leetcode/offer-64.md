---
title: offer-64
tags:
  - LeetCode
description: ''
urlname: offer-64
date: 2020-02-29 11:06:57
---

# 题目

https://leetcode-cn.com/problems/qiu-12n-lcof/

> 求 `1+2+...+n` ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
>
> **示例 1：**
>
> ```
> 输入: n = 3
> 输出: 6
> ```
>
> **示例 2：**
>
> ```
> 输入: n = 9
> 输出: 45
> ```

# 解题思路 √

1. Python中包含很多直接简单的求和方式。

2. **骤死性评估：**左侧的表达式为假时整个表达式后续将不再进行评估。-> CPP

   用这种方式可以实现递归的操作。题目要求中我们不能使用 `if` ，那对于我们来说 常见的递归出口就不能直接写了。用这种方式就实现了一行中代表递归语句。

   

   

# Python

```python
class Solution:
    def sumNums(self, n: int) -> int:
        return sum(range(1,n+1))
```

# C++

骤死性评估-模拟递归

```cpp
class Solution {
public:
    int sumNums(int n) {
        int res=n;
        n && (res+=sumNums(n-1));
        return res;
    }
};
```



# 整理与总结

1. 为什么要用`res=n`，因为在操作中明显是需要两个参数，并且都有进行修改。
2. 没有`if`，那就用`&&`来代替。
3. 不能用`循环`那就找`递归`。
