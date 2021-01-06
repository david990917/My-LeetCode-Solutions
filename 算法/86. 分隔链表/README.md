| [English](README_EN.md) | 简体中文 |

# [86. 分隔链表](https://leetcode-cn.com/problems/partition-list)
<p>给你一个链表和一个特定值<em> </em><code>x</code> ，请你对链表进行分隔，使得所有小于 <code>x</code> 的节点都出现在大于或等于 <code>x</code> 的节点之前。</p>

<p>你应当保留两个分区中每个节点的初始相对位置。</p>

<p> </p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>head = 1->4->3->2->5->2, <em>x</em> = 3
<strong>输出：</strong>1->2->2->4->3->5
</pre>

**标签:**  [链表](https://leetcode-cn.com/tag/linked-list) [双指针](https://leetcode-cn.com/tag/two-pointers) 
# 解题思路 √

### Python

1. 链表的连接：直接维护一个链表不是很简洁，使用两个链表在单独操作的时候很简洁

```python
class Solution {
    public ListNode partition(ListNode head, int x) {
        ListNode small = new ListNode(0);
        ListNode smallHead = small;
        ListNode large = new ListNode(0);
        ListNode largeHead = large;
        while (head != null) {
            if (head.val < x) {
                small.next = head;
                small = small.next;
            } else {
                large.next = head;
                large = large.next;
            }
            head = head.next;
        }
        large.next = null;
        small.next = largeHead.next;
        return smallHead.next;
    }
}
```


```python

```

### C++

```cpp

```

---



# 整理与总结

1. 