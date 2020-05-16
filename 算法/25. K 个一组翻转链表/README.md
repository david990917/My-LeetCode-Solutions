| [English](README_EN.md) | 简体中文 |

# [25. K 个一组翻转链表](https://leetcode-cn.com/problems/reverse-nodes-in-k-group)
<p>给你一个链表，每&nbsp;<em>k&nbsp;</em>个节点一组进行翻转，请你返回翻转后的链表。</p>

<p><em>k&nbsp;</em>是一个正整数，它的值小于或等于链表的长度。</p>

<p>如果节点总数不是&nbsp;<em>k&nbsp;</em>的整数倍，那么请将最后剩余的节点保持原有顺序。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<p>给你这个链表：<code>1-&gt;2-&gt;3-&gt;4-&gt;5</code></p>

<p>当&nbsp;<em>k&nbsp;</em>= 2 时，应当返回: <code>2-&gt;1-&gt;4-&gt;3-&gt;5</code></p>

<p>当&nbsp;<em>k&nbsp;</em>= 3 时，应当返回: <code>3-&gt;2-&gt;1-&gt;4-&gt;5</code></p>

<p>&nbsp;</p>

<p><strong>说明：</strong></p>

<ul>
	<li>你的算法只能使用常数的额外空间。</li>
	<li><strong>你不能只是单纯的改变节点内部的值</strong>，而是需要实际进行节点交换。</li>
</ul>

**标签:**  [链表](https://leetcode-cn.com/tag/linked-list) 
 ### 相似题目
- 中等:	[两两交换链表中的节点](https://leetcode-cn.com/problems/swap-nodes-in-pairs) 

# 解题思路 √

### Python

1. 照着图片慢慢操作就好啦

![k个一组翻转链表.png](https://pic.leetcode-cn.com/866b404c6b0b52fa02385e301ee907fc015742c3766c80c02e24ef3a8613e5ad-k%E4%B8%AA%E4%B8%80%E7%BB%84%E7%BF%BB%E8%BD%AC%E9%93%BE%E8%A1%A8.png)

```python
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        pre, end = dummy, dummy

        while end.next:
            # 取出待翻转的部分
            i = 0
            while i < k and end:
                end = end.next
                i += 1
            if not end: break

            # 断开链表
            startNode = pre.next
            nextNode = end.next
            end.next = None

            # 处理翻转 
            pre.next = self.reverse(startNode)
            # startNode 转到翻转这部分节点的最后了

            # 连接断开的链表
            startNode.next = nextNode

            # 挪动以进行下一组处理
            pre = startNode
            end = pre
        return dummy.next

    def reverse(self, head):
        pre = None
        curr = head
        while curr:
            nextNode = curr.next
            curr.next = pre
            pre = curr
            curr = nextNode
        return pre
```


```python

```

### C++

```cpp

```

---



# 整理与总结

1. 