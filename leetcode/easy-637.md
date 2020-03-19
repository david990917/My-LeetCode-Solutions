---
title: easy-637
tags:
  - LeetCode
description: '二叉树的层平均值'
urlname: easy-637
date: 2020-03-10 15:22:51
---

# 题目

https://leetcode-cn.com/problems/average-of-levels-in-binary-tree/

给定一个非空二叉树, 返回一个由每层节点平均值组成的数组.

**示例 1:**

```
输入:
    3
   / \
  9  20
    /  \
   15   7
输出: [3, 14.5, 11]
解释:
第0层的平均值是 3,  第1层是 14.5, 第2层是 11. 因此返回 [3, 14.5, 11].
```

**注意：**

1. 节点值的范围在32位有符号整数范围内。

# 解题思路 √

### Python

1. 基于前面的层次遍历方法

```python
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:return []
        que=[[root,0]]
        height,currResult,currCount,result=0,0,0,[]
        while que:
            node,currheight=que.pop(0)
            if currheight>height:
                height=currheight
                result.append(currResult/currCount)
                currResult,currCount=0,0
            currResult+=node.val
            currCount+=1
            if node.left:que.append([node.left,currheight+1])
            if node.right:que.append([node.right,currheight+1])
        result.append(currResult/currCount)
        return result
```


```python
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:return []
        from collections import deque
        deq=deque()
        deq.append(root)

        result=[]
        while deq:
            size=len(deq)
            value=0
            for i in range(size):
                node=deq.popleft()
                value+=node.val
                if node.left:deq.append(node.left)
                if node.right:deq.append(node.right)
            result.append(value/size)
        return result
```



### C++

```cpp

```

---



# 整理与总结

1. 整理一下层次遍历：

   ```
   
   ```

   

