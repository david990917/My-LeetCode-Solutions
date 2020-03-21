---
title: easy-232
tags:
  - LeetCode
description: 'Implement Queue using Stacks'
urlname: easy-232
date: 2019-09-01 16:50:01
---

# 题目

[用栈实现队列](https://leetcode-cn.com/problems/implement-queue-using-stacks/)

使用栈实现队列的下列操作：

- push(x) -- 将一个元素放入队列的尾部。
- pop() -- 从队列首部移除元素。
- peek() -- 返回队列首部的元素。
- empty() -- 返回队列是否为空。

**示例:**

```
MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // 返回 1
queue.pop();   // 返回 1
queue.empty(); // 返回 false
```

**说明:**

- 你只能使用标准的栈操作 -- 也就是只有 `push to top`, `peek/pop from top`, `size`, 和 `is empty` 操作是合法的。
- 你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
- 假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。

# 解题思路 √

这道题目是让我们用栈来模拟实现队列。 我们直到栈和队列都是一种受限的数据结构。 栈的特点是只能在一端进行所有操作，队列的特点是只能在一端入队，另一端出队。

在这里我们可以借助另外一个栈，也就是说用两个栈来实现队列的效果。这种做法的时间复杂度和空间复杂度都是O(n)。

由于栈只能操作一端，因此我们peek或者pop的时候也只去操作顶部元素，要达到目的 我们需要在push的时候将队头的元素放到栈顶即可。

因此我们只需要在push的时候，用一下辅助栈即可。 具体做法是先将栈清空并依次放到另一个辅助栈中，辅助栈中的元素再次放回栈中，最后将新的元素push进去即可。

比如我们现在栈中已经是1，2，3，4了。 我们现在要push一个5.

push之前是这样的：

[![232.implement-queue-using-stacks.drawio](easy-232/232.implement-queue-using-stacks-1.jpg)](https://github.com/azl397985856/leetcode/blob/master/assets/problems/232.implement-queue-using-stacks-1.jpg)

然后我们将栈中的元素转移到辅助栈：

[![232.implement-queue-using-stacks.drawio](easy-232/232.implement-queue-using-stacks-2.jpg)](https://github.com/azl397985856/leetcode/blob/master/assets/problems/232.implement-queue-using-stacks-2.jpg)

最后将新的元素添加到栈顶。

[![232.implement-queue-using-stacks.drawio](easy-232/232.implement-queue-using-stacks-3.jpg)](https://github.com/azl397985856/leetcode/blob/master/assets/problems/232.implement-queue-using-stacks-3.jpg)

整个过程是这样的：

[![232.implement-queue-using-stacks.drawio](easy-232/232.implement-queue-using-stacks-4.jpg)](https://github.com/azl397985856/leetcode/blob/master/assets/problems/232.implement-queue-using-stacks-4.jpg)

## 关键点解析

- 在push的时候利用辅助栈(双栈)

# Python

```python
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.help_stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while self.stack:
            self.help_stack.append(self.stack.pop())
        self.stack.append(x)
        while self.help_stack:
            self.stack.append(self.help_stack.pop())
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```



# 整理与总结

1. 因为 pop  peek 是两个操作，为了方便他们。选择的是 push 的时候麻烦一些。

