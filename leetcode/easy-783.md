---
title: easy-783
tags:
  - LeetCode
description: ''
urlname: easy-783
date: 2020-03-21 23:19:21
---

# 题目

[二叉搜索树结点最小距离](https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/)

给定一个二叉搜索树的根结点 root，返回树中任意两节点的差的最小值。 

示例：

```
输入: root = [4,2,6,1,3,null,null]
输出: 1
解释:
注意，root是树结点对象(TreeNode object)，而不是数组。
```

给定的树 [4,2,6,1,3,null,null] 可表示为下图:

          4
        /   \
      2      6
     / \    
    1   3  

最小的差值是 1, 它是节点1和节点2的差值, 也是节点3和节点2的差值。



# 解题思路 √

### Python

1. 类似`easy-530`

```python
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.result,self.preNode=sys.maxsize,None
        def inorder(root):
            if not root:return 
            inorder(root.left)
            if self.preNode:
                self.result=min(self.result,abs(root.val-self.preNode.val))
            self.preNode=root
            inorder(root.right)
        inorder(root)
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

