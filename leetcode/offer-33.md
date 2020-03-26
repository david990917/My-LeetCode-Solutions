---
title: offer-33
tags:
  - LeetCode
description: ''
urlname: offer-33
date: 2020-03-26 21:51:23
---

# 题目

[二叉搜索树的后序遍历序列](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/)

输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。 

参考以下这颗二叉搜索树：

```
     5
    / \
   2   6
  / \
 1   3
```

示例 1：

```
输入: [1,6,3,2,5]
输出: false
```


示例 2：

```
输入: [1,3,2,6,5]
输出: true
```


提示：

数组长度 <= 1000



# 解题思路 √

### Python

1. 切分-递归判断

```python
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if not postorder:return True
        length=len(postorder)
        root=postorder[-1]
        for i in range(length):
            if postorder[i]>root:
                break
            
        for j in range(i,length-1):
            if postorder[j]<root:
                return False

        left=self.verifyPostorder(postorder[:i]) if i>0 else True
        right=self.verifyPostorder(postorder[i:-1]) if i<length-1 else True
        return left and right
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

