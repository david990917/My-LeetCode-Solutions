---
title: medium-279
tags:
  - LeetCode
description: ''
urlname: medium-279
date: 2020-03-19 21:18:47
---

# 题目



给定正整数 *n*，找到若干个完全平方数（比如 `1, 4, 9, 16, ...`）使得它们的和等于 *n*。你需要让组成和的完全平方数的个数最少。

**示例 1:**

```
输入: n = 12
输出: 3 
解释: 12 = 4 + 4 + 4.
```

**示例 2:**

```
输入: n = 13
输出: 2
解释: 13 = 4 + 9.
```

# 解题思路 √

### Python

1. 逐点分析

```python
class Solution:
    def numSquares(self, n: int) -> int:
        from collections import deque
        deq=deque()
        visited=set()
        
        deq.append((n,0))
        while deq:
            number,step=deq.popleft()
            targets=[number-i*i for i in range(1,int(number**0.5)+1)]
            for target in targets:
                if target==0:return step+1
                if target not in visited:
                    deq.append((target,step+1))
                    visited.add(target)
        return 0
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 层次遍历的第一道题目

   层次遍历就是BFS，可以理解成最短路径问题

   需要有一个队列 + hashtable【存储我们的visited】+ level

   

   

