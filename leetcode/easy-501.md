---
title: easy-501
tags:
  - LeetCode
description: ''
urlname: easy-501
date: 2020-03-21 23:25:42
---

# 题目

[二叉搜索树中的众数](https://leetcode-cn.com/problems/find-mode-in-binary-search-tree/)

给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。

假定 BST 有如下定义：

结点左子树中所含结点的值小于等于当前结点的值
结点右子树中所含结点的值大于等于当前结点的值
左子树和右子树都是二叉搜索树
例如：

```
给定 BST [1,null,2,2],

   1
    \
     2
    /
   2
返回[2].
```

提示：如果众数超过1个，不需考虑输出顺序

进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）

# 解题思路 √

### Python

1. 容易的-只用操作最中心的元素就可以啦

```python
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        self.currCount,self.maxCount,self.preVal,self.result=0,0,None,[]
        def inorder(root):
            if not root:return
            inorder(root.left)
            if isinstance(self.preVal,int):
                if root.val==self.preVal:self.currCount+=1
                else:self.currCount=1
                if self.currCount==self.maxCount:
                    self.result.append(root.val)
                elif self.currCount>self.maxCount:
                    self.maxCount=self.currCount
                    self.result=[root.val]
            else:
                self.currCount=1
                self.maxCount=1
                self.result=[root.val]
            self.preVal=root.val
            inorder(root.right)
            
        inorder(root)
        return self.result
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

