---
title: medium-241
tags:
  - LeetCode
description: '为运算表达式设计优先级'
urlname: medium-241
date: 2020-03-11 17:50:14
---

# 题目

https://leetcode-cn.com/problems/different-ways-to-add-parentheses/

> 给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及 * 。
>
> 示例 1:
>
> 输入: "2-1-1"
> 输出: [0, 2]
> 解释: 
> ((2-1)-1) = 0 
> (2-(1-1)) = 2



# 解题思路 √

### Python

1. **分治法**

   对于一个形如 x op y（op 为运算符，x 和 y 为数） 的算式而言，它的结果组合取决于 x 和 y 的结果组合数，而 x 和 y 又可以写成形如 x op y 的算式。

   因此，该问题的子问题就是 `x op y` 中的 `x` 和 `y`：**以运算符分隔的左右两侧算式解**。

```python
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if input.isdigit():
            return [int(input)]

        result=[]
        for i, char in enumerate(input):
            if char in ['+', '-', '*']:
                # Divide and Conquer
                left=self.diffWaysToCompute(input[:i])
                right=self.diffWaysToCompute(input[i+1:])
                # Combine         
                for x in left:
                    for y in right:
                        if char=='+':result.append(x+y)
                        elif char=='-':result.append(x-y)
                        elif char=='*':result.append(x*y)
        return result
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. **分治算法三步走**
   1. 分解：按运算符分成左右两部分，分别求解
   2. 解决：实现一个递归函数，输入算式，返回算式解
   3. 合并：根据运算符合并左右两部分的解，得出最终解
