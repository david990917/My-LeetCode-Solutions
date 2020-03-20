---
title: easy-257
tags:
  - LeetCode
description: '二叉树的所有路径'
urlname: easy-257
date: 2020-03-20 15:55:42
---

# 题目

https://leetcode-cn.com/problems/binary-tree-paths/

给定一个二叉树，返回所有从根节点到叶子节点的路径。

**说明:** 叶子节点是指没有子节点的节点。

**示例:**

```
输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
```



# 解题思路 √

### Python

1. 

```python
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:return []
        results=[]

        def backTrack(node,tempPath):
            if not node:return 
            part=str(node.val)
            if len(tempPath)!=0:part='->'+part
            if not node.left and not node.right:
                results.append(tempPath+part)
            backTrack(node.left,tempPath+part)
            backTrack(node.right,tempPath+part)
            

        backTrack(root,'')
        return results
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 二叉树的所有路径

