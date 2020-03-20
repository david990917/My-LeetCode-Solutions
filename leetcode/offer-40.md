---
title: offer-40
tags:
  - LeetCode
description: '最小的k个数'
urlname: offer-40
date: 2020-03-20 10:43:06
---

# 题目

https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/

输入整数数组 `arr` ，找出其中最小的 `k` 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

 

**示例 1：**

```
输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
```

**示例 2：**

```
输入：arr = [0,1,2,1], k = 1
输出：[0]
```

 

**限制：**

- `0 <= k <= arr.length <= 10000`
- `0 <= arr[i] <= 10000`

# 解题思路 √

### Python

1. 直接排序

```python
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        arr=sorted(arr)
        return arr[:k]
```

2. 堆 k个元素的大根堆

   Python里面的堆是小根堆，所以我们取相反数就可以了


```python
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:return []

        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if arr[i]<-hp[0]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        ans = [-x for x in hp]
        return ans
```

3. 快速排序

```python

```



### C++

```cpp

```

---



# 整理与总结

1. Python中的堆是一个小根堆

   Python默认的堆

   ```python
   # 在线性时间内将列表x转换为堆
   heapq.heapify(hp)
   # 弹出并返回堆中的最小项，保持堆不变
   heapq.heappop（堆）
   # 将值项推入堆中，保持堆不变
   heapq.heappush(hp, -arr[i])
   ```

   

