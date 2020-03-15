---
title: easy-594
tags:
  - LeetCode
description: '最长和谐子序列'
urlname: easy-594
date: 2020-03-11 16:25:26
---

# 题目

https://leetcode-cn.com/problems/longest-harmonious-subsequence/

> 和谐数组是指一个数组里元素的最大值和最小值之间的差别正好是1。
>
> 现在，给定一个整数数组，你需要在所有可能的子序列中找到最长的和谐子序列的长度。
>
> 示例 1:
>
> 输入: [1,3,2,2,5,2,3,7]
> 输出: 5
> 原因: 最长的和谐数组是：[3,2,2,2,3].
> 说明: 输入的数组长度最大不超过20,000.

# 解题思路 √

### Python

1. 滑动窗口

```python
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums=sorted(nums)
        slow,maxLength=0,0
        for fast in range(len(nums)):
            while nums[fast]-nums[slow]>1:
                slow+=1
            if nums[fast]-nums[slow]==1:
                maxLength=max(maxLength,fast-slow+1)
        return maxLength
```

2. Hashmap


```python
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        hashmap={}
        for i in nums:
            if i in hashmap:hashmap[i]+=1
            else: hashmap[i]=1
        
        maxLength=0
        for i in hashmap:
            if i+1 in hashmap:
                maxLength=max(maxLength,hashmap[i]+hashmap[i+1])

        return maxLength
```



### C++

```cpp

```

---



# 整理与总结

1. 记录滑动窗口的模板：

   - 最短子串

     ```
     for (int j = 0; j < s.size(); j++) {
     	窗口右端扩展，加进s[j], 更新条件
     	while(满足条件) {
     		和当前最优比较并保存
     		窗口左端移除s[i]，更新条件，i++
     	}
     }
     ```

   - 最长子串

     ```python
     for (int j = 0; j < s.size(); j++) {
     	窗口右端扩展，加进s[j], 更新条件
     	while(不满足条件) {
     		窗口左端移除s[i]，更新条件，然后i++
     	}
     	此时重新满足条件，和最优比较并记录
     }
     ```

     
