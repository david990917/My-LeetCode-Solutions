---
title: medium-98
tags:
  - LeetCode
description: ''
urlname: medium-98
date: 2020-03-22 08:26:17
---

# 题目

[验证二叉搜索树](https://leetcode-cn.com/problems/validate-binary-search-tree/)

给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

- 节点的左子树只包含小于当前节点的数。
- 节点的右子树只包含大于当前节点的数。
- 所有左子树和右子树自身必须也是二叉搜索树。

示例 1:

```
输入:
    2
   / \
  1   3
输出: true
```


示例 2:

```
输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
根节点的值为 5 ，但是其右子节点值为 4 。
```



# 解题思路 √

### Python

1. `isinstance(preVal,int)`这个别忘了

```python
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.preVal,self.result=None,True
        def inorder(root):
            if not root:return 
            inorder(root.left)
            if isinstance(self.preVal,int):
                if root.val<=self.preVal:
                    self.result=False
                    return
            self.preVal=root.val
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

