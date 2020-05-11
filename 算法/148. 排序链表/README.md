| [English](README_EN.md) | 简体中文 |

# [148. 排序链表](https://leetcode-cn.com/problems/sort-list)
<p>在&nbsp;<em>O</em>(<em>n</em>&nbsp;log&nbsp;<em>n</em>) 时间复杂度和常数级空间复杂度下，对链表进行排序。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> 4-&gt;2-&gt;1-&gt;3
<strong>输出:</strong> 1-&gt;2-&gt;3-&gt;4
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> -1-&gt;5-&gt;3-&gt;4-&gt;0
<strong>输出:</strong> -1-&gt;0-&gt;3-&gt;4-&gt;5</pre>

**标签:**  [排序](https://leetcode-cn.com/tag/sort) [链表](https://leetcode-cn.com/tag/linked-list) 
 ### 相似题目
- 简单:	[合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists) 
- 中等:	[颜色分类](https://leetcode-cn.com/problems/sort-colors) 
- 中等:	[对链表进行插入排序](https://leetcode-cn.com/problems/insertion-sort-list) 

# 解题思路 √

### Python

1. 找中点  + 递归 + Merge

![Picture2.png](README/8c47e58b6247676f3ef14e617a4686bc258cc573e36fcf67c1b0712fa7ed1699-Picture2.png)

```python
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:return head
        # Cut
        slow,fast=head,head.next
        while fast and fast.next:
            fast,slow=fast.next.next,slow.next
        slow.next,mid=None,slow.next
        # Recursion
        left,right=self.sortList(head),self.sortList(mid)
        # Merge
        h=res=ListNode(0)
        while left and right:
            if left.val<right.val:h.next,left=left,left.next
            else:h.next,right=right,right.next
            h=h.next
        h.next=left if left else right
        return res.next
```

2. 从底至顶直接合并 - 这个没咋看懂


```python
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        h,length,intv=head,0,1
        while h: h,length=h.next,length+1
        res=ListNode(0)
        res.next=head
        # Merge
        while intv<length:
            pre,h=res,res.next
            while h:
                h1,i=h,intv
                while i and h:h,i=h.next,i-1
                if i:break
                h2,i=h,intv
                while i and h:h,i=h.next,i-1
                c1,c2=intv,intv-i
                while c1 and c2:
                    if h1.val<h2.val:pre.next,h1,c1=h1,h1.next,c1-1
                    else:pre.next,h2,c2=h2,h2.next,c2-1
                    pre=pre.next
                pre.next=h1 if c1 else h2
                while c1>0 or c2>0:pre,c1,c2=pre.next,c1-1,c2-1
                pre.next=h
            intv*=2
        return res.next
```

### C++

```cpp

```

---



# 整理与总结

1. 