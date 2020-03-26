---
title: offer-32
tags:
  - LeetCode
description: ''
urlname: offer-32
date: 2020-03-26 21:39:57
---

# 题目

[从上到下打印二叉树](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/)

从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

例如:

```
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回：

[3,9,20,15,7]
```

# 解题思路 √

### Python

1. [从上到下打印二叉树](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/)

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:return []
        result=[]
        
        from collections import deque
        deq=deque()
        deq.append(root)
        
        while deq:
            node=deq.popleft()
            result.append(node.val)
            if node.left:deq.append(node.left)
            if node.right:deq.append(node.right)
        return result
```

2. [从上到下打印二叉树 II](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/)


```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:return []
        
        from collections import deque
        deq=deque()
        deq.append(root)
        result=[]
        
        while deq:
            length=len(deq)
            temp=[]
            for i in range(length):
                node=deq.popleft()
                temp.append(node.val)
                if node.left:deq.append(node.left)
                if node.right:deq.append(node.right)
            result.append(temp)
        return result
```

3. [从上到下打印二叉树 III](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/)

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:return []
        
        from collections import deque
        deq=deque()
        deq.append(root)
        result,flag=[],False
        
        while deq:
            temp=[]
            length=len(deq)
            for i in range(length):
                node=deq.popleft()
                temp.append(node.val)
                if node.left:deq.append(node.left)
                if node.right:deq.append(node.right)
            if flag:temp=temp[::-1]
            result.append(temp)
            flag=True if flag==False else False
        return result
```



### C++

```cpp

```

---



# 整理与总结

1. 

