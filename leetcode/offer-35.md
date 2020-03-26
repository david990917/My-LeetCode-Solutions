---
title: offer-35
tags:
  - LeetCode
description: ''
urlname: offer-35
date: 2020-03-26 23:09:04
---

# 题目

[复杂链表的复制](https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/)

请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。 

示例 1：

![img](offer-35/e1.png)

```
输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
```


示例 2：

![img](offer-35/e2.png)

```
输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]
```


示例 3：

![img](offer-35/e3.png)

```
输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]
```


示例 4：

```
输入：head = []
输出：[]
解释：给定的链表为空（空指针），因此返回 null。
```



# 解题思路 √

> 浅拷贝只复制指向某个对象的指针，而不复制对象本身，新旧对象还是共享同一块内存。但深拷贝会另外创造一个一模一样的对象，新对象跟原对象不共享内存，修改新对象不会改到原对象。
>

![2.png](offer-35/166afb3c11f82e09fdf3dd5e01731f12d73ae21c328b5981957a86b109e52c14-2.png)

### Python

1. 实际上就是深拷贝

```python
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        return copy.deepcopy(head)
```

2. 深度优先
   - 从头结点 head 开始拷贝；
   - 由于一个结点可能被多个指针指到，因此如果该结点已被拷贝，则不需要重复拷贝；
   - 如果还没拷贝该结点，则创建一个新的结点进行拷贝，并将拷贝过的结点保存在哈希表中；
   - 使用递归拷贝所有的 next 结点，再递归拷贝所有的 random 结点。


```python
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        def dfs(head):
            if not head:return None
            if head in visited:
                return visited[head]
            copy=Node(head.val)
            visited[head]=copy
            copy.next=dfs(head.next)
            copy.random=dfs(head.random)
            return copy
        visited={}
        return dfs(head)
```

3. 广度优先
   - 创建哈希表保存已拷贝结点，格式 {原结点：拷贝结点}
   - 创建队列，并将头结点入队；
   - 当队列不为空时，弹出一个结点，如果该结点的 next 结点未被拷贝过，则拷贝 next 结点并加入队列；同理，如果该结点的 random 结点未被拷贝过，则拷贝 random 结点并加入队列；

```python
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        visited={}
        
        def bfs(head):
            if not head:return head
            clone=Node(head.val)
            queue=collections.deque()
            queue.append(head)
            visited[head]=clone
            while queue:
                node=queue.pop()
                if node.next and node.next not in visited:
                    visited[node.next]=Node(node.next.val)
                    queue.append(node.next)
                if node.random and node.random not in visited:
                    visited[node.random]=Node(node.random.val)
                    queue.append(node.random)
                visited[node].next=visited.get(node.next)
                visited[node].random=visited.get(node.random)
            return clone
        
        return bfs(head)
```



### C++

```cpp

```

---



# 整理与总结

1. 

