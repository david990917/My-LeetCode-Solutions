---
title: easy-101
tags:
  - LeetCode
description: '对称二叉树'
urlname: easy-101
date: 2020-03-16 13:24:09
---

# 题目

https://leetcode-cn.com/problems/symmetric-tree

给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

```
    1
   / \
  2   2
 / \ / \
3  4 4  3
```

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

```
    1
   / \
  2   2
   \   \
   3    3
```

**说明:**

如果你可以运用递归和迭代两种方法解决这个问题，会很加分

# 解题思路 √

### Python

1. 递归

   如果一个树的左子树与右子树镜像对称，那么这个树是对称的。

   ![Push an element in stack](easy-101/c84c1825698f5ccec14aa932e33113585d06baa75567a5a7839bbd0f71c9875a-file_1555698520895.png)

   因此，该问题转化为：两个树在什么情况下互为镜像？

   **如果同时满足下面的条件，两个树互为镜像：**

   1. 它们的两个根结点具有相同的值。

   2. 每个树的右子树都与另一个树的左子树镜像对称。

      ![Push an element in stack](easy-101/2c9a13df75821ba472de5267470481e48386ffa658b3f91a8acca5abfa43625d-file_1555698500306.png)

```python
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(leftT,rightT):
            if leftT and not rightT:return False
            if rightT and not leftT:return False
            if not leftT and not rightT:return True
            return (leftT.val==rightT.val) and helper(leftT.left,rightT.right) and helper(leftT.right,rightT.left)
        
        if not root:return True
        return helper(root.left,root.right)
```

2. 迭代

   利用队列进行迭代：队列中每两个连续的结点应该是相等的，而且它们的子树互为镜像。最初，队列中包含的是 `root.left` 以及 `root.right`。该算法的工作原理类似于 BFS，但存在一些关键差异。每次提取两个结点并比较它们的值。然后，将两个结点的左右子结点按相反的顺序插入队列中。当队列为空时，或者我们检测到树不对称（即从队列中取出两个不相等的连续结点）时，该算法结束。



```python
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:return True

        from collections import deque
        deq=deque()
        deq.append(root.left)
        deq.append(root.right)
        while deq:
            node1=deq.pop()
            node2=deq.pop()
            if not node1 and not node2:continue
            if node1 and not node2:return False
            if node2 and not node1:return False
            if node1.val!=node2.val:return False
            deq.append(node1.left)
            deq.append(node2.right)
            deq.append(node1.right)
            deq.append(node2.left)
        return True
```



### C++

```cpp

```

---



# 整理与总结

1. 

