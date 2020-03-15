---
title: easy-107
tags:
  - LeetCode
description: ''
urlname: easy-107
date: 2020-03-10 14:25:01
---

# 题目

> 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
>
> 例如：
> 给定二叉树 [3,9,20,null,null,15,7],
>
>     3
>    / \
>   9  20
>     /  \
>    15   7
> 返回其自底向上的层次遍历为：
>
> [
>   [15,7],
>   [9,20],
>   [3]
> ]
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



# 解题思路 √

### Python

1. 基于正序，然后输出逆序

```python
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:return []
        que=[[root,0]]
        height,currResult,result=0,[],[]
        while que:
            node,currheight=que.pop(0)
            if currheight>height:
                height=currheight
                result.append(currResult)
                currResult=[]
            currResult.append(node.val)
            if node.left:que.append([node.left,currheight+1])
            if node.right:que.append([node.right,currheight+1])
        result.append(currResult)
        return result[::-1]
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

