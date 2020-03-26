---
title: medium-946
tags:
  - LeetCode
description: ''
urlname: medium-946
date: 2020-03-26 21:34:30
---

# 题目

[验证栈序列](https://leetcode-cn.com/problems/validate-stack-sequences/)

给定 pushed 和 popped 两个序列，每个序列中的 值都不重复，只有当它们可能是在最初空栈上进行的推入 push 和弹出 pop 操作序列的结果时，返回 true；否则，返回 false 。

 示例 1：

```
输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
输出：true
解释：我们可以按以下顺序执行：
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
```


示例 2：

```
输入：pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
输出：false
解释：1 不能在 2 之前弹出。
```



# 解题思路 √

### Python

1. 栈的辅助

```python
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        idx=0
        for x in pushed:
            stack.append(x)
            while stack and idx<len(popped) and stack[-1]==popped[idx]:
                stack.pop()
                idx+=1
        return not stack
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

