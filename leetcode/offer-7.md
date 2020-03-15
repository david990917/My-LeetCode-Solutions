---
title: offer-7
tags:
  - LeetCode
description: '重建二叉树'
urlname: offer-7
date: 2020-03-15 09:54:46
---

# 题目

https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/

输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

**例如，给出**

```
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
```

**限制：**

0 <= 节点个数 <= 5000

# 解题思路 √

### Python

1. 经典的题目 前中序生成二叉树，使用递归

```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder: return []
        hashmap={}
        for idx,number in enumerate(inorder):hashmap[number]=idx

        def helper(preroot,left,right):
            if left>right:return
            # preroot是在前序中的下标 #idx是中序中的下标
            root=TreeNode(preorder[preroot]) 
            idx=hashmap[preorder[preroot]]
            root.left=helper(preroot+1,left,idx-1)
            root.right=helper(preroot+idx-left+1,idx+1,right)
            return root
        return helper(0,0,len(inorder)-1)
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

