---
title: interview-68
tags:
  - LeetCode
description: ''
urlname: interview-68
date: 2020-04-05 22:51:02
---

# 题目

[二叉搜索树的最近公共祖先](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/)





# 解题思路 √

### Python

1. 

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val>root.val and q.val>root.val:return self.lowestCommonAncestor(root.right,p,q)
        if p.val<root.val and q.val<root.val:return self.lowestCommonAncestor(root.left,p,q)
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

