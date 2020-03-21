---
title: medium-769
tags:
  - LeetCode
description: '最多能完成排序的块'
urlname: medium-769
date: 2020-03-21 10:25:54
---

# 题目

[最多能完成排序的块](https://leetcode-cn.com/problems/max-chunks-to-make-sorted/)

数组`arr`是`[0, 1, ..., arr.length - 1]`的一种排列，我们将这个数组分割成几个“块”，并将这些块分别进行排序。之后再连接起来，使得连接的结果和按升序排序后的原数组相同。

我们最多能将数组分成多少块？

**示例 1:**

```
输入: arr = [4,3,2,1,0]
输出: 1
解释:
将数组分成2块或者更多块，都无法得到所需的结果。
例如，分成 [4, 3], [2, 1, 0] 的结果是 [3, 4, 0, 1, 2]，这不是有序的数组。
```

**示例 2:**

```
输入: arr = [1,0,2,3,4]
输出: 4
解释:
我们可以把它分成两块，例如 [1, 0], [2, 3, 4]。
然而，分成 [1, 0], [2], [3], [4] 可以得到最多的块数。
```

**注意:**

- `arr` 的长度在 `[1, 10]` 之间。
- `arr[i]`是 `[0, 1, ..., arr.length - 1]`的一种排列。



# 解题思路 √

### Python

1. 分割数组，是数组排序后都有序

   不断更新我数组的最右边，使得每一小段都自洽

```python
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        if not arr:return 0
        result,right=0,arr[0]
        for i in range(len(arr)):
            right=max(right,arr[i])
            if right==i:result+=1
        return result
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

