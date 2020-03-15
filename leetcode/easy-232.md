---
title: easy-232
tags:
  - LeetCode
description: 'Implement Queue using Stacks'
urlname: easy-232
date: 2019-09-01 16:50:01
---

# 题目

https://leetcode.com/problems/implement-queue-using-stacks/description/

Implement the following operations of a queue using stacks.

- push(x) -- Push element x to the back of queue.
- pop() -- Removes the element from in front of queue.
- peek() -- Get the front element.
- empty() -- Return whether the queue is empty.

**Example:**

```
MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
```

**Notes:**

- You must use *only* standard operations of a stack -- which means only `push to top`, `peek/pop from top`, `size`, and `is empty` operations are valid.
- Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
- You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

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

