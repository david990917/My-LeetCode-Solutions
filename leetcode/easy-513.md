---
title: easy-513
tags:
  - LeetCode
description: '找树左下角的值'
urlname: easy-513
date: 2020-03-19 19:58:03
---

# 题目

https://leetcode-cn.com/problems/find-bottom-left-tree-value/

给定一个二叉树，在树的最后一行找到最左边的值。

**示例 1:**

```
输入:

    2
   / \
  1   3

输出:
1
```

 

**示例 2:**

```
输入:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

输出:
7
```

 

**注意:** 您可以假设树（即给定的根节点）不为 **NULL**。

# 解题思路 √

### Python

1. 层次遍历

```python
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        currHeight,result=-1,0
        deq=[(root,0)]
        while deq:
            node,height=deq.pop(0)
            if height>currHeight:
                result=node.val
                currHeight=height
            if node.left:deq.append((node.left,height+1))
            if node.right:deq.append((node.right,height+1))
        return result
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

