---
title: easy-543
tags:
  - LeetCode
description: ''
urlname: easy-543
date: 2020-03-10 13:11:23
---

# 题目

> 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。
>
> 示例 :
> 给定二叉树
>
>           1
>          / \
>         2   3
>        / \     
>       4   5    
> 返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
>
> 注意：两结点之间的路径长度是以它们之间边的数目表示。
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/diameter-of-binary-tree
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 解题思路 √

### Python

1. 利用树的深度来进行操作。

```python
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans=0
        def depth(node):
            if not node:return 0
            L=depth(node.left)
            R=depth(node.right)
            self.ans=max(self.ans,L+R)
            return 1+max(L,R)
        
        depth(root)
        return self.ans
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

