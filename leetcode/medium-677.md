---
title: medium-677
tags:
  - LeetCode
description: ''
urlname: medium-677
date: 2020-03-22 18:01:41
---

# 题目

[键值映射](https://leetcode-cn.com/problems/map-sum-pairs/)

实现一个 MapSum 类里的两个方法，insert 和 sum。

对于方法 insert，你将得到一对（字符串，整数）的键值对。字符串表示键，整数表示值。如果键已经存在，那么原来的键值对将被替代成新的键值对。

对于方法 sum，你将得到一个表示前缀的字符串，你需要返回所有以该前缀开头的键的值的总和。

示例 1:

```
输入: insert("apple", 3), 输出: Null
输入: sum("ap"), 输出: 3
输入: insert("app", 2), 输出: Null
输入: sum("ap"), 输出: 5
```



# 解题思路 √

### Python

1. 

```python
class TrieNode(dict):
    def __init__(self):
        self.val=None
    
class MapSum:
    def __init__(self):
        self.root=TrieNode()

    def insert(self, key: str, val: int) -> None:
        curr=self.root
        for char in key:
            node=curr.get(char)
            if node is None:
                node=TrieNode()
                curr[char]=node
            curr=node
        curr.val=val
            

    def sum(self, prefix: str) -> int:
        curr=self.root
        self.result=0
        for char in prefix:
            curr=curr.get(char)
            if curr is None:return 0
            
        def dfs(root):            
            if root is None:return 
            if root.val:self.result+=root.val
            for follow in root:
                curr=root[follow]                
                dfs(curr)

        dfs(curr)
        return self.result
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

