---
title: medium-173
tags:
  - LeetCode
description: ''
urlname: medium-173
date: 2020-03-22 10:04:35
---

# 题目

[二叉搜索树迭代器](https://leetcode-cn.com/problems/binary-search-tree-iterator/)
实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。

调用 `next()` 将返回二叉搜索树中的下一个最小的数。

 

**示例：**

**![img](medium-173/bst-tree.png)**

```
BSTIterator iterator = new BSTIterator(root);
iterator.next();    // 返回 3
iterator.next();    // 返回 7
iterator.hasNext(); // 返回 true
iterator.next();    // 返回 9
iterator.hasNext(); // 返回 true
iterator.next();    // 返回 15
iterator.hasNext(); // 返回 true
iterator.next();    // 返回 20
iterator.hasNext(); // 返回 false
```

 

**提示：**

- `next()` 和 `hasNext()` 操作的时间复杂度是 O(1)，并使用 O(*h*) 内存，其中 *h* 是树的高度。
- 你可以假设 `next()` 调用总是有效的，也就是说，当调用 `next()` 时，BST 中至少存在一个下一个最小的数。

# 解题思路 √

### Python

1. 中序遍历常规思路

```python
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.result=self.inorder(root)
        self.idx=0
        
    def inorder(self,root):
        return self.inorder(root.left)+[root.val]+self.inorder(root.right) if root else []


    def next(self) -> int:
        """
        @return the next smallest number
        """
        val=self.result[self.idx]
        self.idx+=1
        return val
        


    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.idx!=len(self.result)
```

2. 使用栈来保存

我们调用 next()，我们需要返回二叉搜索树中的下一个最小元素，即栈的顶部元素。有两种可能性：

- 一个是栈顶部的节点是一个叶节点。这是最好的情况，因为我们什么都不用做，只需将节点从栈中弹出并返回其值。所以这是个常数时间的操作。
- 另一个情况是栈顶部的节点拥有右节点。我们不需要检查左节点，因为左节点已经添加到栈中了。栈顶元素要么没有左节点，要么左节点已经被处理了。如果栈顶部拥有右节点，那么我们需要对右节点上调用帮助函数。该时间复杂度取决于树的结构。


```python
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack=[]
        self.helper(root)
        
    def helper(self,root):
        while root:
            self.stack.append(root)
            root=root.left


    def next(self) -> int:
        """
        @return the next smallest number
        """
        result=self.stack.pop()
        if result.right:
            self.helper(result.right)
        return result.val


    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack)>0
```



### C++

```cpp

```

---



# 整理与总结

1. 

