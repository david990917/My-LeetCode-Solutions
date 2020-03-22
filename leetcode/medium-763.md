---
title: medium-763
tags:
  - LeetCode
description: 'Partition Labels'
urlname: medium-763
date: 2019-09-25 16:29:04
---

# 题目

[划分字母区间](https://leetcode-cn.com/problems/partition-labels/)

字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。返回一个表示每个字符串片段的长度的列表。

示例 1:

```
输入: S = "ababcbacadefegdehijhklij"
输出: [9,7,8]
解释:
划分结果为 "ababcbaca", "defegde", "hijhklij"。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
```


注意:

- S的长度在[1, 500]之间。
- S只包含小写字母'a'到'z'。

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
        hashmap={}
        for idx,char in enumerate(S):hashmap[char]=idx
        
        result,start,end=[],0,0
        for idx,char in enumerate(S):
            if hashmap[char]>end:
                end=hashmap[char]
            if idx==end:
                result.append(end-start+1)
                start=end+1
        return result
```



# 整理与总结

1. Hashmap - > Dict
2. 注意if逻辑的先后执行！
3. 注意逻辑的判断点（当前扫描位置 i）

