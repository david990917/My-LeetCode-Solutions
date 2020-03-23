---
title: easy-252
tags:
  - LeetCode
description: ''
urlname: easy-252
date: 2020-03-23 20:41:43
---

# 题目



给定一个会议时间安排的数组，每个会议时间都会包括开始和结束的时间 [[s1,e1],[s2,e2],...] (si < ei)，请你判断一个人是否能够参加这里面的全部会议。

示例 1:

```
输入: [[0,30],[5,10],[15,20]]
输出: false
```


示例 2:

```
输入: [[7,10],[2,4]]
输出: true
```



# 解题思路 √

### Python

1. 算法的题目：按照上课时间排序

```python
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals)==1:return True
        intervals=sorted(intervals,key=lambda x:x[0])
        for idx in range(1,len(intervals)):
            if intervals[idx][0]<intervals[idx-1][1]:
                return False
        return True
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

