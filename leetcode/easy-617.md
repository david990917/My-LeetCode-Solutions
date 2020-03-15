---
title: easy-617
tags:
  - LeetCode
description: ''
urlname: easy-617
date: 2020-03-10 13:44:01
---

# 题目

https://leetcode-cn.com/problems/merge-two-binary-trees/

> 给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
>
> 你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则**不为** NULL 的节点将直接作为新二叉树的节点。
>
> **示例 1:**
>
> ```
> 输入: 
> 	Tree 1                     Tree 2                  
>           1                         2                             
>          / \                       / \                            
>         3   2                     1   3                        
>        /                           \   \                      
>       5                             4   7                  
> 输出: 
> 合并后的树:
> 	     3
> 	    / \
> 	   4   5
> 	  / \   \ 
> 	 5   4   7
> ```



# 解题思路 √

都是以T1作为基础，然后再在上面进行修改、填充。

### Python

1. 如果当前两个树都为非空，则值相加，若有一个为空，则返回另外一个。

```python
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and t2:
            return t2
        elif t1 and t2:
            t1.val+=t2.val
            t1.left=self.mergeTrees(t1.left,t2.left)
            t1.right=self.mergeTrees(t1.right, t2.right)
        return t1
```

2. 复习了前序遍历


```python
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:return t2
        if not t2:return t1

        stack1=[t1]
        stack2=[t2]

        while stack1:
            node1=stack1.pop()
            node2=stack2.pop()
            node1.val=node1.val+node2.val
            if node1.right and node2.right:
                stack1.append(node1.right)
                stack2.append(node2.right)
            elif node2.right:
                node1.right=node2.right
            
            if node1.left and node2.left:
                stack1.append(node1.left)
                stack2.append(node2.left)
            elif node2.left:
                node1.left=node2.left
        return t1
```



### C++

```cpp

```

---



# 整理与总结

1. 

