---
title: medium-763
tags:
  - LeetCode
description: 'Partition Labels'
urlname: medium-763
date: 2019-09-25 16:29:04
---

# 题目

https://leetcode.com/problems/partition-labels/

A string `S` of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.



**Example 1:**

```
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
```



**Note:**

1. `S` will have length in range `[1, 500]`.
2. `S` will consist of lowercase letters (`'a'` to `'z'`) only.

# 解题思路 √

我们最关心的就是每个字母最后出现的位置，然后断开它。

1. 遍历建立一个Hashmap，Python的话就是dict
2. 再次遍历，判断逻辑就是：
   - 如果当前字符在后面还出现过，那我们的end至少要到它结束才行（这个同时保证了最优，扫描过的字符我们都通过end满足了）
   - 如果恰好当前扫描位置是可以让前面的字符都结束的位置，那么输出分划长度

# Python

```python
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        dict={}
        for i in range(len(S)):
            dict[S[i]]=i
        
        
        start=end=0
        res=[]
        for i in range(len(S)):
            if dict[S[i]]>end:
                end=dict[S[i]]
            if i==end:
                res.append(end-start+1)            
                start=end+1
        return res
            
```



# 整理与总结

1. Hashmap - > Dict
2. 注意if逻辑的先后执行！
3. 注意逻辑的判断点（当前扫描位置 i）

