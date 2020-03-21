---
title: medium-1038
tags:
  - LeetCode
description: ''
urlname: medium-1038
date: 2020-03-21 19:37:40
---

# 题目

[从二叉搜索树到更大和树](https://leetcode-cn.com/problems/binary-search-tree-to-greater-sum-tree/)

给出二叉 搜索 树的根节点，该二叉树的节点值各不相同，修改二叉树，使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。

提醒一下，二叉搜索树满足下列约束条件：

节点的左子树仅包含键 小于 节点键的节点。
节点的右子树仅包含键 大于 节点键的节点。
左右子树也必须是二叉搜索树。


示例：

```
输入：[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
```


提示：

树中的节点数介于 1 和 100 之间。
每个节点的值介于 0 和 100 之间。
给定的树为二叉搜索树。



# 解题思路 √

### Python

1. 递归 - 逆着中序遍历 - 就是我们的最大到最小

```python
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.sum=0
        def traver(root):
            if not root:return
            traver(root.right)
            self.sum+=root.val
            root.val=self.sum
            traver(root.left)

        traver(root)
        return root
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

