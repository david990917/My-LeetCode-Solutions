---
title: medium-406
tags:
  - LeetCode
description: ''
urlname: medium-406
date: 2020-03-22 11:11:35
---

# 题目

[根据身高重建队列](https://leetcode-cn.com/problems/queue-reconstruction-by-height/)

假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。 编写一个算法来重建这个队列。

注意：
总人数少于1100人。

示例

```
输入:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

输出:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
```



# 解题思路 √

![](medium-406/0b13fafcb2dad898575a95702d0f76d58eb973f84112c011c0771c282eb1cc6c-file_1577091496469.jfif)

从最简单的情况下思考，当队列中所有人的 `(h,k)` 都是相同的高度 `h`，只有 `k` 不同时，解决方案很简单：每个人在队列的索引 `index = k`。

![在这里插入图片描述](medium-406/f1d3fb50fbff21d238b5373f026e5d8145b03a71b80cd469d2f1003db9f31fca-file_1577091496518.jfif)

即使不是所有人都是同一高度，这个策略也是可行的。因为个子矮的人相对于个子高的人是 “看不见” 的，所以可以先安排个子高的人。

![在这里插入图片描述](medium-406/3910bd5f1730547364d6a44e04de732819ebcb5c1ab3ce116ffff648d6e9e122-file_1577091496595.jfif)

**算法：**

- 排序：
  - 按高度降序排列。
  - 在同一高度的人中，按 `k` 值的升序排列。
- 逐个地把它们放在输出队列中，索引等于它们的 `k` 值。
- 返回输出队列

### Python

1. 直接进行操作

```python
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: (-x[0], x[1]))
        output = []
        for p in people:
            output.insert(p[1], p)
        return output
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

