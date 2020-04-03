---
title: offer-36
tags:
  - LeetCode
description: ''
urlname: offer-36
date: 2020-03-27 08:39:16
---

# 题目

[二叉搜索树与双向链表](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof) 

输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。

 

为了让您更好地理解问题，以下面的二叉搜索树为例：

 ![img](offer-36/bstdlloriginalbst.png)

我们希望将这个二叉搜索树转化为双向循环链表。链表中的每个节点都有一个前驱和后继指针。对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。

下图展示了上面的二叉搜索树转化成的链表。“head” 表示指向链表中有最小元素的节点。

 ![img](offer-36/bstdllreturndll.png)

特别地，我们希望可以就地完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中的第一个节点的指针。

# 解题思路 √

### Python

1. 中序遍历操作

```python
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:return None
        self.head=None
        self.prev=None
        def inorder(root):
            if not root:return
            inorder(root.left)
            if self.prev==None:
                self.head=root
            else:
                self.prev.right=root
                root.left=self.prev
            self.prev=root
            inorder(root.right)
        inorder(root)
        self.head.left,self.prev.right=self.prev,self.head
        return self.head
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

