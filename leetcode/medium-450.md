---
title: medium-450
tags:
  - LeetCode
description: ''
urlname: medium-450
date: 2020-03-22 09:24:56
---

# 题目

[删除二叉搜索树中的节点](https://leetcode-cn.com/problems/delete-node-in-a-bst/)

给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

一般来说，删除节点可分为两个步骤：

首先找到需要删除的节点；
如果找到了，删除它。
说明： 要求算法时间复杂度为 O(h)，h 为树的高度。

示例:

```
root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7
```

给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。

一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。

```
    5
   / \
  4   6
 /     \
2       7
```

另一个正确答案是 [5,2,6,null,4,null,7]。

```
    5
   / \
  2   6
   \   \
    4   7
```



# 解题思路 √

**递归**
这里有三种可能的情况：

1. 要删除的节点为叶子节点，可以直接删除。

![在这里插入图片描述](medium-450/b86c5d5866fb8b1f6a2f15f47262adf3ae68e56498c9e261a031bbb8ebc55588-file_1576477912302.jfif)

2. 要删除的节点不是叶子节点且拥有右节点，则该节点可以由该节点的后继节点进行替代，该后继节点位于右子树中较低的位置。然后可以从后继节点的位置递归向下操作以删除后继节点。

![在这里插入图片描述](medium-450/12353e5c71267aafd355319a8b881f0b9efae0680358b7ce738228151a42d3cc-file_1576477912312.jfif)

3. 要删除的节点不是叶子节点，且没有右节点但是有左节点。这意味着它的后继节点在它的上面，但是我们并不想返回。我们可以使用它的前驱节点进行替代，然后再递归的向下删除前驱节点。

![在这里插入图片描述](medium-450/2a9aa44aab7948e78e06182791e2eaaf00fb72eff054a1f4612030a047dde59a-file_1576477912315.jfif)

**算法：**

- 如果 key > root.val，说明要删除的节点在右子树，root.right = deleteNode(root.right, key)。
- 如果 key < root.val，说明要删除的节点在左子树，root.left = deleteNode(root.left, key)。
- 如果 key == root.val，则该节点就是我们要删除的节点，则：
  - 如果该节点是叶子节点，则直接删除它：root = null。
  - 如果该节点不是叶子节点且有右节点，则用它的后继节点的值替代 root.val = successor.val，然后删除后继节点。
  - 如果该节点不是叶子节点且只有左节点，则用它的前驱节点的值替代 root.val = predecessor.val，然后删除前驱节点。
- 返回 root。

### Python

1. 分开情况讨论

```python
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        def successor(root):
            root=root.right
            while root.left:
                root=root.left
            return root.val
        def predecessor(root):
            root=root.left
            while root.right:
                root=root.right
            return root.val
        
        if not root:return None
        if root.val>key:
            root.left=self.deleteNode(root.left,key)
        elif root.val<key:
            root.right=self.deleteNode(root.right,key)
        else:
            if not root.left and not root.right:root=None
            elif root.right:
                root.val=successor(root)
                root.right=self.deleteNode(root.right,root.val)
            else:
                root.val=predecessor(root)
                root.left=self.deleteNode(root.left,root.val)
        return root
```


```python

```



### C++

```cpp

```

---



# 整理与总结

![在这里插入图片描述](medium-450/0cc0a63c4c063977e74374a94ab4f6ed4e7cad94ddc52b99ab3afcff073738c1-file_1576477912261.jfif)

![在这里插入图片描述](medium-450/309271bd1f94c57fd4e19f5eee624dd2ad3ef8e4d5a3b6eca5556e9f2e43a3bc-file_1576477912310.jfif)

1. Successor 代表的是中序遍历序列的下一个节点。即比当前节点大的最小节点，简称后继节点。 先取当前节点的右节点，然后一直取该节点的左节点，直到左节点为空，则最后指向的节点为后继节点。

   ```python
   def successor(root):
       root = root.right
       while root.left:
           root = root.left
       return root
   ```

2. Predecessor 代表的是中序遍历序列的前一个节点。即比当前节点小的最大节点，简称前驱节点。先取当前节点的左节点，然后取该节点的右节点，直到右节点为空，则最后指向的节点为前驱节点。

   ```python
   def predecessor(root):
       root = root.left
       while root.right:
           root = root.right
       return root
   ```

   




