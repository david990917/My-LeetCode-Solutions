---
title: medium-102
tags:
  - LeetCode
description: ''
urlname: medium-102
date: 2020-03-10 14:44:28
---

# 题目

> 给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。
>
> 例如:
> 给定二叉树: [3,9,20,null,null,15,7],
>
>     3
>    / \
>   9  20
>     /  \
>    15   7
> 返回其层次遍历结果：
>
> [
>   [3],
>   [9,20],
>   [15,7]
> ]
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



# 解题思路 √

### Python

1. 直接操作就可以了，按照层次遍历的方式。

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
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
        return result
```

2. 递归
   - 不能直接输出的 - 往往是通过内部函数来递归
   - level可以作为一个全局可以识别的参数


```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result=[]
        if not root:return result

        def helper(root,level):
            # Initialize for the current level
            if len(result)==level:result.append([])
            result[level].append(root.val)
            if root.left: helper(root.left,level+1)
            if root.right:helper(root.right,level+1)

        helper(root,0)
        return result
```



### C++

```cpp

```

---



# 整理与总结

1. 

