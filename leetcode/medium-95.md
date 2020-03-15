---
title: medium-95
tags:
  - LeetCode
description: ''
urlname: medium-95
date: 2020-03-11 18:10:41
---

# 题目

https://leetcode-cn.com/problems/unique-binary-search-trees-ii/

> 给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。
>
> 示例:
>
> 输入: 3
> 输出:
> [
>   [1,null,3,2],
>   [3,2,null,1],
>   [3,1,null,null,2],
>   [2,1,3],
>   [1,null,2,null,3]
> ]
> 解释:
> 以上的输出对应以下 5 种不同结构的二叉搜索树：
>
>    1         3     3      2      1
>     \       /     /      / \      \
>      3     2     1      1   3      2
>     /     /       \                 \
>    2     1         2                 3



# 解题思路 √

### Python

1. **分治**

```python
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generate_tree(start,end):
            if start>end:return [None]

            result=[]
            for i in range(start,end+1):
                left=generate_tree(start, i-1)
                right=generate_tree(i+1, end)
                
                for x in left:
                    for y in right:
                        currNode=TreeNode(i)
                        currNode.left=x
                        currNode.right=y
                        result.append(currNode)
            return result
        return generate_tree(1,n) if n else []
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

