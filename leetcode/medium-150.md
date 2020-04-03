---
title: medium-150
tags:
  - LeetCode
description: ''
urlname: medium-150
date: 2020-04-03 10:29:47
---

# 题目

[逆波兰表达式求值](https://leetcode-cn.com/problems/evaluate-reverse-polish-notation) 

根据逆波兰表示法，求表达式的值。

有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

说明：

整数除法只保留整数部分。
给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
示例 1：

```
输入: ["2", "1", "+", "3", "*"]
输出: 9
解释: ((2 + 1) * 3) = 9
```


示例 2：

```
输入: ["4", "13", "5", "/", "+"]
输出: 6
解释: (4 + (13 / 5)) = 6
```


示例 3：

```
输入: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
输出: 22
解释: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
```



# 解题思路 √

### Python

1. 使用栈，需要注意的是除法 `-6//12=-1`

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operations=['+','-','*','/']
        for element in tokens:
            if element in operations:
                op2=stack.pop()
                op1=stack.pop()
                if element=='+':stack.append(op1+op2)
                elif element=='-':stack.append(op1-op2)
                elif element=='*':stack.append(op1*op2)
                elif element=='/':stack.append(int(op1/op2))
            else:
                stack.append(int(element))
        
        return stack[-1]
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

