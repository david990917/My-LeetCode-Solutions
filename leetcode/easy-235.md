---
title: easy-235
tags:
  - LeetCode
description: '二叉搜索树的最近公共祖先'
urlname: easy-235
date: 2020-03-15 17:43:54
---

# 题目

https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大**（一个节点也可以是它自己的祖先）**。”

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]

 ![img](easy-235/binarysearchtree_improved.png)

**示例 1:**

```
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6 
解释: 节点 2 和节点 8 的最近公共祖先是 6。
```


**示例 2:**

```
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
```

**说明:**

所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉搜索树中。

# 解题思路 √

二叉搜索树（BST）的性质：

- 节点 N 左子树上的所有节点的值都小于等于节点 N 的值
- 节点 N 右子树上的所有节点的值都大于等于节点 N 的值
- 左子树和右子树也都是 BST

### Python

1. **递归**

   - 从根节点遍历树
   - 如果都是在右子树，右子树继续
   - 如果都是在左子树，左子树继续
   - 不成立，那么就找到了

   【大于才能是右子树，等于不行】

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:return None
        vp,vq,vr=p.val,q.val,root.val
        if vp>vr and vq>vr:return self.lowestCommonAncestor(root.right,p,q)
        if vp<vr and vq<vr:return self.lowestCommonAncestor(root.left,p,q)
        return root
```

2. 迭代 - 分割点
   - 让节点 p 和节点 q 不能在同一颗子树上的那个节点
   - 或者是节点 p 和节点 q 中的一个 - 其中一个节点是另一个节点的父亲节点


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

