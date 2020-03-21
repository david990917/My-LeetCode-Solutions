---
title: medium-347
tags:
  - LeetCode
description: ''
urlname: medium-347
date: 2020-03-21 18:05:23
---

# 题目

[前 K 个高频元素](https://leetcode-cn.com/problems/top-k-frequent-elements/)

给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:

```
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
```


示例 2:

```
输入: nums = [1], k = 1
输出: [1]
```


说明：

你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。

# 解题思路 √

### Python

1. 应用桶排序的方法

   ![img](medium-347/ad27531bbe762c0cf408a1e80f6468800d3e4ee2d6318963276b9ed923dd2c54-file_1561712388097.jfif)

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        for idx,number in enumerate(nums):
            if number in hashmap:hashmap[number]+=1
            else:hashmap[number]=1
        
        tong=[[] for i in range(len(nums)+1)]
        for number in hashmap:
            time=hashmap[number]
            tong[time].extend([number])

        result=[]
        for idx in range(len(nums),-1,-1):
            if tong[idx]:
                for number in tong[idx]:
                    result.append(number)
                    if len(result)==k:return result
```

2. 直接用k元素的堆


```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        for idx,number in enumerate(nums):
            if number in hashmap:hashmap[number]+=1
            else:hashmap[number]=1
        
        hp,count=[],0
        for number in hashmap:
            if count<k:
                hp.append(hashmap[number])
                count+=1
                if count==k:heapq.heapify(hp)
            else:
                target=hashmap[number]
                if target>hp[0]:
                    heapq.heappop(hp)
                    heapq.heappush(hp,hashmap[number])
        
        times=hp[0]
        result=[]
        for number in hashmap:
            if hashmap[number]>=times:
                result.append(number)
        return result
```

3. Python自带

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)   
        return heapq.nlargest(k, count.keys(), key=count.get) 
```



### C++

```cpp

```

---



# 整理与总结

1. 排序算法的比较

   ![20190624173156.jpg](medium-347/cde64bf682850738153e6c76dd3f6fb32201ce3c73c23415451da1eead9eb7cb-20190624173156.jpg)

