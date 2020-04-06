---
title: interview-54
tags:
  - LeetCode
description: ''
urlname: interview-54
date: 2020-04-05 22:46:34
---

# 题目

[二叉搜索树的第k大节点](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/)



# 解题思路 √

### Python

1. 

```python
class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.count,self.result=0,None
        def inorder(root):
            if not root:return 
            inorder(root.right)
            self.count+=1
            if self.count==k:
                self.result=root.val
            inorder(root.left)
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

