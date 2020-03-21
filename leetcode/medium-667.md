---
title: medium-667
tags:
  - LeetCode
description: '优美的排列 II'
urlname: medium-667
date: 2020-03-21 09:10:45
---

# 题目

https://leetcode-cn.com/problems/beautiful-arrangement-ii/

给定两个整数 `n` 和 `k`，你需要实现一个数组，这个数组包含从 `1` 到 `n` 的 `n` 个不同整数，同时满足以下条件：

① 如果这个数组是 [a1, a2, a3, ... , an] ，那么数组 [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] 中应该有且仅有 k 个不同整数；.

② 如果存在多种答案，你只需实现并返回其中任意一种.

**示例 1:**

```
输入: n = 3, k = 1
输出: [1, 2, 3]
解释: [1, 2, 3] 包含 3 个范围在 1-3 的不同整数， 并且 [1, 1] 中有且仅有 1 个不同整数 : 1
```

 

**示例 2:**

```
输入: n = 3, k = 2
输出: [1, 3, 2]
解释: [1, 3, 2] 包含 3 个范围在 1-3 的不同整数， 并且 [2, 1] 中有且仅有 2 个不同整数: 1 和 2
```

 

**提示:**

1.  `n` 和 `k` 满足条件 1 <= k < n <= 104.



# 解题思路 √

### Python

1. 前k+1个元素构建出来k个不相同的差值

   ```
   1 k+1 2 k 3 k-1 ··· k//2 k//2+1
   ```

   

```python
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        result=[]
        interval,i=k,1
        for idx in range(k+1):
            if idx%2==1:
                result.append(interval+1)
                interval-=1
            elif idx%2==0:
                result.append(i)
                i+=1
        for idx in range(k+1,n):
            result.append(idx+1)
        return result
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. [优美的排列 II](https://leetcode-cn.com/problems/beautiful-arrangement-ii/)

