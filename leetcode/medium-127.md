---
title: medium-127
tags:
  - LeetCode
description: '单词接龙'
urlname: medium-127
date: 2020-03-19 21:59:35
---

# 题目

https://leetcode-cn.com/problems/word-ladder/

给定两个单词（*beginWord* 和 *endWord*）和一个字典，找到从 *beginWord* 到 *endWord* 的最短转换序列的长度。转换需遵循如下规则：

1. 每次转换只能改变一个字母。
2. 转换过程中的中间单词必须是字典中的单词。

**说明:**

- 如果不存在这样的转换序列，返回 0。
- 所有单词具有相同的长度。
- 所有单词只由小写字母组成。
- 字典中不存在重复的单词。
- 你可以假设 *beginWord* 和 *endWord* 是非空的，且二者不相同。

**示例 1:**

```
输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出: 5

解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
     返回它的长度 5。
```

**示例 2:**

```
输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: 0

解释: endWord "cog" 不在字典中，所以无法进行转换。
```

# 解题思路 √

### Python

1. 我的方法超时了

```python
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:return 0
        from collections import deque
        deq=deque()
        visited=set()

        def changeT(word,curr):
            if len(word)!=len(curr):return False
            count=0
            for i in range(len(word)):
                if word[i]!=curr[i]:
                    count+=1
                    if count==2:return False
            return count==1

        deq.append((beginWord,0))
        while deq:
            curr,step=deq.popleft()
            targets=[word for word in wordList if changeT(word,curr)]
            for target in targets:
                if target==endWord:
                    return step+2 # step+1 变换的次数；再加1是序列的长度
                if target not in visited:
                    deq.append((target,step+1))
                    visited.add(target)
        return 0

```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

