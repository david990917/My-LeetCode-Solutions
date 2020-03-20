---
title: medium-287
tags:
  - LeetCode
description: '寻找重复数'
urlname: medium-287
date: 2020-03-20 22:34:42
---

# 题目

https://leetcode-cn.com/problems/find-the-duplicate-number/

给定一个包含 *n* + 1 个整数的数组 *nums*，其数字都在 1 到 *n* 之间（包括 1 和 *n*），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

**示例 1:**

```
输入: [1,3,4,2,2]
输出: 2
```

**示例 2:**

```
输入: [3,1,3,4,2]
输出: 3
```

**说明：**

1. **不能**更改原数组（假设数组是只读的）。
2. 只能使用额外的 *O*(1) 的空间。
3. 时间复杂度小于 *O*(*n*2) 。
4. 数组中只有一个重复的数字，但它可能不止重复出现一次。

# 解题思路 √

### Python

1. 把nums想象成一根绳子，重复的值会在连接到前面的点（形成一些环），假设有一个环。环的入口为m（所求），周长为c, 快指针在绳上走2n步，慢指针走n步相遇了。快指针多走的n步是在环里转圈，且刚好转够整数圈，所以n%c=0, 这时候慢指针在环里走了 n-m 步，新建find指针从0开始走，走到环口为m步，而慢针刚好走了n-m+m=n步，环周长的整数倍（慢针进环是在结合点，转够整数圈一定还在结合点，也就是重复值）

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
            
        find = 0
        while True:
            find = nums[find]
            slow = nums[slow]
            if find == slow:
                return find
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. [寻找重复数](https://leetcode-cn.com/problems/find-the-duplicate-number/)

