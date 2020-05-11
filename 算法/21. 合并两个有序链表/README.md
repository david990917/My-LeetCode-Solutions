| [English](README_EN.md) | 简体中文 |

# [21. 合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists)
<p>将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>1-&gt;2-&gt;4, 1-&gt;3-&gt;4
<strong>输出：</strong>1-&gt;1-&gt;2-&gt;3-&gt;4-&gt;4
</pre>

**标签:**  [链表](https://leetcode-cn.com/tag/linked-list) 
 ### 相似题目
- 困难:	[合并K个排序链表](https://leetcode-cn.com/problems/merge-k-sorted-lists) 
- 简单:	[合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array) 
- 中等:	[排序链表](https://leetcode-cn.com/problems/sort-list) 
- 中等:	[最短单词距离 II](https://leetcode-cn.com/problems/shortest-word-distance-ii) 

# 解题思路 √

### Python

1. 

```python

```


```python

```

### C++

正常操作就可以啦

```cpp
class Solution {
public:
	ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
		ListNode* head = new ListNode(0);
		ListNode* curr = head;
		while (l1 and l2) {
			ListNode* tmp = NULL;
			if (l1->val < l2->val) {
				tmp = new ListNode(l1->val);
				l1 = l1->next;
			}
			else {
				tmp = new ListNode(l2->val);
				l2 = l2->next;
			}
			curr->next = tmp;
			curr = curr->next;
		}
		if (l1) { curr->next = l1; }
		if (l2) { curr->next = l2; }
		return head->next;
	}
};
```

---



# 整理与总结

1. 