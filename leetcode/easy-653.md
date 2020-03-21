---
title: easy-653
tags:
  - LeetCode
description: ''
urlname: easy-653
date: 2020-03-21 22:51:27
---

# 题目

[两数之和 IV - 输入 BST](https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst/)

给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

案例 1:

```
输入: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

输出: True
```


案例 2:

```
输入: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

输出: False
```





# 解题思路 √

### Python

1. 转换成数组

```python
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        self.nums=[]
        def inorder(root):
            if not root:return
            inorder(root.left)
            self.nums.append(root.val)
            inorder(root.right)
        
        inorder(root)
        hashset=set()
        for idx,number in enumerate(self.nums):
            if k-number in hashset:return True
            if number not in hashset:hashset.add(number)
        return False
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

