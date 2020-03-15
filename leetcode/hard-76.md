---
title: hard-76
tags:
  - LeetCode
description: '最小覆盖子串'
urlname: hard-76
date: 2020-03-09 11:52:25
---

# 题目

> 给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。
>
> 示例：
>
> 输入: S = "ADOBECODEBANC", T = "ABC"
> 输出: "BANC"
> 说明：
>
> 如果 S 中不存这样的子串，则返回空字符串 ""。
> 如果 S 中存在这样的子串，我们保证它是唯一的答案。
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/minimum-window-substring
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 解题思路 √

### Python

1. 滑动窗口
   - 初始的时候都指向第一个元素
   - right右滑增大，直到满足条件
   - left右滑减小间隔，直到最小情况/不满足条件
   - right继续右滑

现在的难点就在于如何计数了——两个哈希表



```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hashmap={}
        hashmap_t=collections.Counter(t)
        required=len(hashmap_t)
        
        start,left,right,counter,minCoverLength=0,0,0,0,sys.maxsize
        while right<len(s):
            target=s[right]
            if target in hashmap_t:
                if target in hashmap:hashmap[target]+=1
                else:hashmap[target]=1
                if hashmap[target]==hashmap_t[target]:counter+=1

            while counter==required:
                if right-left+1<minCoverLength:
                    start=left
                    minCoverLength=right-left+1
                target=s[left]
                if target in hashmap:
                    hashmap[s[left]]-=1
                    if hashmap[s[left]]<hashmap_t[s[left]]:
                        counter-=1
                left+=1
            right+=1
        if minCoverLength==sys.maxsize:return ""
        return s[start:start+minCoverLength]
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 整理滑动窗口

   ```python
   int left = 0, right = 0;
   
   while (right < s.size()) {
       window.add(s[right]);
           
       while (valid) {
           window.remove(s[left]);
           left++;
       }
       right++;
   }
   ```

2. 最大值