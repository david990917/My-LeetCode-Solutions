---
title: offer-34
tags:
  - LeetCode
description: ''
urlname: offer-34
date: 2020-03-26 22:50:34
---

# 题目

[二叉树中和为某一值的路径](https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof) 

输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

 

示例:

```
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1

返回:
[
   [5,4,11,2],
   [5,8,4,5]
]
```



# 解题思路 √

### Python

1. 还是很棒的

```python
class Solution:
    def pathSum(self, root: TreeNode, sumVal: int) -> List[List[int]]:
        if not root:return []
        result=[]
        
        def dfs(temp,curr,target):
            if target==curr.val:
                if not curr.left and not curr.right:
                    result.append(temp+[curr.val])
                    return
            if curr.left:
                dfs(temp+[curr.val],curr.left,target-curr.val)
            if curr.right:
                dfs(temp+[curr.val],curr.right,target-curr.val)
                
                
        dfs([],root,sumVal)
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

