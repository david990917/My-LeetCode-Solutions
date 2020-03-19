---
title: easy-836
tags:
  - LeetCode
description: '矩形重叠'
urlname: easy-836
date: 2020-03-18 21:32:13
---

# 题目

https://leetcode-cn.com/problems/rectangle-overlap/

矩形以列表 `[x1, y1, x2, y2]` 的形式表示，其中 `(x1, y1)` 为左下角的坐标，`(x2, y2)` 是右上角的坐标。

如果相交的面积为正，则称两矩形重叠。需要明确的是，只在角或边接触的两个矩形不构成重叠。

给出两个矩形，判断它们是否重叠并返回结果。

 

**示例 1：**

```
输入：rec1 = [0,0,2,2], rec2 = [1,1,3,3]
输出：true
```

**示例 2：**

```
输入：rec1 = [0,0,1,1], rec2 = [1,0,2,1]
输出：false
```

 

**提示：**

1. 两个矩形 `rec1` 和 `rec2` 都以含有四个整数的列表的形式给出。
2. 矩形中的所有坐标都处于 `-10^9` 和 `10^9` 之间。
3. `x` 轴默认指向右，`y` 轴默认指向上。
4. 你可以仅考虑矩形是正放的情况。

# 解题思路 √

### Python

1. 检查位置

```python
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        flag    =   rec1[0]>=rec2[2] or\
                    rec1[1]>=rec2[3] or\
                    rec1[2]<=rec2[0] or\
                    rec1[3]<=rec2[1]
        return not flag
```

2. 检查重叠

   如果两个矩形重叠，那么它们重叠的区域一定也是一个矩形，那么这代表了两个矩形与 x*x* 轴平行的边（水平边）投影到 x*x* 轴上时会有交集，与 y*y* 轴平行的边（竖直边）投影到 y*y* 轴上时也会有交集。因此，我们可以将问题看作一维线段是否有交集的问题。


```python
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        def intersectHelper(p1,p2,q1,q2):
            return min(p2,q2)>max(p1,q1)
        return (intersectHelper(rec1[0],rec1[2],rec2[0],rec2[2]) and 
                    intersectHelper(rec1[1],rec1[3],rec2[1],rec2[3]))
```



### C++

```cpp
class Solution {
public:
    bool isRectangleOverlap(vector<int>& rec1, vector<int>& rec2) {
        return !(rec1[2] <= rec2[0] ||   // left
                 rec1[3] <= rec2[1] ||   // bottom
                 rec1[0] >= rec2[2] ||   // right
                 rec1[1] >= rec2[3]);    // top
    }
};
```

---



# 整理与总结

1. 

